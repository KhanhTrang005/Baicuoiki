# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:44:23 2024

@author: Windows
"""
#10
def question_10() -> None:
    ds = input("Nhập danh sách: ")
    tach = ds.split()
    if tach:
        return ''.join([i for i in tach])
    return None
#11
def question_11(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    sotrc = 0
    sosau = 1
    
    for i in range(2,n+1):
        sohientai = sotrc + sosau
        sotrc=sosau
        sosau=sohientai
    return sohientai
if __name__=="__main__":
    print(question_11(5))
    print(question_11(10))

