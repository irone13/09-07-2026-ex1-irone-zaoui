number = int(input("Enter a number : "))
if number >= 10 and number <= 99 :
    tens = number // 10
    ones = number % 10
    if tens == ones :
        print("tens equal ones")
    else :
        print("tens not equal ones")
else :
    print ("The number should be between 10 - 99")
    
