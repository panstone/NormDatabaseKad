import os
import re

with open("gotovo1.txt") as gile:
    atr = [row.strip() for row in gile]
    ##print('\n'.join(arr))

with open("gotovo1copy.txt") as rile:
    acr = [row.strip() for row in rile]
    ##print('\n'.join(arr))
    
result=list(set(atr) - set(acr))
print('\n'.join(result))
