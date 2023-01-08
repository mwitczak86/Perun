#Michal Witczak
from target import Target
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import print
import datetime


class DomainTarget(Target):    
    #tworzenie obiektu DomianTarget klasy Target wraz z dziedziczeniem    
    def __init__(self, name,domain,*args,**kwargs):
        self.name = name
        self.domain =domain
        self.ipadd = ""
        self.datetime = datetime.datetime.now()
        super().__init__(*args, **kwargs)
    
    #wyswietlanie szczegolow obiektu
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
    
    
        

