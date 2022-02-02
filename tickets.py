ticket = int(input('How many tickets would you like to buy?'))
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Age {1} participant's "))
    if age < 18:
        price.append(0)
    elif 18 < age < 25:
        price.append(990)
    elif age > 25:
        price.append(1390)
print(price)
if ticket > 3:
    a = int(sum(price) - sum(price)/10)
    print("your purchase amount is:" , a)
else:
    a = sum(price)
    print ("your purchase amount is: ", a)
print(price)


