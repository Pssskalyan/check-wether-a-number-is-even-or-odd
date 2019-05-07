num = int(input())

mod = num % 2

if num < 0:

    print("invalid")
elif mod > 0:

    print("Odd")
else:
    print("Even")
