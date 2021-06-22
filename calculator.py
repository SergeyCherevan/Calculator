
import colorama as cama
cama.init(convert=True)

while True:    
    
    print(cama.Fore.BLUE)
    
    
    operation = input("операция: ")
    

    if operation == "end":
        break



    try:
        num1 = float( input("первое число: ") )
        
    except:
        print(cama.Fore.RED + "не удалось привести первый операнд к числовому виду")
        continue
        

    if not operation.startswith("унарный"):
        try:
            num2 = float( input("второе число: ") )
            
        except:
            print(cama.Fore.RED + "не удалось привести второй операнд к числовому виду")
            continue
    


    print(cama.Fore.BLACK + "результат:" + cama.Fore.GREEN, end=" ")


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
