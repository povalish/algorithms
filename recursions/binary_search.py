def binary_search(array, target, startIndex=0, endIndex=0):
  # if endIndex is not defined
  # set default value - max array index
  if endIndex == 0:
    endIndex = len(array)

  # validate endIndex
  # endIndex must be more then startIndex
  if endIndex < startIndex:
    return -1

  # pick middle index for matching
  middleIndex = (startIndex + endIndex) // 2

  # check middle value
  if target == array[middleIndex]:
    return middleIndex
  # if target value more then middle value
  elif target > array[middleIndex]:
    return binary_search(array, target, middleIndex + 1, endIndex)
  # or if target less then middle value
  else:
    return binary_search(array, target, startIndex, middleIndex - 1)
  


numbers = [2, 5, 9, 12, 28, 32, 37, 40, 44, 53, 73, 90]
foundedIndex = binary_search(numbers, 2)

print(f'Founded index: {foundedIndex}')
