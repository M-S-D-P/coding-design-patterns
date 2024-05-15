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