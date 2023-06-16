from collections import deque

def main() :
  N = int(input())
  n_list = deque(range(1, N + 1))

  while (len(n_list) > 1) :
    n_list.popleft()
    n_list.append(n_list.popleft())
  
  print(n_list[0])

if __name__== "__main__" :
  main()