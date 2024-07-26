counter_a = 0
counter_b = 0
vicky_is_woozy = 0
while vicky_is_woozy == 0:
    cozy = input("Password: ")
    if cozy == "WoozyVicky":
        vicky_is_woozy = 1
        print("Awwwww")
        break
    else:
        print("Incorrect Password!")
        continue

while vicky_is_woozy == 1:
    try:
        a = int(input("Enter first value to add: "))
        vicky_is_woozy = 2
    except: 
        counter_a = counter_a + 1
        if counter_a >= 3:
            print("You have failed too many times. Try running the code again.")
            quit()
        else:
            print("Not a valid number! Please try again!")
            continue
    break
while vicky_is_woozy == 2:
    try:
        b = int(input("Enter second value to add: "))
    except:
        counter_b = counter_b + 1
        if counter_b >= 3:
            print("You have failed too many times. Try running the code again.")
            quit()
        else:
            print("Not a valid number! Please try again!")
            continue
    break
sum = a + b
print("Your sum is",sum)
