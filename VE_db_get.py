#!/usr/bin/env python
import logging
import os
import sys
import time
from datetime import datetime

import SocketServer
from threading import Thread

from ConfigParser import SafeConfigParser
try:
    import MySQLdb
except:
    import pymysql as MySQLdb


conCount = 0
totCon = 0
serverRun = True


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

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

    #sLog.debug('New db cursor')
    return dbAxs, dbAxs.cursor()


def axs_close(dbAxs, curAxs):
    #sLog.debug('Close db')
    curAxs.close()
    dbAxs.close()


ax_id = 3306
f_nr = 1

i = 0
for arg in sys.argv:
    i = i + 1
    if i < 2:
        continue
    
    print i, " ", arg
    if i == 2:
        ax_id = int(arg)
    if i == 3:
        f_nr = int(arg)    

sys.stderr.write( 'AX_ID: '+ str(ax_id)  +'  Felt: '+ str(f_nr) +'\n')

db, cur = axs_cursor()
# qry = 'select count(*) from axs_vepas where axspeed_id = 3305 and datotid > "2016-02-01 16:00:00" and linje_id = 0'
qry = 'select p1.a_s1, p1.a_s2, p2.a_s1, p2.a_s2, v_nr, ve.datotid '
qry += ' from axs_vepas ve '
qry += '   join axs_vepas_p p1 on (ve.axs_vepas_id = p1.axs_vepas_id and p1.axs_vepas_aksel_nr = 1 ) '
qry += '   join axs_vepas_p p2 on (ve.axs_vepas_id = p2.axs_vepas_id and p2.axs_vepas_aksel_nr = 2 ) '
qry += ' where axspeed_id = '+ str(ax_id) 
qry += ' and datotid > "2016-01-02 16:00:00" and linje_id = '+ str(f_nr - 1)

# print qry, ';'

cur.execute(qry)
for row in cur:
    print row[0], row[1], row[2], row[3], str(ax_id) +'-13', row[4], row[5]
    #for i, e in enumerate(row):
    #    print i, e
      
      
      
sys.stderr.write( 'Rader returnert: '+ str(cur.rowcount)  +'\n' )

# sLog.info('Close connection')
axs_close(db, cur)

