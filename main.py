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

models = ["Ford", "Holden", "Toyota", "Mitsubishi", "Mazda"]
for model in models:
    print(model)

s = 0
for i in range(1,11):
    s = s+i
print(s)

