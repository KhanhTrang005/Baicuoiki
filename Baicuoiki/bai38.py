# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:49:09 2024

@author: Windows
"""
def question_38(n: int) -> int:
    if n <=1 :
        return 1
    a, b = 1,1 
    for i in range(2, n+1):
        a, b = b, a + b
    return b 

if __name__ == "__main__":
    print(question_38(3))
    print(question_38(2))

    
