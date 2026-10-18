num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num=input("Enter function(+-*/):")

def calc(num1,num2):
    if num=="+":
       print("Addition:",num1+num2)
    
    elif num=="-":
       print("Substraction:",num1-num2)
    
    elif num=="*":
       print("Multiplication:",num1*num2)
    
    elif num=="/":
       print("Division:",num1/num2)
     
calc(num1,num2)