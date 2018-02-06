import os
import re

input = open('gotovo.txt', 'r')
output = open('gotovo1.txt', 'w')
linesarray = input.readlines()
input.close()
seen = []
for i in range(len(linesarray)):
    if seen.count(linesarray[i]) == 0:
        seen.append(linesarray[i])
        output.write(linesarray[i])
output.close()
