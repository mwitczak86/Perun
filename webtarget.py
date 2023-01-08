#Michal Witczak
import whois
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import print
from tld import get_tld

class WebTarget:
    #read domain names in filer2.txt and checking if user input is in a given range
    def validate_tld(self,domain):
        tld_list=[]
        with open("filer2.txt", 'r') as tlds:
            tld_list = [line.strip() for line in tlds]
                       
        tld = str("."+get_tld(domain,fix_protocol=True))
               
        if tld in tld_list:
            print("[bright_cyan]Success!!!  [white]:heavy_check_mark:")
            self.print_info(domain)
        else:
            print("\n[bold red3 blink]Sorry your address is out of the current domain scope. Try different tool.")
        
        
        
    #Whois response with 'rich' panels and tables
    def print_info(self,domain):
        console = Console()
        console.clear()
        
        try:
            
            w=(whois.query(domain).__dict__)
            w_name=w['name']
            w2=whois.query(domain)     
            cdate = w2.creation_date.date()
            edate = w2.expiration_date.date()
        
            cstr = cdate.strftime("%Y-%m-%d")
            estr = edate.strftime("%Y-%m-%d")
        
        
        
      
        
            p=Panel.fit(("Domain: [yellow1]" + w_name), padding=2, title="Target",subtitle="whois...", style="bright_cyan")

            
            tab1 = Table(title="Registrar",title_style="yellow1", style="dark_orange")
            tab2 = Table(title="Dates", title_style="yellow1", style="dark_orange")
            tab3 = Table(title="Name servers", title_style="yellow1", style="dark_orange")

            snlist = sorted(w['name_servers'])
            
            tab1.add_column("[white]Name", justify="center")
            tab1.add_row("[yellow1]"+w['registrar'])

            tab2.add_column()
            tab2.add_column("[white]Date",justify="center")
            tab2.add_row("[white]Creation date: ","[yellow1]"+cstr)
            tab2.add_row("[white]Expiration date: ","[yellow1]"+estr)
            


            tab3.add_column("[white]Id", style="white")
            tab3.add_column("[white]Name", style="yellow1", justify="left")


            for i in snlist:
                index = str(snlist.index(i)+1)
                tab3.add_row(index,i)              
            

            grid = Table.grid(expand=False)
            grid.add_column()
            grid.add_column(justify="center")
            grid.add_column()
            grid.add_row(p)
            grid.add_row()
            grid.add_row(tab1,tab2 ,tab3)



            console.print(grid)
        
           
        except:
            print("Sorry, no data available. Please verify your input or try another tool.")
        
        

    

if __name__ == "__main__":
    WebTarget().validate_tld(domain)