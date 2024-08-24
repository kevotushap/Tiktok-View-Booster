from core import *
from core.plugins.log import *
from core.plugins.cfg import *

class UI:
    def banner():
        banner = f'''{Fore.BLUE}
                          d8, d8b                        d8b                                      
                   d8P   `8P  ?88          d8P           ?88                                      
                d888888P       88b      d888888P          88b                                     
                  ?88'    88b  888  d88'  ?88'   d8888b   888  d88'                               
                  88P     88P  888bd8P'   88P   d8P' ?88  888bd8P'                                
                  88b    d88  d88888b     88b   88b  d88 d88888b                                  
                 `?8b  d88' d88' `?88b,  `?8b  `?8888P'd88' `?88b,                               
                                                                            
           d8,                           d8b                                                      
          `8P                            ?88                                 d8P                  
                                          88b                             d888888P                
?88   d8P  88b d8888b ?88   d8P  d8P      888888b  d8888b  d8888b  .d888b,  ?88'   d8888b  88bd88b
d88  d8P'  88Pd8b_,dP d88  d8P' d8P'      88P `?8bd8P' ?88d8P' ?88 ?8b,     88P   d8b_,dP  88P'  `
?8b ,88'  d88 88b     ?8b ,88b ,88'      d88,  d8888b  d8888b  d88   `?8b   88b   88b     d88     
`?888P'  d88' `?888P' `?888P'888P'      d88'`?88P'`?8888P'`?8888P'`?888P'   `?8b  `?888P'd88'     
'''

        banner = pystyle.Center.XCenter(banner)
        print(banner)
