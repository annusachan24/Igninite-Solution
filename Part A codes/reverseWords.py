def main():
	original_string=raw_input()
	words=original_string.split(' ')
	res=""
	for word in words:
		temp_string=""
		rev_temp=""
		flag=0
		for i in range(0,len(word)):
			if word[i].isalpha() or word[i].isdigit() or word[i]=='-':
				temp_string+=word[i]
			else:
				flag=1
				rev_temp=temp_string[::-1]
				res+=rev_temp+word[i]
				if i+1>=len(word):
					res+=' '
				temp_string=""
			#print "1, ", rev_temp
			#print "2, ", temp_string
		if flag==0:
			res+=temp_string[::-1]+' '
		if temp_string!="" and flag==1:
			res+=temp_string[::-1]
		
	print res


if __name__=="__main__":
	main()
