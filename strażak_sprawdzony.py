
import time
import copy
from colorama import init, Fore 
init(autoreset=True)

time.sleep ( 1 )
name = input(Fore.YELLOW + str("Cześć, jak masz na imię?: "))
while name == "":
    name = input(Fore.YELLOW + str("No nie wstydź się, podaj swoje imię... "))
    
print(Fore.BLUE + str("\nŚwietnie, ja jestem Bieniek, to teraz zagramy w strażaka.\n"))
time.sleep ( 1 )
print(Fore.BLUE + str("Ja będę Cię pytał, czego potrzebuje Twój strażak,\n"))
time.sleep ( 1 )
print(Fore.BLUE + str("a Ty odpowiadaj tak długo, aż będziesz umieć zawsze poprawnie odpowiedzieć.\n"))

decision = input(Fore.GREEN + str("Czy chcesz grać dalej?: 't' lub 'n'" ))
while decision == "":
    decision = input(Fore.GREEN + str("Musisz odpowiedzieć, czy chcesz grać dalej?: 't' lub 'n'" ))

while decision != "n":
    time.sleep ( 1 )
    answer = input(Fore.YELLOW + str("Czego potrzebuje Twój strażak?: "))
    while answer == "":
        answer = input(Fore.YELLOW + str("Czego potrzebuje Twój strażak? (musisz coś wpisać): "))
    if  answer[0] == name[0]:
        time.sleep ( 1 )
        print(Fore.BLUE + str("Tak, tego potrzebuje Twoj strazak."))
    elif answer[0] != name[0]:
        time.sleep ( 1 )
        print(Fore.BLUE + str("Nie, Twoj strazak tego nie potrzebuje..."))
    time.sleep ( 1 )
    decision = input(Fore.GREEN + str("Czy chcesz grać dalej?:" ))
    while decision == "":
        decision = input(Fore.GREEN + str("Musisz odpowiedzieć, czy chcesz grać dalej?: 't' lub 'n'" ))
else:
    time.sleep ( 1 )
    print(Fore.BLUE + str("Dziękuję, zatem kończymy na dziś."))
    
      

    