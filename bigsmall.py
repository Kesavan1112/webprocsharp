def extract_digits(num1,num2,num3,num4):
     max_digit1=max(int(digit) for digit in str(num1) if digit.isdigit())
     max_digit2=max(int(digit) for digit in str(num2) if digit.isdigit())
     min_digit1=min(int(digit) for digit in str(num3) if digit.isdigit())
     min_digit2=min(int(digit) for digit in str(num4) if digit.isdigit())
     return max_digit1,max_digit2,min_digit1,min_digit2
def main():
     input1=input("Enter the first number : ")
     input2=input("Enter the second number : ")
     input3=input("Enter the third number : ")
     input4=input("Enter the fourth number : ")
     
     max_digit1,max_digit2,min_digit1,min_digit2=extract_digits(input1,input2,input3,input4)
     
     result=max_digit1 + max_digit2 + min_digit1 + min_digit2
     
     print(f"Sum of biggest digits from first two inputs and smallest digits from last two inputs: ",result)
if __name__ =="__main__":
     main()
