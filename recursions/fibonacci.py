def fibonacci_loop(n):
  prev = 0
  curr = 1

  if n < 2:
    return n

  for _ in range(2, n):
    curr, prev = prev + curr, curr

  return prev + curr



def fibonacci_recursion_bad(n):
  if n < 2:
    return n

  return fibonacci_recursion_bad(n - 1) + fibonacci_recursion_bad(n - 2)



def fibonacci_recursion_good(n):
  if n < 2:
    return (n, 0)

  (curr, prev) =  fibonacci_recursion_good(n - 1)
  return (curr + prev, curr)
  


print(fibonacci_recursion_good(5))