def count_digit(number,digit):
	count=0
	while number > 0:
		if number % 10==digit:
			count+=1
		number //=10
	return count
def main():
	max_occurs=0
	most_frequent_digit=-1
	input1=int(input("Enter the first number : "))
	input2=int(input("Enter the second number : "))
	input3=int(input("Enter the third number : "))
	input4=int(input("Enter the fourth number : "))
	for digit in range(10):
		current_count=(
			count_digit(input1,digit)+
			count_digit(input2,digit)+
			count_digit(input3,digit)+
			count_digit(input4,digit)
			)
		if current_count > max_occurs:
			max_occurs=current_count
			most_frequent_digit=digit
	print("The most frequent digit is : ",most_frequent_digit)
	
if __name__=="__main__":
	main()
