
import colorama as cama
cama.init(convert=True)

while True:    
    
    print(cama.Fore.BLUE + "\nоперация: " + cama.Style.RESET_ALL, end="")    
    operation = input()
    

    if operation == "end":
        break



    try:        
        print(cama.Fore.BLUE + "первое число: " + cama.Style.RESET_ALL, end="")
        num1 = float( input() )
        
    except:
        print(cama.Fore.RED + "не удалось привести первый операнд к числовому виду")
        continue
        

    if not operation.startswith("унарный"):
        try:
            print(cama.Fore.BLUE + "второе число: " + cama.Style.RESET_ALL, end="")
            num2 = float( input() )
            
        except:
            print(cama.Fore.RED + "не удалось привести второй операнд к числовому виду")
            continue
    


    print(cama.Style.RESET_ALL + "результат:" + cama.Fore.GREEN, end=" ")


    if operation == "унарный +":
        print(+num1)

    elif operation == "унарный -":
        print(-num1)

    elif operation == "+":
        print(num1 + num2)

    elif operation == "-":
        print(num1 - num2)

    elif operation == "*":
        print(num1 - num2)

    elif operation == "/":
        print(num1 - num2)

    else:
        print(cama.Fore.RED + "неизвестная операция")


print(cama.Fore.CYAN + "\nпрограмма прекратила выполнение")
input()
