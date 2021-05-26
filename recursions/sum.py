def linear_sum(array, index=0):
  if index == (len(array) - 1):
    return array[index]
  return array[index] + linear_sum(array, index+1)
  
