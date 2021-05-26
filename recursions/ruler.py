def draw_line(length, label = ''):
  """
  Draw ruler line with provided length and optional label
  """
  line = '-' * length

  if label:
    line += ' ' + label

  print(line)



def draw_interval(center_tick):
  """
  Call drawer recursively.

  Draw center line, and call this function 
  for left and right sides.
  """

  if center_tick > 0:   # recursion stopper
    draw_interval(center_tick - 1)
    draw_line(center_tick)
    draw_interval(center_tick - 1)



def draw_ruler(num_inches, major_tick):
  """
  Main function for drawing English ruler.

  Draw first line, then draw intervals in the loop.
  """

  draw_line(major_tick, '0')  # draw first line

  # then draw intervals
  for i in range(1, 1 + num_inches):
    draw_interval(major_tick - 1)
    draw_line(major_tick, str(i))




if __name__ == '__main__':
  draw_ruler(3, 4)
