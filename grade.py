percent = int(input("Enter your Percentage: "))
if(percent in range(91,100)):
    print("Your Grade is Ex")
elif(percent in range(81,90)):
    print("Your Grade is A")
elif(percent in range(71,80)):
    print("Your Grade is B")
elif(percent in range(61,70)):
    print("Your Grade is C")
elif(percent in range(51,60)):
    print("Your Grade is D")
else:
    print("Improve! Your marks are low")