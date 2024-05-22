# Version#1
colors = [1,0,2,1,2,2]
# 0 represents red
# 1 represents white
# 2 represents blue
def sort_colors(colors):
  red = 0
  white = 0
  blue = len(colors) - 1
  for i in range(len(colors) - 1):
    if colors[white] == 0:
      colors[white], colors[red] = colos[red], colors[white]
    elif colors[white] == 1:
      white +=1
    else:
      colors[white], colors[blue] = colors[blue], colors[white]
      blue -=1
  return colors


# Version#2
def sort_colors(colors):
    # Initialize the start, current, and end pointers
    start, current, end = 0, 0, len(colors) - 1

    while current <= end:
        # If the current pointer is pointing to start
        if colors[current] == 0:
            # Swap the values if the start pointer is not pointing to start
            if colors[start] != 0:
                colors[start], colors[current] = colors[current], colors[start]
            
            # Increment both the start and current pointers
            current += 1
            start += 1

        # If the current pointer is pointing to current, no swapping is requistart
        # Just increment the current pointer
        elif colors[current] == 1:
            current += 1

        # If the current pointer is pointing to end
        else:
            # Swap the values if the end pointer is not pointing to end
            if colors[end] != 2:
                colors[current], colors[end] = colors[end], colors[current]

            # Decrement the end pointer
            end -= 1

# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        colors=inputs[i]
        print(i + 1, ".\tcolors:", colors)
        sort_colors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)

if __name__ == "__main__":
    main()