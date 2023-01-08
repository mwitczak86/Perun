#Michal Witczak
from rich import print
from tld import get_tld
from rich.panel import Panel
from webtarget import WebTarget
from digtarget import DigTarget
from vtsubs import VtSubs
from rich.markdown import Markdown
from rich.console import Console
from targets_db import TargetsDb
from domain_target import DomainTarget
from domain_resolver import DomainResolver

class MenuModule:

    
     #main menu output   

    def print_menu(self):
        print(Panel.fit("""

[bright_cyan]T.[/bright_cyan] Targets - database

[yellow1]1.[/yellow1] Whois - retrieve information of given domain.
[yellow1]2.[/yellow1] Dig
[yellow1]3.[/yellow1] VirusTotal - subdomain analysis
[yellow1]4.[/yellow1] Reverse DNS lookup [IP --> domain]

[green]H.[/green] Help

[red3]Q.[/red3] Quit
""",title="Menu",border_style="bright_cyan",style="white"))
    #submenu output
    def sub_menu(self):
        print("""
-------------------
[red3]Q.[/red3] Quit
[yellow1]M.[/yellow1] Main menu
""")
    #user input
    def run(self):
        self.print_menu()
        while(True):    
            option = ''
            try:
                option = input('Enter your choice: ')
            except:
                print('Wrong input. Please enter a number ...')
        #user input verification
            if option == "1":
                print()
                self.option1()
                self.sub_menu()
                optionS = ''
                while(True):
                    try:
                        optionS = str(input('Enter your choice: '))
                    except:
                        print('Wrong input. Please enter Q or M ...')
                    if optionS == "Q" or optionS == "q":
                        print("[yellow1 bold]:high_voltage:It was a pleasure, see you soon. [yellow1 bold]:high_voltage:")
                        exit()
                    elif optionS == "M" or optionS == "m":
                        self.run()
                    else:
                        print('Wrong input. Please enter Q or M ...') 
            
            
            
            
            elif option == "2":
                print()
                self.option2()
                self.sub_menu()
                optionS = ''
                while(True):
                    try:
                        optionS = str(input('Enter your choice: '))
                    except:
                        print('Wrong input. Please enter Q or M ...')
                    if optionS == "Q" or optionS == "q":
                        print("[yellow1 bold]:high_voltage:It was a pleasure, see you soon. [yellow1 bold]:high_voltage:")
                        exit()
                    elif optionS == "M" or optionS == "m":
                        self.run()
                    else:
                        print('Wrong input. Please enter Q or M ...') 
                        

            elif option == "3":
                print()
                self.option3()
                self.sub_menu()
                optionS = ''
                while(True):
                    try:
                        optionS = str(input('Enter your choice: '))
                    except:
                        print('Wrong input. Please enter Q or M ...')
                    if optionS == "Q" or optionS == "q":
                        print("[yellow1 bold]:high_voltage:It was a pleasure, see you soon. [yellow1 bold]:high_voltage:")
                        exit()
                    elif optionS == "M" or optionS == "m":
                        self.run()
                    else:
                        print('Wrong input. Please enter Q or M ...')  
            
            elif option == "T" or option == "t":
                print()
                self.optionT()
                self.sub_menu()
                optionS = ''
                while(True):
                    try:
                        optionS = str(input('Enter your choice: '))
                    except:
                        print('Wrong input. Please enter Q or M ...')
                    if optionS == "Q" or optionS == "q":
                        print("[yellow1 bold]:high_voltage:It was a pleasure, see you soon. [yellow1 bold]:high_voltage:")
                        exit()
                    elif optionS == "M" or optionS == "m":
                        self.run()
                    else:
                        print('Wrong input. Please enter Q or M ...')  

            elif option == "4":
                print()
                self.option4()
                self.sub_menu()
                optionS = ''
                while(True):
                    try:
                        optionS = str(input('Enter your choice: '))
                    except:
                        print('Wrong input. Please enter Q or M ...')
                    if optionS == "Q" or optionS == "q":
                        print("[yellow1 bold]:high_voltage:It was a pleasure, see you soon. [yellow1 bold]:high_voltage:")
                        exit()
                    elif optionS == "M" or optionS == "m":
                        self.run()
                    else:
                        print('Wrong input. Please enter Q or M ...')

            elif option == "H" or option == "h":
                print()
                self.optionH()
                self.sub_menu()
                optionS = ''
                while(True):
                    try:
                        optionS = str(input('Enter your choice: '))
                    except:
                        print('Wrong input. Please enter Q or M ...')
                    if optionS == "Q" or optionS == "q":
                        print("[yellow1 bold]:high_voltage:It was a pleasure, see you soon. [yellow1 bold]:high_voltage:")
                        exit()
                    elif optionS == "M" or optionS == "m":
                        self.run()
                    else:
                        print('Wrong input. Please enter Q or M ...')    

            elif option == "Q" or option == "q":
                print('[yellow1 bold]:high_voltage:It was a pleasure, see you soon. [yellow1 bold]:high_voltage:')
                exit()
            else:
                print('[yellow1 bold]Invalid option. Please enter a number between[bright_cyan] 1[yellow1 bold] and [bright_cyan] 3[yellow1 bold],\nor press[bright_cyan] Q[yellow1 bold] to quit.')


    #parse user choice to Whois function
    def option1(self):
        obj1 = WebTarget()
        target=''
        try:
           target=int(input("Please enter the domain component Id number: "))
        except:
           print('Wrong input.')
        try:
            for x in TargetsDb().targets:
                if x.id == target:
                    domain = x.domain
        
                
            
                
            if domain !="":
                obj1.validate_tld(domain)
            else:
                print("Please enter a valid number.")

        except:
            print('Sorry no data for this domain')
            self.run()
    #parse user choice to Dig function
    def option2(self):
        obj2 = DigTarget()
        target=''
        try:
           target=int(input("Please enter the domain component Id number: "))
        except:
           print('Wrong input.')
        try:
            for x in TargetsDb().targets:
                if x.id == target:
                    domain = x.domain
        
                
            
                
            if domain !="":
                obj2.run_commands(domain)
            else:
                print("Please enter a valid number.")

        except:
            print('Sorry no data for this domain')
            self.run()   
        
        
    #parse data to VirustTotal resolver
    def option3(self):
        obj3 = VtSubs()
        target=''
        try:
           target=int(input("Please enter the domain component Id number: "))
        except:
           print('Wrong input.')
        try:
            for x in TargetsDb().targets:
                if x.id == target:
                    domain = x.domain
        
                
            
                
            if domain !="":
                if domain[:4] == "www.":
                    valdomain = domain[4:]
                    obj3.get_vtdata(valdomain)
                    print("Data collecting in progress...")
                else:
                    valdomain = domain
                    obj3.get_vtdata(valdomain)
                    print("Data collecting in progress...")

                
            else:
                print("Please enter a valid domain.")

        except:
            print('Sorry no data for this domain')
            self.run()    
          
        

    #parse data to DomainResolver
    def option4(self):
        obj4 = DomainResolver()
        target=''
        try:
           target=int(input("Please enter the domain component Id number: "))
        except:
           print('Wrong input.')
        try:
            for x in TargetsDb().targets:
                if x.id == target:
                    domain = x.domain  

            if domain !="":
                print("Unable to update the database.")
            else:
                try:
                    obj4.domain_from_ip(target)
                except:
                    print("Error occured... Check your input.")
        except:
            print('Sorry no data for this Id')
            self.run()   

    
    #target database output
    def optionT(self):
         objT = TargetsDb()
         objT.target_menu()
    #markdown help file
    def optionH(self):
         console=Console()
         f = open("help.txt", "r")
         md=Markdown(f.read(),style="white")
         console.print(md)
        
   
    

    
    
            
if __name__ == "__main__":
    MenuModule().run()