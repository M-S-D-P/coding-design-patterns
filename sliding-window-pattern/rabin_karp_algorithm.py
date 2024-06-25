# Notes:

# Let's assume the original string is 𝑇
# and its length is 𝑛. On the other hand, the string to be searched is
# 𝑃, and its length is 𝑚.

# Spurious hits occur in the searching process. These occur when the hash value of the search pattern is matched with the hash value of the text window, but the window is not the actual pattern.

# Let's see the following example to understand the working of the algorithm.

# T: 3 1 4 1 5 9 2 6 5 3
# length of T(n): 11
# P: 2 6 (pattern to find)
# mod calculation 26 % 11 = 4
# we look for the hits that give us mod 4 for this key only.

number_of_characters = 256

def search(search_string, original_text, q):
	n = len(search_string)
	m = len(original_text)
	i = 0 # index
	j = 0 # index
	p = 0 # hash key for search_string
	t = 0 # hash key for original_text
	h = 1

	# h would be assigned "pow(number_of_characters, n-1)%q"
	for i in range(n-1):
		h = (h*number_of_characters)%q

	# calculate the hash value of search_string and first occurence of text
	for i in range(n):
		p = (number_of_characters*p + ord(search_string[i]))%q
		t = (number_of_characters*t + ord(original_text[i]))%q

	# slide over the search_string character by character
	for i in range(m-n+1):
		# we check the hash values for the current window of original_text and search_string. 
		# if the hash value matches then we check for characters one by one
		if p==t:
			for j in range(n):
				if original_text[i+j] != search_string[j]:
					break
				else: j+=1

			# if p == t and search_string[0...n-1] = original_text[i, i+1, ...i+n-1]
			if j==n:
				print ("search_string found at slide " + str(i))

		# we calculate the hash value for the next window of text: Remove
		# leading digit, add trailing digit
		if i < m-n:
			t = (number_of_characters*(t-ord(original_text[i])*h) + ord(original_text[i+n]))%q

			# if we encounter negative values of t, we convert it to positive
			if t < 0:
				t = t+q

# main
original_text = "31415926535"
search_string = "41"

# prime number
q = 101
search(search_string,original_text,q)
