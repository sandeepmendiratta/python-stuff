def dedup1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


def dedup2(x):
    a = set(x)
    b = list(a)
    return b

x = [1,3,4,2,4,9,23,3,3]
print(dedup1(x))
print(dedup2(x))
