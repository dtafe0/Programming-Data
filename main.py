def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number(90)

x = 1000
y = 10
st = "x is less than y" if (x<y) else "x is greater than or the same"
print (st)

# 1
print("area =", 2.6 * 3.7)

# 2
H = "hello"
W = "world"
print(H + W)

# 3 
g = "giraffe"
n = 3
print(n*g)
print(n,g)
print(str(n)+g)

# 4 
print("The room as an area of ", 2.6 * 3.7, "m2")

# 5 
print("Hello, Welcome to programming")
name = input("what is your name?")
print("nice to meet you", name)