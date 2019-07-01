"""
Created on Mon Jul  1 09:04:01 2019

@author: laelume
"""


for i in range (1,101):
    
    div3 = (i/3) - int((i/3))
    div5 = (i/5) - int((i/5))
    
    if div3 == 0 and div5 == 0:
        print("CracklePop")     
    elif div3 == 0:
        print("Crackle")
    elif div5 == 0:
        print("Pop")
    else:
        print(i)