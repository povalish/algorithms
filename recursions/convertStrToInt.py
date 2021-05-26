def convertStrToInt(sourceStr, rank=1):
  value = int(sourceStr[-rank]) * (10 ** (rank - 1))
  if rank == len(sourceStr):
    return value
  return value + convertStrToInt(sourceStr, rank+1)


print(convertStrToInt('13531'))
