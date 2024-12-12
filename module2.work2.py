first = int(input("input fist number: "))
second = int(input("input sekond: "))
third = int(input("input third: "))
if first == second == third:
    print(3)
elif (first == second or first == third or second == third):
    print(2)
else:
    print(0)