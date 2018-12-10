def get_order(menu):
    orders = []
    while True:
        order = input("what would like to order, Enter Q for quit :")
        if order == "Q":
            break
        orders.append(order)
    return orders
def print_menu(menu):
    for name, price in menu.items():
        print(name, ':$', format(price, '.2f'), sep='')
def bill_total(orders, menu):
    total = 0
    for order in orders:
        total += menu[order]
    return total
def write_sales_log(order):
    file = open('sales.txt', 'a')
    total = 0
    for item, price in order.items():
        file.write(item + ' '+ format(price, '.2f') + '\n')
        total += price
    file.write('total = ' + format(total, '.2f')+ '\n')
    file.close()


def main():
    menu = {'spam': 2.0, 'roti': 3.0, 'tea': 1}
    print("printing menu")
    print_menu(menu)
    order = get_order(menu)
    print("printing order")
    print(order)
    total_bill = bill_total(order, menu)
    print(total_bill)
    write_sales_log(menu)



main()
