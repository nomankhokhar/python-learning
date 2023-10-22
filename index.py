# Variables

noman = "Noman Ali"

print(noman)

comment = """
I am Python Learning LOL Best in the Developer it's my though but it's may be or may not be true
"""

print(comment)

arr = [1, 0, 2, 0, 4665, 0, 35, 4, 0, 64, 6, 45, 75675, 675655]
print('Orignal Arr : ', arr)

index = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[index] = arr[i]
        index = index + 1


print(index)

for index in range(len(arr)):
    arr[index] = 0

print("All Zero in the End : ", index)
