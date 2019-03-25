from itertools import count
def lcm(*args):
    print(args)
    if len(args) == 1:
        return args[0]
    elif len(args) == 2:
        n = min(args[0])
        for k in count(1):
            if not (k * n)%max(args[0]):
                return k * n
    else:
        return lcm(lcm(args[:len(args)//2]), lcm(args[len(args)//2:]))



while True:
    print(eval(input(">>>")))
