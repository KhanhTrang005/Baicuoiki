# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 02:33:40 2024

@author: Windows
"""

def question_22(nums: list[int]) -> None:
    ds = []
    for i in range(len(nums)):
        if i != 0:
           ds.append(i)
   # ds = [i for i in nums if i != 0]
    ds_moi = ds + [0] * (len(nums) - len(ds))
    return ds_moi 

print(question_22( [0,1,1,2,3,4,5,0,5]))
" biến = [expression for item in iterable if condition ]"
#expression: biểu thức tính toán giá trị của từng tử trong list mới
# item: biến được sử dụng để lặp qua từng phần tử trong list đầu
# condition: điều kiện kiểm tra các item phải thỏa để thêm vào