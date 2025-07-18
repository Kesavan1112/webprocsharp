user_input=int(input("Enter the number : "))
odd_number=0
even_number=0
while user_input > 0 :
	last_digit=user_input % 10
	if last_digit % 2==1:
		odd_number=odd_number + last_digit
	else:
		even_number=even_number + last_digit
	user_input=user_input // 10
print("Sum of odd numbers in given number : ",odd_number)
print("Sum of even numbers in given number : ",even_number)
