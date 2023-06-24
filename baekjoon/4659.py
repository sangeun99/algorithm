import sys

def nicePassword(str) :
  vowels = ['a', 'e', 'i', 'o', 'u']
  exceptions = ['e', 'o']
  vowelCount = 0
  vowelSeq = 0
  consonantSeq = 0
  lastletter = ''
  for i in str :
    if i in vowels:
      vowelCount += 1
      vowelSeq += 1
      consonantSeq = 0
    else :
      consonantSeq += 1
      vowelSeq = 0
    if vowelSeq == 3 or consonantSeq == 3 :
      return False
    if (i not in exceptions) and (i == lastletter) :
      return False
    lastletter = i
  if vowelCount == 0 :
    return False
  else :
    return True

def main():
  while (1) :
    password = sys.stdin.readline().strip()
    if (password == "end") :
      exit()
    elif (nicePassword(password)) :
      print('<{}> is acceptable.'.format(password))
    else :
      print('<{}> is not acceptable.'.format(password))
if __name__ == "__main__" :
  main()