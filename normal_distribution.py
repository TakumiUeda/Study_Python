#coding: UTF-8

from random import Random
count = 6*[0]
NUM=10000

for i in range(NUM):
    r = Random()
    x = r.randint(1, 6)
    count[x-1]+=1
print(count)


