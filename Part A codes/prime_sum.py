def is_prime(number):
    factors = [candidate_factor for candidate_factor in range(1, number+1) if number % candidate_factor == 0]
    return len(factors) == 2

def sum_prime(n):
	prime_list = [number for number in range(2,n) if is_prime(number)]
	prime_sum = sum(prime_list)
	return prime_sum



def main():
	n=int(raw_input("enter the number upto which you need to calculate the sum of prime numbers: "))
	print sum_prime(n)


if(__name__ == "__main__"):
	main()


