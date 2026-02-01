from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# for i in range(len(val)):
#     print(val[i], end=' ')

# for x in val:
#     print(x, end=' , ')

# print(val.typecode)

# val.reverse()
# for x in val:
#     print(x, end=' , ')

# val.insert(1,  50)
# for i in val:
#     print(i, end=' ')

# val.append(100)
# for i in val:
#     print(i, end=' ')

# val[2]=1000
# for i in val:
#     print(i, end=' ')

# copyVal = array(val.typecode, (x for x in val))
# copyVal = array(val.typecode, (x*3 for x in val))
# for i in copyVal:
    # print(i, end=' ')

# val.pop(3)
# val.pop()
# for i in val:
#     print(i, end=' ')

# val.remove(1)
# for i in val:
#     print(i, end=' ')

# arr = val[2:5]
# for i in arr:
#     print(i, end=' ')

# arr = val[2:-3]
# for i in arr:
#     print(i, end=' ')

# arr = val[::-1]
# for i in arr:
#     print(i, end=' ')

# arr = array("i", [])
# n = int(input('Enter array length'))
# for i in range(n):
#     arr.append(int(input('Enter element')))

# for i in arr:
#     print(i, end=' ')

i = val.index(3)
print(i)

for i in val:
    print(i, end=' ')