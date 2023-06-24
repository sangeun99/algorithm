from collections import deque
import sys

def VPS(str) :
  deq = deque()
  for i in str :
    if i == "(" :
      deq.append(i)
    elif i == ")" and len(deq) != 0 :
      deq.pop()
    else :
      return False
  if (len(deq) == 0) :
    return True
  else :
    return False

def main() :
  T = int(sys.stdin.readline())
  for i in range(T) :
    str = sys.stdin.readline().strip()
    if VPS(str) :
      print('YES')
    else :
      print('NO')

if __name__== "__main__" :
  main()