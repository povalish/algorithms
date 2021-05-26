def insertion_sort(array):
  start_index = 1
  end_index = len(array)

  for i in range(start_index, end_index):
    # if current picked element less then prev. element
    if array[i] < array[i-1]: # start sorting
      j = i
      while j > 0 and array[j] < array[j-1]:
        array[j-1], array[j] = array[j], array[j-1]
        j -= 1

  return array



print(insertion_sort([2, 3, 4, 1, 7, 6, 5]))
