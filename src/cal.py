# Please make sure your code is running fine before pushing it online to github and add your code only where specified 
# Add only one feature 

def AddTwoNumbers(numb,numb1):
    print("enter your name here...")
    #add your code here to add two numbers and print the answer
    print(numb, "+", numb1, "=", (numb+numb1))
    ## Who is meant to enter their name on line 5? ##

def multiplyTwoNumbers(numb,numb1):
  print("enter your name here...")
   #add your code here to multiply two numbers and print the answer

def AddThreeNumbers(numb, numb1):
  num3 = int(input("Enter third number: "))
  print("enter your name here...")
   # add your code here to add three numbers and print the answer

def multiplyThreeNumbers(numb, numb1):
 num3 = int(input("Enter third number: "))
 print("enter your name here...")
 # add your code here to multiply three numbers here and print the answer

def isiteven(numb):
    if numb % 2 == 0:
        return True
    else:
        return False
# add your code here to check if a number is even

def main():
  try:
    ask = input("What do you want to do? (hint Enter add2, muti2, add3, muti3): ")
    num = int(input("Enter first number: "))
    num1 = int(input("Enter second number: "))

    if ask == "add2":
      AddTwoNumbers(num,num1)
    elif ask == "muti2":
      multiplyTwoNumbers(num,num1)
    elif ask == "add3":
      AddThreeNumbers(num, num1)
    elif ask == "muti3":
      multiplyThreeNumbers(num,num1)
    else:
      print("Bye Enter the correct information")
  except:
    print("Enter a whole number or the right value. Bye!")  
if __name__ == '__main__':
    main()
    
