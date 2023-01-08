# Meet Perun, the thunder god.
For many pagan slavs, <b>Perun</b> was the most important god. He was powerful, fierce but also kind and live-giving. Just like the <b>Information Gathering</b> is the first step for every penetration test. Without information about your target, you will go nowhere.
<br>If you will get enough data, you can decide how to use it.
<br><b>Perun</b> is a python tool designed to gather information about domains and subdomains using passive recon. 
It was developed and tested for <b>ParrotOs</b>.
<br><b>Perun</b> enumerates subdomains using popular python libraries and online tools. It does nothing new, being a simple commands wrapper, it will help you receive the basic pieces of information in just a few clicks.

## Dependencies:
As mentioned above <b>Perun</b> depends on several different libraries.
- rich (library for rich text and beautiful formatting in the terminal)
- tld (Extract the top-level domain (TLD) from the URL given)
- requests
- json
- dig
- VirusTotal (free virus, malware, and URL online scanning service):
### <b>Private API is needed to use VirusTotal.</b>
1. You must sign in to VirustTotal community, to retrieve your private API key. <br>https://www.virustotal.com/gui/my-apikey</ul>
2. Insert your API KEY into "API" field in the 'perun_config.ini' configuration file, as shown below:



These dependencies can be installed using the requirements file:
Installation on Linux
sudo pip install -r requirements.txt
Alternatively, each module can be installed independently before using <b>Perun</b>.
Current tld supported domains can be found in filler.txt.

## How does it works
### Welcome screen and main menu 
![Welcome screen](/Demo_images/main_menu.png)
### Target database - u can specify serveral different objects to resolve with Perun
![Target submenu screen](/Demo_images/target_input.png)
![Target_details](/Demo_images/target_details.png)
![Targets-list](/Demo_images/targets_final_list.png)

### Resolve IP address from DNS
![DNS_Resolver](/Demo_images/dns_resolver_result.png)

### dig 
 is a command-line tool that is used to perform DNS lookups. It can be used to query DNS servers for information about various DNS records, including A records (which map domain names to IP addresses), MX records (which identify mail servers for a domain), and more
![DNS_Resolver](/Demo_images/dig_result.png)

### Whois response 
![Whois](/Demo_images/webtarget_result.png)

### VirusTotal response 
Thanks to Python's 'rich' library, the output is clean and any potentially harmful elements are highlighted. 
![VT_response](/Demo_images/vt_result.png)

### Help 
![Help](/Demo_images/help.png)


##<br><b>Installation</b>
git clone https://github.com/mwitczak86/Perun
```
sudo pip install -r requirements.txt
```

## Recommended Python Version
<b>Perun</b> currently supports <b>Python 3</b>.
The recommended version for Python 3 is 3.7.x
<br><br>
## <i>To-Do list:</i>
- [ ] expand tld supported domains</li>
- [ ] add more whois query details</li>
- [ ] simple (pdf) report creator</li>
- [ ] integrate Perun with other OSINT libraries for more detailed passive recon.</li>

## Author
M.Witczak
