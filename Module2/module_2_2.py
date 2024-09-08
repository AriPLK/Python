first = int(input("First: "))
second = int(input("Second: "))
third = int(input("Third: "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
