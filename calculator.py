
while True:    
    
    print()
    
    
    operation = input("операция: ")
    

    if operation == "end":
        break



    try:
        num1 = float( input("первое число: ") )
        
    except:
        print("не удалось привести первый операнд к числовому виду")
        continue
        

    if not operation.startswith("унарный"):
        try:
            num2 = float( input("второе число: ") )
            
        except:
            print("не удалось привести первый операнд к числовому виду")
            continue
    


    print("результат:", end=" ")


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
        print("неизвестная операция")


print("\nпрограмма прекратила выполнение")
input()
