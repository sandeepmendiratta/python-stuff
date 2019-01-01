def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:

        print(primes)
        print("Entered while loop")
        for y in primes:  # use the primes list!
            print(x)
            print(y)
            if x%y == 0:
                x += 2
                print("before break")
                print(primes)
                break
        else:
            print("after break")
            primes.append(x)
            x += 2
            print(primes)
    print(primes)
    return len(primes)

count_primes2(9)
