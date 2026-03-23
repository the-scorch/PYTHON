# While Loop
n = 128
i = 2
while i <= 128: # till the condition is false
    print(i) # keep executing the code
    i *= 2

num = -1
while num != 0:
    num = int(input("Enter Zero: ")) # keep taking input until Zero
print("Success!")

# For Loop
numbers = [1, 6, 4, 3, 2, 5]
for num in numbers: # iterate list
    print(num, end=" ")

string = 'bolloon'
cnt = 0
for s in string: # iterate string
    if(s == 'o'):
        cnt += 1
print()
print(cnt)

for i in range(10): # 0 to 9
    print(i*i)

for i in range(55, 100, 3): # start : end : step
    print(i)

for i in range(30, 4, -1): # decrementing
    print(i)

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i: # Nested Loops
        print("*", end=' ')
        j += 1
    print()
    i += 1