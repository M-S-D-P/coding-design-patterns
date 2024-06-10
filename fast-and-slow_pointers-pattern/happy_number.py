def calculate_next_num(num):
    # Initialize sum to 0
    sum = 0
    
    # Loop until there are no more digits in the number
    while num > 0:
        # Get the last digit of the number
        digit = num % 10  # For example, if num is 19, digit will be 9 (1st iteration)
        
        # Add the square of the digit to the sum
        sum += digit * digit  # In the 1st iteration, sum will be 0 + 9*9 = 81
        
        # Remove the last digit from the number
        num //= 10  # For example, if num is 19, num will become 1 (1st iteration)
    
    # Return the calculated sum of squares of digits
    return sum

def is_happy_number(num):
    # Initialize slow and fast pointers to the initial number
    slow = num
    fast = num

    # Loop to find if the number is happy or enters a cycle
    while True:
        # Move slow pointer one step ahead
        slow = calculate_next_num(slow)  # For example, for num=19, slow will be 81 (1st iteration)
        
        # Move fast pointer two steps ahead
        fast = calculate_next_num(calculate_next_num(fast))  # For example, for num=19, fast will be 1 (after 2 steps)
        
        # If fast pointer reaches 1, the number is a happy number
        if fast == 1:
            return True
        
        # If slow and fast pointers meet, a cycle is detected
        if slow == fast:
            return False

# Test the function with the number 19
num = 19
print(is_happy_number(num))  # Output should be True, as 19 is a happy number
