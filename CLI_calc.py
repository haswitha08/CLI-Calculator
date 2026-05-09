
def cli_calc(f_num, opr, s_num):
    if opr=='+':
        return f_num + s_num
    
    elif opr=='-':
        return f_num - s_num
    
    elif opr=='*':
        return f_num * s_num
    
    elif opr=='/':
        return f_num / s_num
        
    elif opr=='//':
         return f_num // s_num
    
    else:
         return f_num % s_num
        

while True:
     
    while True:
        try:
            f_num = int(input("Enter the first number: "))
            break
            
        except ValueError:
             print("Enter valid number!")
    
    while True:
        opr = input("Enter the operator (+, -, *, /, %, //): ")
    
        if opr in ['+', '-', '*', '/', '%', '//']:
            break
        else:
            print("Invalid operator.Enter again!")
    
    while True:
        try:
            s_num = int(input("Enter the second number: "))
            break
        except ValueError:
             print("Enter valid number!")

    if opr in ['/', '//', '%'] and s_num == 0:
        print("Can't divide by ZERO!")
        continue

    
    result = cli_calc(f_num, opr, s_num)
    print(f" Result : {f_num} {opr} {s_num} = {result} ")
    while True:
        Choice=input("Do you want to continue?(yes/no): ")
        if Choice=='yes':
            break
        elif Choice=='no':
            print("Bye!")
            exit()
    else:
       print("INVALID OUTPUT. Choose either 'yes' or 'no'!")