def reverse(array, startIndex=0, endIndex=0):
  if endIndex == 0:
    endIndex = len(array) - 1

  # empty or 1 element
  if startIndex == endIndex or startIndex == endIndex - 1:
    return array
  
  # stop recursion
  if startIndex > endIndex - 1:
    return array

  # swap
  array[startIndex], array[endIndex] = array[endIndex], array[startIndex]
  # move deeper
  return reverse(array, startIndex+1, endIndex-1)


print(reverse([1]))
