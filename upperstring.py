"""a=input("enter the string :").split()
if(len(a)<2):
	print("invalid string")
else:
      for i in range(len(a)):
       if(i==1):
         print(a[i].upper())
       else:
           print(a[i],end=" ")"""
a = input("Enter the string: ").split()
if len(a) < 2:
    print("invalid string")
else:
    # Convert second word to uppercase
    a[1] = a[1].upper()
    # Join all words with space and print
    print(" ".join(a))
    
           
           
"""a = input("Enter the string: ").split()
if len(a) < 2:
    	print("invalid string")
else:
    for i in range(len(a)):
        if i == 1:
            print(a[i].upper(),end=''  '')  # Print second word in uppercase on its own line
        else:
            print(a[i], end=" ")  # Print other words on the same line with spaces

    print()  # Add newline at the end"""
"""a = input("Enter the string: ").split()

if len(a) < 2:
    print("invalid string")
else:
    for i in range(len(a)):
        if i == 1:
            print(a[i].upper(), end=" ")
        else:
            print(a[i], end=" ")
    print()  # newline after all words

           
           """
