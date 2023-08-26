import wikipedia
import warnings
from unidecode import unidecode
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
    result = wikipedia.summary(wikipedia.suggest(li[option-1]))
except wikipedia.exceptions.DisambiguationError as e:
    print("Code under confusion.")
    for l,k in enumerate(e.options):
        print(l,k)
    op=int(input("Enter selection an option:"))
    result = wikipedia.summary(wikipedia.suggest(e.options[op]))
# printing the result
print(unidecode(result))