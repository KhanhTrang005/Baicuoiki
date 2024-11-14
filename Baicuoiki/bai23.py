# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:16:55 2024

@author: Windows
"""
def question_23(nums: list[int]) -> bool:
    for i in range(len(nums)):
        if nums.count(nums[i])>1:
            return True
    return False
    print( question_23([1,1,2,3,4,5]))            
