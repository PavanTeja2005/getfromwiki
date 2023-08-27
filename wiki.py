import subprocess
import sys
import os
def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        subprocess.check_call([sys.executable, "-m", "pip3", "install", package])
try:
    import wikipedia
except ModuleNotFoundError:
    install("wikipedia")
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            pass
    try:
        import wikipedia
    except:
        print("Req. module not installed aborting....")
        quit(0)
import warnings
un=0
try:
    import unidecode
    un=1
except ModuleNotFoundError:
    install("unidecode")
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            pass
    try:
        import unindecode
        un=1
    except:
        pass

warnings.filterwarnings('ignore')
title="""
  ____      _   _____                 __        ___ _    _ 
 / ___| ___| |_|  ___| __ ___  _ __ __\ \      / (_) | _(_)
| |  _ / _ \ __| |_ | '__/ _ \| '_ ` _ \ \ /\ / /| | |/ / |
| |_| |  __/ |_|  _|| | | (_) | | | | | \ V  V / | |   <| |
 \____|\___|\__|_|  |_|  \___/|_| |_| |_|\_/\_/  |_|_|\_\_|

"""
print(title)
query=input("Enter to search wiki:")
li=wikipedia.search(query)
for i,j in enumerate(li): print(i+1,j)
option=int(input("Select on option:"))
while( not (option <= len(li) and option > 0) ):
    option=int(input("Please enter a valid option:"))
try:
    result = wikipedia.summary(li[option-1])
except wikipedia.exceptions.DisambiguationError as e:
    print("Code under confusion.")
    for l,k in enumerate(e.options):
        print(l,k)
    op=int(input("Enter selection an option:"))
    result = wikipedia.summary(e.options[op])
# printing the result
if(un):
    print(unidecode.unidecode(result))
else:
    print(str(result.encode("utf-8"))[2:-1])
file=input("Enter file name to save summary or type quit to quit:")
if(file!="quit" and bool(file)==True):
    open(file,"a").write(unidecode.unidecode(result))
    print("File saved!")
elif(file==""):
    print("File name shouldn't be empty! Aborting...")
elif(file=="quit"):
    quit()
else:
    os.execv(sys.argv[0], sys.argv)
    pass
