#Michal Witczak
from target import Target
import subprocess
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import print
import datetime

class IpTarget(Target): 
    
    
    #creating IPTarget object (Target class)    
    def __init__(self, name,ipadd,*args,**kwargs):
        self.name = name
        self.domain =""
        self.ipadd = ipadd
        self.datetime=datetime.datetime.now()
        super().__init__(*args, **kwargs)
    
    #IPTarget details output
    def print_details(self):
        console = Console()
        console.clear()
        tab1 = Table(title="Target details",title_style="yellow1", style="white")
        tab1.add_column("ID",justify="center" )
        tab1.add_column("Name",justify="center" )
        tab1.add_column("Domain",justify="center" )
        tab1.add_column("Ip Address",justify="center" )
        tab1.add_column("Target type",justify="center" )
        tab1.add_column("Creation date/time",justify="right")
        tab1.add_row("[yellow1]"+str(self.id),self.name,self.domain,self.ipadd,self.target_type,str(self.datetime))
        print(tab1)
    
    
    
    

