#!/usr/bin/python3
#Michal Witczak
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import print
from rich.markdown import Markdown
from menu import MenuModule

#Welcome screen and main menu
class PerunIntro:
  def print_logo():

    console = Console()
    console.set_window_title("Perun - AutoRecon Tool")
    console.clear()
    WELCOME = """
# **Welcome to Perun AutoRecon tool.**
## *Created by M.Witczak*
### 2022
    """



    logo = """

      ▄███████▄    ▄████████    ▄████████ ███    █▄  ███▄▄▄▄   
      ███    ███   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄ 
      ███    ███   ███    █▀    ███    ███ ███    ███ ███   ███ 
      ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███ ███   ███ 
    ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███ ███   ███ 
      ███          ███    █▄  ▀███████████ ███    ███ ███   ███ 
      ███          ███    ███   ███    ███ ███    ███ ███   ███ 
    ▄████▀        ██████████   ███    ███ ████████▀   ▀█   █▀  
                                ███    ███                      
                                              passive autorecon tool.
    """

    wl = Markdown(WELCOME)

    console.print(wl, style="white", justify="center")
    console.print(logo, style="bright_cyan", justify="center")
    MenuModule().run()


    
  
  
if __name__ == "__main__":
  PerunIntro.print_logo()
  

