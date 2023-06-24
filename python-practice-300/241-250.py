# ----------------
#   파이썬 모듈
# ----------------

import datetime

now = datetime.datetime.now()
print(now, type(now))

def before_x_days(x) :
    return datetime.date.today() + \
      datetime.timedelta(days = x)

print(before_x_days(5))
print(before_x_days(4))
print(before_x_days(3))
print(before_x_days(2))
print(before_x_days(1))

now = datetime.datetime.now()
print(now.strftime('%H:%M:%S'))

date = "2020-05-04"
ret = datetime.datetime.strptime(date, '%Y-%m-%d')
print(ret, type(ret))


import time

def sleep_1sec():
    while True:
        print(datetime.datetime.now())
        time.sleep(1)

# sleep_1sec()

import os

print(os.getcwd())

def make_txt(filename):
    f = open(filename, 'x')
    f.close()

def rename_file(filename) :
    os.rename(filename, 'hi.txt')

# make_txt('hello.txt')
# rename_file('hello.txt')


import numpy

print(numpy.arange(0.0, 5.1, 0.1))