k = int(input())

mod = k % 2

if k < 0:

    print("invalid")
elif mod > 0:

    print("Odd")
else:
    print("Even")
