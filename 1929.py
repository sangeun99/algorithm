def makePrimeNumList(n) :
  primeNumList = list(range(0, n+1))
  primeNumList[1] = 0
  for i in range(2, n) :
    if primeNumList[i] == 0 :
      continue
    for j in range(2 * i, n + 1, i) :
      primeNumList[j] = 0
  return primeNumList

def main():
  m, n = map(int, input().split())
  
  primeNumList = makePrimeNumList(n)
  for i in range (m, n+1) :
    if (primeNumList[i] > 0) :
      print(primeNumList[i])

if __name__== "__main__" :
  main()
