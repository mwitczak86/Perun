#Michal Witczak
import subprocess
from targets_db import TargetsDb
from rich import print

class DomainResolver:

    #checking if domain obj exists
    def domain_from_ip(self,id):
        for x in TargetsDb().targets:
            try:
                if x.id == id:
                    cmd = subprocess.Popen(["dig","-x",x.ipadd,"+short"], stdout=subprocess.PIPE)
                    output = cmd.stdout.read()
                    outstring = output.decode('utf-8')
                    self.string_decode(outstring,id)
            except:
                print("Sorry, no data avaible for given address...")
        
            
    #TLD resolver      
    def string_decode(self,outstring,id):
        print(outstring)
        
        firstdot=(outstring.index(".")+1)
        string=outstring[firstdot:]
        length = len(string)
        lastdot=string[length -2]
        
        
        if lastdot == ".":
            domain=(string[:(length-2)])
            print(domain)
        else:
            domain=(outstring[firstdot:])

        self.db_update(domain,id)
        
            
    #updating domain info in IpTarget object
    def db_update(self,domain,id):
        for x in TargetsDb().targets:
            if x.id == id:
                x.domain = domain
                x.print_details()
        print("[bright_cyan]Components database has been updated.")
        
