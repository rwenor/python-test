
def AxHex(hex):
    assert(hex[0]=='#')
    
    return int(hex[1:], 16)
    

str = " 79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a1383c,25,-273,22,-39,315,-30,28,1,55`"

ve_list = [ "32 VEINI,3301,1670055,1,#03080f31",
 "78 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a11da9,18,-283,20,-23,305,-19,0,1,58`",
 "78 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a1227f,20,-307,20,-28,342,-20,0,1,58`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a13317,16,-214,17,-30,388,-30,30,1,28`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a1383c,25,-273,22,-39,315,-30,28,1,55`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a13da5,14,-306,19,-27,286,-20,14,1,58`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a148ff,28,-274,29,-39,318,-34,23,1,56`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a14e63,34,-302,32,-48,290,-33,23,1,68`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a153e6,25,-317,29,-35,366,-28,18,1,62`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a159a7,22,-305,26,-30,364,-34,13,1,64`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a15b7d,12,-350,18,-19,279,-13,21,1,51`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1607e,22,-385,27,-25,215,-16,14,1,32`",
 "79 VEFRO,3301,1670055,1,#55A368A15B7D,#55A368A164CB,0,-4481,-4470,234,200,200,32",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a15f1f,37,-306,36,-45,382,-48,47,1,70`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1658d,14,-346,26,-19,298,-10,12,1,40`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a1648d,37,-282,35,-49,373,-51,36,1,53`",
 "78 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a16b4e,15,-524,18,-21,249,-11,8,1,18`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,3,#55a368a169e6,25,-246,24,-40,466,-52,35,1,22`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a170bb,23,-312,21,-22,485,-26,42,1,43`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a17612,24,-351,23,-34,314,-34,29,1,45`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a17b3c,19,-255,24,-45,237,-24,17,1,59`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a180c5,22,-371,20,-15,464,-26,27,1,52`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1866a,22,-251,27,-37,407,-34,43,1,47`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a18bab,35,-276,31,-39,391,-44,44,1,54`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a190f0,30,-280,27,-43,410,-36,22,1,54`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a196b3,28,-262,29,-44,451,-40,43,1,41`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a19c41,39,-280,39,-52,396,-55,59,1,63`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1a19d,45,-256,45,-75,382,-58,40,1,56`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1a6fd,46,-264,35,-58,427,-57,37,1,40`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1acaf,34,-254,31,-56,415,-56,52,1,40`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1b258,46,-276,43,-66,417,-65,58,1,57`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1b7db,47,-251,39,-66,405,-71,53,1,47`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1bd6a,39,-263,32,-60,392,-66,38,1,39`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1ce4f,24,-230,21,-44,458,-58,39,1,15`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1d3e9,15,-224,16,-33,454,-47,33,1,11`",
 "79 VEDMP,3301,1670055,1,`PZACT,3,1,#55a368a1df78,16,-245,18,-28,461,-41,32,1,18`",
 "82 VEPAS,3301,1670055,1,SP,#55A368A15B7D,2,-4481,0,200,18,20,-4470,232,200,27,20,32"]

str = str[4:] # skip length
d = str.strip().split(',')

print d

#for i, itm in enumerate(d):
#    print i, ':', itm 
    
    
if d[4] == "`PZACT":
    print AxHex(d[7])    


# ***    
class VE:
    def __init__(self, veNr):
        self.veNr = veNr
        self.pz = {}
        self.first = {}
        self.last = {}
        
    def __str__(self):
        return self.veNr + ': ' + repr(self.pz)
        
    def add_pz(self, time, sens, sig):
        #if sens not in self.first:
        if sens not in self.pz:
            self.pz[sens] = []
            self.first[sens] = time
            self.last[sens] = time
            
        self.pz[sens].append((time - self.first[sens], time - self.last[sens], sig))
        self.last[sens] = time
    
    
# ***    
class VE_Pars:
    
    def __init__(self):
        self.ve = {}
    
    def ParsLine(self, str):
        str = str[3:] # skip length
        d = str.strip().split(',')

        veNr = d[2]
        print 'veNr:', veNr
        
        if veNr in self.ve:
            ve = self.ve[veNr]
        else: # nytt kjt.
            ve = VE(veNr)
            self.ve[veNr] = ve
            
        print d
        
    
        if d[0] == "VEPAS":
            print 'PASS'
            print ve
            del self.ve[veNr]
            
        if d[4] == "`PZACT":
            print AxHex(d[7])  
            ve.add_pz(AxHex(d[7]), d[6], int(d[10]))
            
        #print ve 
        
        
    
if __name__ == '__main__':
    ## Test    
    import unittest
    
    
    class TestStringMethods(unittest.TestCase):

      def test_ParsVE(self):
          print '\nLeser et kjt.'
          vep = VE_Pars()
          vep.ParsLine(str)

      def test_ParsVE_lines(self):
          print '\nLeser et helt kjt.'
          vep = VE_Pars()
          for line in ve_list:
              vep.ParsLine(line)
    
    
    print '*'*40      
    print 'Test: '
    unittest.main()
    