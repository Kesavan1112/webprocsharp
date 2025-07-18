def solve_input(number):
	number_str=str(number)
	digits=[int(digits) for digits in number_str]
	sum1=sum(digits)
	sum2=sum(digits[1:])
	sum3=digits[-1]
	result=sum1+sum2+sum3
	return result
number=865
output=solve_input(number)
print(f"Output : {output}")
