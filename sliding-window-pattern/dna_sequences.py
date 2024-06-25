def find_repeated_sequences(s, k):
    
    n = len(s)

    if n < k:
        return set()

    # Mapping of characters
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Base value
    a = 4

    # Numeric representation of the sequence
    numbers = []
    for i in range(n):
        numbers.append(mapping.get(s[i]))

    # Current hash value
    hash_value = 0

    # 1. Hash set to store the unique hash values
    # 2. Output set to store the repeated substrings
    hash_set = set()
    output = set()

    for i in range(n - k + 1):
        
        # If the window is at it's initial position, calculate the hash value from scratch
        if i == 0:
            for j in range(k):
                hash_value += numbers[j] * (a ** (k - j - 1))
            
        # Otherwise, utilize the previous hash value
        else: 
            previous_hash_value = hash_value
            hash_value = ((previous_hash_value - numbers[i - 1] * (a ** (k - 1))) * a) + numbers[i + k - 1]
        
        # If the current hash value is present in the hash set, the current substring has been repeated, so we add it to the output
        if hash_value in hash_set:
            output.add(s[i : i + k])
            
        # We add the evaluated hash value to the hash set
        hash_set.add(hash_value)

    return output



def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i + 1, ".\tInput sequence:",inputs_string[i], 
                     "\n\tk:", inputs_k[i],
                     "\n\n\tRepeated sequences:", find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()