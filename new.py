# import pandas as pd
monkeys = []

with open("input.txt") as f:
    # reading file line wise
    data = f.readlines()
    # number of monkeys in army
    N = int(data[0])
    # print(type(N))

    # converting int   
    monkeys = list(map(int, data))
    monkeys.remove(1000000)
    # print(monkeys[0])

    health = 2000
    injuries = 1
    max_inj = 1000000


    count = 0

    for monkey in monkeys:
        if health <= 0 and injuries >= max_inj:
            break
        else:    
            health = health - monkey
            injuries = injuries * monkey
            count += 1

    print("monkey defeated = ",count)        
        