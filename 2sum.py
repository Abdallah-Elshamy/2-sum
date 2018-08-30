#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:44:35 2018

@author: Abdallah-Elshamy
"""
from threading import Thread
ans = 0 

def two_sum(nums , start ,end):
    global ans 
    for t in range(start,end + 1):
        for x in nums.keys():
            y = t - x
            if y != x and nums.get(y) != None:
                ans += 1
                break                              
     


nums = {}
with open('2sum.txt') as f:
    data = f.readlines()
    for line in data:
        nums[int(line)] = 0
f.close()

t1 = Thread(target = two_sum , args =(nums ,-10000,-7500))
t2 = Thread(target = two_sum , args =(nums ,-7500,-5000))
t3 = Thread(target = two_sum , args =(nums ,-5000,-2500))
t4 = Thread(target = two_sum , args =(nums ,-2500,0))
t5 = Thread(target = two_sum , args =(nums ,0,2500))
t6 = Thread(target = two_sum , args =(nums ,2500,5000))
t7 = Thread(target = two_sum , args =(nums ,5000,7500))
t8 = Thread(target = two_sum , args =(nums ,7500,10000))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()


print(ans)

