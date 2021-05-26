
# O(n)
def pow(number, power):
  if power == 0:
    return 1
  if power == 1:
    return number
  return number * pow(number, power - 1)


# O(log n)
def pow_efficient(number, power):
  if power == 0:
    return 1
  if power == 1:
    return number
  
  partial = pow_efficient(number, power // 2)
  result = partial * partial

  if power % 2 == 1:
    result *= number

  return result

