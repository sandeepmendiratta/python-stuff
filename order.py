orders = []
while (True):
    order = input("What would you like to order, Please enter (Q to quit)")
    if order == "tea":
        print("Sorry tea is not available")
        continue
    elif order.upper() == "Q":
        break
    # found = menu.get(order)
    # if found:
    orders.append(order)
    # else:
        # print("this item does not exist")
    order = input(" Do you like to order something else")
print(orders)
