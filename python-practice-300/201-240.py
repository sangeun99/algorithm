# ----------------
#   파이썬 함수
# ----------------


# 200 - 210

def print_coin():
    print("비트코인")

def print_coins() :
    for _ in range(100):
        print_coin()

print_coins()

# 211 - 220

def print_with_smile(str):
    print(f'{str}:D')

print_with_smile("hello")

def print_upper_price(price):
    print(price * 1.3)


def print_sum(a, b):
    print(a + b)

def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

print_arithmetic_operation(3, 4)

def print_max(a, b, c) :
    max = a
    if (max < b) :
        max = b
    if (max < c) :
        max = c
    print(max)

print_max(3, 6, 2)

# 221 - 230

def print_reverse(str) :
    result = ''
    for i in range(len(str) - 1, -1, -1):
        print(str[i], end="")
    print()

print_reverse("python")

def print_reverse_best(str) :
    print(str[::-1])

print_reverse_best("python")

def print_score(lst) :
    sum = 0
    for score in lst:
        sum += score
    mean = sum / len(lst)
    print(mean)
  
print_score([1, 2, 3])

def print_even(lst):
    for num in lst:
        if (num % 2 == 0):
            print(num)

print_even([1, 3, 2, 10, 12, 11, 15])

def print_keys(dict):
    for key in dict.keys():
        print(key)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

def print_value_by_key(dict, key):
    print(dict[key])

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
print_value_by_key  (my_dict, "10/26")

def print_5xn(str):
    for i in range(0, len(str), 5):
        print(str[i:i+5])

print_5xn("아이엠어보이유알어걸")

def print_mxn(str, m):
    for i in range(0, len(str), m):
        print(str[i:i+m])    

print_mxn("아이엠어보이유알어걸", 3)


def calc_monthly_salary(num):
    print(num // 12)

calc_monthly_salary(12000000)

# 231 - 240

def make_url(str):
    url = "www." + str + ".com"
    print(url) 

make_url("naver")

def make_list(str):
    result = []
    for i in str:
        result.append(i)
    print(result)

make_list("abcd")

def pickup_even(lst):
    result = []
    for num in lst:
        if (num % 2 == 1):
            result.append(num)
    print(result)

pickup_even([3, 4, 5, 6, 7, 8])

def convert_int(str):
    except_comma = ''
    for c in str:
        if (c != ','):
            except_comma += c
    result = int(except_comma)
    return result

print(convert_int("1,234,567"))

def convert_int_best(str):
    return int(str.replace(',', ''))

print(convert_int_best("1,234,567"))