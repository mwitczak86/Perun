#Michal Witczak
import subprocess
from rich import print
from rich.panel import Panel 
from rich.console import Console
from rich.table import Table
from targets_db import TargetsDb


class DigTarget:

    
    #running 'dig' commands with dns responses
    def run_commands(self,domain):
        cmd = subprocess.Popen(["dig","any",domain], stdout=subprocess.PIPE)
        cmd2 = subprocess.Popen(["dig","+short",domain], stdout=subprocess.PIPE)
        cmd3 = subprocess.Popen(["dig","+short","ns",domain], stdout=subprocess.PIPE)
        cmd4 = subprocess.Popen(["dig","+short","txt",domain], stdout=subprocess.PIPE)
        cmd5 = subprocess.Popen(["dig","+short","mx",domain], stdout=subprocess.PIPE)
        
    
        output = cmd.stdout.readlines()
        output2 = cmd2.stdout.read()
        output3 = cmd3.stdout.read()
        output4 = cmd4.stdout.read()
        output5 = cmd5.stdout.read()
        
            

        self.dns_resolver(output, output2,output3,output4,output5,domain)
    #decoding dns response to utf-8
    def dns_resolver(self,output,output2,output3,output4,output5,domain):
        out2string = output2.decode('utf-8')
        out3string = output3.decode('utf-8')
        out4string = output4.decode('utf-8')
        out5string = output5.decode('utf-8')
        
        res=[]
        res.append(output)
        console=Console()
        first=(res[0])
       
        stringlist=[x.decode('utf-8') for x in first]
        
        

        self.print_info(stringlist,out2string,out3string,out4string,out5string,domain)

    
        

    #output with 'rich' tables
    def print_info(self,stringlist,out2string,out3string,out4string,out5string,domain):
        console=Console()
        console.clear()
        plist=[]
        for i in stringlist[13:]:
                a=i.strip(";;")
                b=a.replace("\t\t",": ")
                c=b.replace("\t",", ")
                plist.append(c)
        joined_string = "".join(plist) 
                   
        ip=(Panel.fit(("[white]"+domain + ":\n" +"[yellow1]"+ out2string), title="Dig Short Answer", subtitle="ip address", padding=1, border_style ="bright_cyan"))
        ns=(Panel.fit(("[white]"+domain + " ns:\n" +"[yellow1]"+ out3string), title="Dig Short Answer", subtitle="ns names", padding=1, border_style ="bright_cyan"))
        txt=(Panel.fit(("[white]"+domain + " txt:\n" +"[yellow1]"+ out4string), title="Dig Short Answer", subtitle="txt records", padding=1, border_style ="bright_cyan"))
        mx=(Panel.fit(("[white]"+domain + " mx:\n" +"[yellow1]"+ out5string), title="Dig Short Answer", subtitle="mx records", padding=1, border_style ="bright_cyan"))
        full=(Panel.fit("[yellow1]"+(joined_string),title="Dig Full Info", subtitle=domain, style="white", border_style="dark_orange"))

        grid = Table.grid(expand=False)
                 
        grid2 = Table.grid(expand=True)
        grid3 = Table.grid(expand=True)
        grid4 = Table.grid(expand=True)
        grid2.add_column(justify="left")
        grid3.add_column(justify="left")
        grid2.add_row(ip)
        grid2.add_row(ns)
        grid3.add_row(full)
        grid4.add_row(txt)
        grid4.add_row(mx)
        grid.add_row(grid2,grid3,grid4)
        
        try:
            for x in TargetsDb.targets:
                if (x.domain == domain):
                    x.ipadd = out2string
                    print(grid)
                    
        except:
            print("[red3]Unable to update database.")
            print(grid)
        
            


        
    
if __name__ == "__main__":
    DigTarget().run_commands(domain)





















                       