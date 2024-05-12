def find_sum_of_three(nums, target):
  nums.sort()
  n = len(nums)
  for i in range(0, n-2):
    left = i + 1
    right = n - 1
    while left < right:
      triplet = nums[i] + nums[left] + nums[right]
      if triplet == target:
        return True
      elif triplet < target:
        left +=1
      else:
        right -=1
  return False


# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()




# Time complexity
# Sorting Array: O(nlog(n))
# Nested loop: O(n2)
# Therefore, the total time complexity of this solution is O(nlog(n)+n2) -> O(n2)

# Space Complexity
# Since sort function is used, the complexity is O(n)
# it typically ranges from O(log(n)) to O(n)