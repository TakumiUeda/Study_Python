#coding: UTF-8
import math
NUM = 10
SQ_NUM = int(math.sqrt(NUM))
prime = NUM * [1]


prime[0]=0

for i in range(1,SQ_NUM):
    if prime[i] and True:
        j=i+1
        while ((i+1)*j) <= NUM:
            prime[(i+1)*j-1]=0
            j+=1
j=0
k=0
for j in range(NUM):
    if prime[j] and True:
        k+=1;
        print(j+1)

print('発見した素数の個数は{0}個です'.format(k))
