def cal_fib_even_sum():
	fib1 = 1
	fib2 = 2
	term_value = 2
	while term_value < 4000000:
	 fib1 = fib1 + fib2
	 if fib1 % 2 == 0:
	  term_value= term_value+ fib1
	 fib2 = fib1 + fib2
	 if fib2 % 2 == 0:
	  term_value= term_value+ fib2
	return term_value


if(__name__ == "__main__"):
	ans=cal_fib_even_sum()
	print ans
