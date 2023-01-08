#Michal Witczak
import requests, json
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from configparser import ConfigParser


#PHISING EXAMPLE: 
#domain = '02sms.xyz'
class VtSubs:
    #VirusTotal API request and response
    
    def get_vtdata(self, domain):
        config_obj = ConfigParser()
        config_obj.read("perun_config.ini")
        user_info = config_obj["USERINFO"]
        vt_api = user_info["vt_api"]
        if (domain == ""):
            print("Sorry, no data avaible... check your input, and try again.")
        else:

            url_subdomain = ("https://www.virustotal.com/api/v3/domains/"+domain+"/subdomains?limit=40")
            url_domain = ("https://www.virustotal.com/api/v3/domains/"+domain)

            headers = {

                "Accept": "application/json",

                "x-apikey": vt_api,
                

            }

            response_d = requests.get(url_domain,headers=headers)
            response_s = requests.get(url_subdomain, headers=headers)
        
            try:
                resp = response_s.json()
                

                    
                data = resp['data']
                data_d = response_d.json()

                

                p=Panel.fit(("Domain: [yellow1]" + domain), padding=2, title="Target",subtitle="domain", style="bright_cyan")

                tab1 = Table(title="Subdomains and Blacklists analysis", style='bright_cyan')
                #alien,google,eset,gdata,fortinet,zerocert,avira,kaspersky,netcraft
                tab1.add_column("Domain/subdomain", justify="left")
                tab1.add_column("AlienVault", justify="center")
                tab1.add_column("Google", justify="center")
                tab1.add_column("ESET", justify="center")
                tab1.add_column("G-Data", justify="center")
                tab1.add_column("Fortinet", justify="center")
                tab1.add_column("ZeroCert", justify="center")
                tab1.add_column("Avira", justify="center")
                tab1.add_column("Kaspersky", justify="center")
                tab1.add_column("Netcraft", justify="center")

                self.raw_to_list(domain,tab1,data,data_d,p)
            except:
                print("Sorry no data avaible... check your input, and try again.")
       

    #json to dict
    def raw_to_list(self,domain,tab1,data,data_d,p):
        
        slist = []
        ddict = data_d['data']
        ddatr = ddict['attributes']

        for i in data:
            slist.append(i)
        

        
        self.table_filler_d(p,domain,ddict,ddatr,slist,tab1)
        

    #'rich' table output with vendors response
    def table_filler_d(self,p,domain,ddict,ddatr,slist,tab1):
        
        dom = ddict['id']
        
        alien=str((ddatr['last_analysis_results']['AlienVault'])['result'])
        google=str((ddatr['last_analysis_results']['Google Safebrowsing'])['result'])
        eset=str((ddatr['last_analysis_results']['ESET'])['result'])
        gdata=str((ddatr['last_analysis_results']['G-Data'])['result'])
        fortinet=str((ddatr['last_analysis_results']['Fortinet'])['result'])
        zerocert=str((ddatr['last_analysis_results']['ZeroCERT'])['result'])
        avira=str((ddatr['last_analysis_results']['Avira'])['result'])
        kaspersky=str((ddatr['last_analysis_results']['Kaspersky'])['result'])
        netcraft=str((ddatr['last_analysis_results']['Netcraft'])['result'])

        result_list_d = []
        result_list_d.extend([alien,google,eset,gdata,fortinet,zerocert,avira,kaspersky,netcraft])
        

        row_list_d = []
        for i in result_list_d:
            if i =='clean':
                i=("[green1]"+i+" :heavy_check_mark:")
                row_list_d.append(i)
            elif i =='unrated':
                i=("[white]"+i)
                row_list_d.append(i)
            else:
                i=("[bold red3 blink]:warning-emoji: "+i)
                row_list_d.append(i)
        

        tab1.add_row("[bright_cyan]"+dom,row_list_d[0],row_list_d[1],row_list_d[2],row_list_d[3],row_list_d[4],row_list_d[5],row_list_d[6],row_list_d[7],row_list_d[8])


        self.table_filler_s(p,domain,slist,tab1)

    #subdomains column details
    def table_filler_s(self,p,domain,slist,tab1):
       

        for x in slist:
            atr = {}
            atr = x['attributes']
            
            subd=(x['id'])
            
            alien=str((atr['last_analysis_results']['AlienVault'])['result'])
            google=str((atr['last_analysis_results']['Google Safebrowsing'])['result'])
            eset=str((atr['last_analysis_results']['ESET'])['result'])
            gdata=str((atr['last_analysis_results']['G-Data'])['result'])
            fortinet=str((atr['last_analysis_results']['Fortinet'])['result'])
            zerocert=str((atr['last_analysis_results']['ZeroCERT'])['result'])
            avira=str((atr['last_analysis_results']['Avira'])['result'])
            kaspersky=str((atr['last_analysis_results']['Kaspersky'])['result'])
            netcraft=str((atr['last_analysis_results']['Netcraft'])['result'])
            
            result_list = []
            result_list.extend([alien,google,eset,gdata,fortinet,zerocert,avira,kaspersky,netcraft])
            
            row_list = []
            for i in result_list:
                if i =='clean':
                    i=("[green1]"+i+" :heavy_check_mark:")
                    row_list.append(i)
                elif i =='unrated':
                    i=("[white]"+i)
                    row_list.append(i)
                else:
                    i=("[bold red3 blink]:warning-emoji: "+i)
                    row_list.append(i)
            

            tab1.add_row("[yellow1]"+subd,row_list[0],row_list[1],row_list[2],row_list[3],row_list[4],row_list[5],row_list[6],row_list[7],row_list[8])
            
        self.print_tables(p,tab1)
    
    #'rich' table output
    def print_tables(self,p,tab1):
        grid = Table.grid(expand=True)
        grid.add_row(tab1)
        print(p)
        print()
        print(grid)


if __name__ == "__main__":
    
    VtSubs().get_vtdata("")








    
    
   
