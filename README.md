#Meet Perun, the thunder god.
For many pagan slavs, <b>Perun</b> was the most important god. He was powerful, fierce but also kind and live-giving. Just like the <b>Information Gathering</b> is the first step for every penetration test. Without information about your target, you will go nowhere.
<br>If you will get enough data, you can decide how to use it.
<br><b>Perun</b> is a python tool designed to gather information about domains and subdomains using passive recon. 
It was developed and tested for <b>ParrotOs</b>.
<br><b>Perun</b> enumerates subdomains using popular python libraries and online tools. It does nothing new, being a simple commands wrapper, it will help you receive the basic pieces of information in just a few clicks.

<h2>Dependencies:</h2>
As mentioned above <b>Perun</b> depends on several different libraries.
<li>rich (library for rich text and beautiful formatting in the terminal)</li>
<li>tld (Extract the top-level domain (TLD) from the URL given)</li>
<li>requests</li>
<li>json</li>
<li>dig </li>
<li>VirusTotal (free virus, malware, and URL online scanning service):</li>
<u><b>Private API is needed to use VirusTotal.</b></u> 
<ul>1. You must sign in to VirustTotal community, to retrieve your private API key. <br>https://www.virustotal.com/gui/my-apikey</ul>
<ul>2. Insert your API KEY into "API" field in the 'perun_config.ini' configuration file, as shown below:

</ul>

These dependencies can be installed using the requirements file:
Installation on Linux
sudo pip install -r requirements.txt
Alternatively, each module can be installed independently before using <b>Perun</b>.
Current tld supported domains can be found in filler.txt.

<h2>How does it works</h2>
<h3> Welcome screen and main menu </h3>
![Welcome screen](/Demo_images/main_menu.png)
<h3> Target database - u can specify serveral different objects to resolve with Perun </h3>
![Target submenu screen](/Demo_images/target_input.png)
![Target_details](/Demo_images/target_details.png)
![Targets-list](/Demo_images/targets_final_list.png)

<h3> Resolve IP address from DNS </h3>
![DNS_Resolver](/Demo_images/dns_resolver_result.png)

<h3> dig </h3>
 is a command-line tool that is used to perform DNS lookups. It can be used to query DNS servers for information about various DNS records, including A records (which map domain names to IP addresses), MX records (which identify mail servers for a domain), and more
![DNS_Resolver](/Demo_images/dig_result.png)

<h3> Whois response </h3>
![Whois](/Demo_images/webtarget_result.png)

<h3> VirusTotal response </h3>
Thanks to Python's 'rich' library, the output is clean and any potentially harmful elements are highlighted. 
![VT_response](/Demo_images/vt_result.png)

<h3> HELP </h3>
![Help](/Demo_images/help.png)


<br><h2><b>Installation</b></h2>
git clone https://github.com/mwitczak86/Perun
<br>sudo pip install -r requirements.txt
<br>
<h2>Recommended Python Version:</h2>
<b>Perun</b> currently supports <b>Python 3</b>.
The recommended version for Python 3 is 3.7.x
<br><br>
<h2><i>To-Do list:</i></h2>
- [ ] expand tld supported domains</li>
- [ ] add more whois query details</li>
- [ ] simple (pdf) report creator</li>
- [ ] integrate Perun with other OSINT libraries for more detailed passive recon.</li>

<h2>Author</h2>
M.Witczak

