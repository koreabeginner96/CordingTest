from math import *
def solution(w,h):
    return w*h-(w+h-gcd(w,h))