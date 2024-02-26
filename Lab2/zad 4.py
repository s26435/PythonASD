"""
Jan Wolski 2/26/24
"""
num = "11"
x = 0
for i in range(len(num)):
    x += int(num[i])*(pow(2,len(num)-i-1))

print(x)