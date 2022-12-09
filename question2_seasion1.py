class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
import math
def banner():
    print(color.FAIL + """                           
                _                                   
 _           _ ( )_                                 
(_)  ___    (_)| ,_)                                
| |/',__)   | || |                                  
| |\__, \   | || |_                                 
(_)(____/   (_)`\__)                                
 _____                              _           _   
(_   _)     _                      (_ )       /'_`\ 
  | | _ __ (_)   _ _   ___     __   | |    __(_) ) |
  | |( '__)| | /'_` )/' _ `\ /'_ `\ | |  /'__`\ /'/'
  | || |   | |( (_| || ( ) |( (_) | | | (  ___/|_|  
  (_)(_)   (_)`\__,_)(_) (_)`\__  |(___)`\____)(_)  
                            ( )_) |                 
                             \___/'                     

written by : soroush yasini
                                                      
""")
banner()
def triangle():
    a = int(input(color.OKCYAN + "please input the no.1 : "))
    b = int(input(color.OKCYAN + "please input the no.2 : "))
    c = int(input(color.OKCYAN + "please input the no.3 : "))
    if a + b > c and a + c > b and b + c > a :
        print(color.OKBLUE + " congrats! it is a triangle !")
    else :
        print(color.WARNING + " unfortunately it is NOT a Triangle !")
triangle()