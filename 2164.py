def main() :
  N = int(input())
  n_list = list(range(1, N + 1))

  while (len(n_list) > 1) :
    first_item = n_list[1]
    n_list = n_list[2:]
    n_list.append(first_item)
  
  print(n_list[0])

if __name__== "__main__" :
  main()