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
       (_)                  [  |                      
 .--.  __  _ .--..--. _ .--. | |.---.                 
( (`\][  |[ `.-. .-. [ '/'`\ | / /__\\                
 `'.'. | | | | | | | || \__/ | | \__.,         
[\__) [___[___||__||__| ;.__[___'.__.'                
             __      [__|           _                 
            [  |                   / |_               
 .---. ,--.  | |__   _  .---. ,--.`| |-'.--.  _ .--.  
/ /'`\`'_\ : | [  | | |/ /'`\`'_\ :| |/ .'`\ [ `/'`\] 
| \__.// | |,| || \_/ || \__.// | || || \__. || |     
'.___.\'-;__[___'.__.'_'.___.\'-;__\__/'.__.'[___]    

written by : soroush yasini
                                                      
""")
banner()
def oprators():
    global opr
    opr = input(color.OKCYAN + """ which math opration you want to do ?
    choose one from below and type it .

        radical     sin     cos     tan     cot     factorial 

            +   -   /   *   ** 
            
        whtich ? : """)
oprators()
print(opr)
def calc():
    if opr == "sin" :
     ang = float(input("input the angle : "))
     print( " the sinus of angle is : ", round((math.sin(math.radians(ang))),3))
    if opr == "cos" :
     ang = float(input("input the angle : "))
     print( " the cosinus of angle is : ", round((math.cos(math.radians(ang))),3))
    if opr == "tan" :
     ang = float(input("input the angle : "))
     print( " the tangant of angle is : ", round((math.tan(math.radians(ang))),3))
    if opr == "cot" :
     ang = float(input("input the angle : "))
     print( " the cot of angle is : ", round((math.sin(math.radians(ang))),3))
    if opr == "factorial" :
        num = int(input("input the mumber : "))
        print("factorial of the number is : ", math.factorial(num))
    if opr == "radical" :
        num = float(input("input the number : "))
        print("radical of the number is : ", num**(1/2))
    if opr == "/" :
        a = float(input("insert the no.1 : "))
        b = float(input("insert the no.2 : "))
        if b == 0 :
            print("numbers can't be divided to zero !!!")
        c = a / b
        print("here is the anwser : ", c )
    if opr == "+" :
        a = float(input("insert the no.1 : "))
        b = float(input("insert the no.2 : "))
        c = a + b
        print("here is the anwser : ", c )
    if opr == "-" :
        a = float(input("insert the no.1 : "))
        b = float(input("insert the no.2 : "))
        c = a - b
        print("here is the anwser : ", c )
    if opr == "*" :
        a = float(input("insert the no.1 : "))
        b = float(input("insert the no.2 : "))
        c = a + b
        print("here is the anwser : ", c )
    if opr == "**" :
        a = float(input("insert the no.1 : "))
        b = float(input("insert the no.2 : "))
        c = a ** b
        print("here is the anwser : ", c )   
calc()
     


