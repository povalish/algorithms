import os



def memory_usage(path):
  print(f'PathL {path}')

  # check for file/folder exisiting
  if not os.path.exists(path):
    return 0

  total = os.path.getsize(path)

  if os.path.isdir(path):
    for filename in os.listdir(path):
      file_path = os.path.join(path, filename)
      total += memory_usage(file_path)

  return total


print(memory_usage('/Users/poval/practice/algorithms'))