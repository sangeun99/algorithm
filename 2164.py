def main() :
  N = int(input())
  n_list = list(range(1, N + 1))

  while (len(n_list) > 1) :
    n_list.pop(0)
    n_list.append(n_list.pop(0))
  
  print(n_list[0])

if __name__== "__main__" :
  main()