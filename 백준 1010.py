import sys
from math import *

N = int(sys.stdin.readline())

for i in range(N):
    a,b = map(int,sys.stdin.readline().split())

    aws = factorial(b)//(factorial(a)*factorial(b-a))
    print(aws)
