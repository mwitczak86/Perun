#Michal Witczak
import whois
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import print
from tld import get_tld
from target import Target
from ip_target import IpTarget
from domain_target import DomainTarget


class TargetsDb:
    targets=[]
    #target submenu output
    def print_menu(self):
        print(Panel.fit("""
Targets Menu
[yellow1]D.[/yellow1] Add domain target.
[yellow1]I.[/yellow1] Add Ip address target
[yellow1]P.[/yellow1] Show targets.

[yellow1]Q.[/yellow1] Quit.




""",title="Targets Menu",border_style="bright_cyan",style="white"))
    #user input
    def target_menu(self):
        self.print_menu()
        option = ''
        while(True):
            try:
                option = str(input('Enter choice, or press [Q] to quit.: '))
            except:
                print('Wrong input. Please enter D or I ...')
            if option == "I" or option == "i":
                self.create_ip_target("ip address")
            elif option == "D" or option == "d":
                self.create_domain_target("domain")
            elif option == "P" or option == "p":
                self.print_targets()
            elif option == "Q" or option == "q":
                break
            
            else:
                print('Wrong input. Please enter D or I ...')   
    
    #DomainTarget class object creation
    def create_domain_target(self,target_type):
        name=str(input('Type the name of your target: '))
        domain=str(input('Enter domain name: '))
        target_id=(len(TargetsDb.targets)+1)
        target=DomainTarget(name, domain, target_id, target_type)
        TargetsDb().targets.append(target)
        target.print_details()
        
    #IpTarget class object creation
    def create_ip_target(self,target_type):
        name=str(input('Type the name of your target: '))
        ipadd=str(input('Enter ip address: '))
        target_id=(len(TargetsDb.targets)+1)
        target=IpTarget(name, ipadd, target_id, target_type)
        TargetsDb().targets.append(target)
        target.print_details()
        
    #object list output
    def print_targets(self):
        console = Console()
        console.clear()
        tab1 = Table(title="Targets database",title_style="yellow1", style="white")
        tab1.add_column("ID",justify="center" )
        tab1.add_column("Name",justify="center" )
        tab1.add_column("Domain",justify="center" )
        tab1.add_column("Ip Address",justify="center" )

        for target in TargetsDb.targets:
            id=str(target.id)
            name=target.name
            ip=target.ipadd
            domain=target.domain
            tab1.add_row(id,name,domain,ip)
        print(tab1)
    #return to main menu
    def mainMenu(self):
        MenuModule().run()
        

if __name__ == "__main__":
    TargetsDb().target_menu()

