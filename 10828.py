import sys

def push(stack, x) :
  stack.append(x)

def pop(stack):
  if (len(stack) == 0) :
    print(-1)
  else :
    print(stack.pop())

def size(stack):
  print(len(stack))

def empty(stack):
  if (len(stack) == 0) :
    print(1)
  else :
    print(0)

def top(stack):
  if (len(stack) == 0) :
    print(-1)
  else :
    print(stack[len(stack)-1])

def main():
  stack = []
  N = int(sys.stdin.readline())
  for i in range(N) :
    cmd_input = sys.stdin.readline().split()
    cmd = cmd_input[0]
    if cmd == 'push' :
      x = int(cmd_input[1])
      push(stack, x)
    elif cmd == 'pop' :
      pop(stack)
    elif cmd == 'size' :
      size(stack)
    elif cmd == 'empty' :
      empty(stack)
    elif cmd == 'top' :
      top(stack)

if __name__== "__main__" :
  main()