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
    print(color.BOLD + """                           
            _                       _                            _   
           ( )                     ( )_  _                      (_ ) 
   __     _| | _   _    ___    _ _ | ,_)(_)   _     ___     _ _  | | 
 /'__`\ /'_` |( ) ( ) /'___) /'_` )| |  | | /'_`\ /' _ `\ /'_` ) | | 
(  ___/( (_| || (_) |( (___ ( (_| || |_ | |( (_) )| ( ) |( (_| | | | 
`\____)`\__,_)`\___/'`\____)`\__,_)`\__)(_)`\___/'(_) (_)`\__,_)(___)
          _                  _                                       
       _ ( )_               ( )_  _                                  
  ___ (_)| ,_) _   _    _ _ | ,_)(_)   _     ___                     
/',__)| || |  ( ) ( ) /'_` )| |  | | /'_`\ /' _ `\                   
\__, \| || |_ | (_) |( (_| || |_ | |( (_) )| ( ) |                   
(____/(_)`\__)`\___/'`\__,_)`\__)(_)`\___/'(_) (_)                   
                                                        
written by : soroush yasini
                                                      
""")
banner()
def average():
    name = input("what is the name of the sutdent ? : ")
    family = input("what is the family name of her?him ? : ")
    grade1 = int(input("please insert her/his first grade number  : "))
    grade2 = int(input("please insert her/his second grade number  : "))
    grade3 = int(input("please insert her/his third grade number  : "))
    aver = (grade1 + grade2 + grade3) / 3
    if aver > 20 :
        print(color.WARNING + "are you sure you entered righ numbers?")

    if aver >= 17 and aver <= 20 :
            print(color.OKGREEN + """
            THE STUDENT IS 
    _____                        _       _ 
  / ____|                       | |     | |
 | |  __   _ __    ___    __ _  | |_    | |
 | | |_ | | '__|  / _ \  / _` | | __|   | |
 | |__| | | |    |  __/ | (_| | | |_    |_|
  \_____| |_|     \___|  \__,_|  \__|   (_)
                                           
                                           

        """)
    if aver < 17 and aver >= 12 :
            print(color.FAIL + """
                  THE STUDENT IS                                                   
     /\                                                 
    /  \    __   __   ___   _ __    __ _    __ _    ___ 
   / /\ \   \ \ / /  / _ \ | '__|  / _` |  / _` |  / _ \
  / ____ \   \ V /  |  __/ | |    | (_| | | (_| | |  __/
 /_/    \_\   \_/    \___| |_|     \__,_|  \__, |  \___|
                                            __/ |       
                                           |___/        
            """)
    if aver < 12 :
            print(color.FAIL + """

            THE STUDENT IS 
  ______           _   _     _   _   _ 
 |  ____|         (_) | |   | | | | | |
 | |__      __ _   _  | |   | | | | | |
 |  __|    / _` | | | | |   | | | | | |
 | |      | (_| | | | | |   |_| |_| |_|
 |_|       \__,_| |_| |_|   (_) (_) (_)
                                       
                                             
            """)

average()