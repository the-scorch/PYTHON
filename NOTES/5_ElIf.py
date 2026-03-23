speed = int(input())
if(speed > 60):
    print("Danger Speed!") # Indentation : space to tell compiler that this statement is with 'if'
else:
    print("Safe Speed.")

b = int(input())
r = int(input())
if(r > b):
    print("Rob scored higher marks than Bob") # executed if True
elif(r < b):
    print("Bob scored higher marks than Rob") # cheked if the 1st was False
else:
    print("Rob & Bob both scored the same") # executed if above are False

A = list(input().split())
b = input()
for a in A:
    if a == b:
        print("YES")
        quit() # ends the program early
print("NO")