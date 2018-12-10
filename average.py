def average(prices):
    total = 0
    for price in prices:
        total = total + price
    avg = total / len(prices)
    return avg
def main():
    numbers = (1,2,3,4,5)
    print(average(numbers))
main()
