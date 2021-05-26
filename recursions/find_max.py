# def find_max(array):
#   result = array[0]

#   for element in array:
#     if element > result:
#       result = element

#   return result



def find_maxmin(array, index=0, max_value=None, min_value=None):
  if max_value is None:
    max_value = array[index]
    min_value = array[index]

  if index == len(array):
    return (max_value, min_value)

  # new_max_value = max_value
  # if (new_max_value > array[index]):
  #   new_max_value = array[index]

  # new_min_value = min_value
  # if (new_min_value < array[index]):
  #   new_min_value = array[index]

  return find_maxmin(
    array, 
    index+1, 
    array[index] if max_value > array[index] else max_value, 
    array[index] if min_value < array[index] else min_value
  )




array = [11, 2, 44, 23, 45, 12, 29, 209]

print(find_maxmin(array))
