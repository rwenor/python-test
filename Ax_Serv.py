#!/usr/bin/env python
import logging
import os
import sys

import SocketServer
from threading import Thread

conCount = 0
totCon = 0
serverRun = True

from ConfigParser import SafeConfigParser
import MySQLdb
import time
from datetime import datetime


logging.basicConfig(stream=sys.stdout, level=logging.INFO)

sLog = logging.getLogger('Server')
fLog = sLog 


def axs_getdb():
    cfg = SafeConfigParser()
    cfg.read('axs_serv.ini')
    return MySQLdb.connect(host=cfg.get('axs_db', 'host'),
                                    user=cfg.get('axs_db', 'user'),
                                    passwd=cfg.get('axs_db', 'passwd'),
                                    db=cfg.get('axs_db', 'db'))

def axs_cursor():   
    #if not dbAxs.open:
    #    sLog.debug('Connect...')
    dbAxs = axs_getdb()
    sLog.debug('New db cursor')
    return dbAxs, dbAxs.cursor()


def axs_close(dbAxs, curAxs):
    sLog.debug('Close db')
    curAxs.close()
    dbAxs.close()

    
db, cur = axs_cursor()

qry = 'select count(*) from axs_vepas'
print qry, ';'
cur.execute(qry)
for row in cur:
    print row
print '\n'

sLog.info('Close connection')
axs_close(db, cur)

db, cur = axs_cursor()
qry = 'select count(*) from axs_vepas'
print qry, ';'
cur.execute(qry)
for row in cur:
    print row
print '\n'

sLog.info('Close connection')
axs_close(db, cur)


def AxTime(hex):
    if hex[0]=='#':
        return int(hex[1:], 16)/65536.0
    else:
        print "Mangler #!: ", hex
        return int(hex, 16)/65536.0
    

def sqlstr(s):
    return '"'+ str(s) + '"'


def addToVE(s):
    with open("VE_ok.dat", "a") as myfile:
        myfile.write(s)


def addToFail(s):
    with open("failVE.dat", "a") as myfile:
        myfile.write(s)



class service(SocketServer.BaseRequestHandler):
    def handle_timeout(self):
        print 'Timeout ...'

    def handle(self):
        global conCount, totCon


        vp = VePars()

        self.log = logging.getLogger(str(self.client_address))
        logging.basicConfig(level=logging.INFO)
        log = self.log
        
        data = 'dummy'
        resCnt = 0

        self.request.settimeout(15)

        conCount += 1
        totCon += 1

        log.info('Connected from '+ str(self.client_address) +' #'+ str(conCount) + ':'+ str(totCon))
        log.info('Tid: '+ str(datetime.now()) )
            
        ret = '200 Connected from '+ str(self.client_address) +' #'+ str(conCount) + ':'+ str(totCon)
        log.debug('< '+ ret)
        self.request.send(ret + '\r\n')

        # Get new cursor
        dbAxs, curAxs = axs_cursor()
        
        # ta mot data til "." er motatt
        while len(data):
            
            try:
                data = ''
                while data[-1:] <> '\n':
                    
                    d = self.request.recv(1)  # Hvis det kommer mer en ventet....
                    if d:
                        data += d
                    else:
                        addToFail('Con. lost: ' + data)
                        data = d  # Connection lost
                        break

                    #for c in data[-2:]:
                    #    print c, ord(c)
                    
            except Exception as e:
                log.exception(str(e))
                break
    
            if not data:
                self.log.warning('Connection lost')
                break
            
            log.debug( str(resCnt) +'> '+ data.rstrip() +' -Len='+ str(len(data)))


            # Handle request
            if "." == data.rstrip():
                ret = '201 BYE'
            elif data[0] == 'V':

                try:
                    vp.pars(data, dbAxs, curAxs, log)
                    addToVE(data)
                    ret = '210 OK'
                    resCnt += 1
                    #print "210 OK: ", resCnt,
                except Exception as ex:
                    addToFail(data)
                    log.error('*** Parse feil: '+ str( ex ))
                    ret = '410 ERROR'

            elif data[0] == 'H':

                try:
                    # vp.pars(data, dbAxs, curAxs, log)
                    addToVE(data)
                    ret = '210 OK'
                    resCnt += 1
                    #print "210 OK: ", resCnt,
                except Exception as ex:
                    addToFail(data)
                    log.error('*** Parse feil: '+ str( ex ))
                    ret = '410 ERROR'
                
                
            else:
                addToFail(data)
                ret = '410 ERROR'


            if ret[:3] <> '210':
                log.debug('< '+ ret)

            self.request.send(ret + '\r\n')

            # END ???
            if "." == data.rstrip():  break
            if not serverRun:
                log.info('Server stopped')
                break

        # print "Client exited", self.client_address
        
        axs_close(dbAxs, curAxs)
        log.info("Client exit. VE_Cnt: "+ str(resCnt) + " con: "+ str(totCon-1)) 
                      
        totCon -= 1
        self.request.close()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

SocketServer.ThreadingTCPServer.allow_reuse_address = True
# SocketServer.ThreadingTCPServer.timeout = 5
port = 1732 #os.getenv('PORT', '8080')
ip = '0.0.0.0' #os.getenv('IP', '0.0.0.0')
#print "Server on",  ip, port

t = ThreadedTCPServer((ip, port), service)

# t.setDaemon(True)
ip, port = t.server_address
print "Server on",  ip, port

try:
    t.serve_forever()
except:
    print "Stopping..."
    serverRun = False
