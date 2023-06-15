def prime(n) :
  if (n == 1) :
    return False
  for i in range(2, n):
    if n % i == 0 :
      return False
  return True

def all_prime(m ,n) :
  for i in range(m, n + 1) :
    if (prime(i)):
      print(i)

def main():
  m, n = map(int, input().split())
  print(all_prime(m, n))

if __name__== "__main__" :
    main()
