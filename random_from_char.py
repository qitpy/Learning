import random

rainy = "rainy"
zero = "zero"
cold = "cold"
lipenty = "lipenty"

total = rainy + zero + cold + lipenty

def random_name(total):
    result = ""
    for x in range(3):
        s_random = random.choice(total)
        if x == 0:
            # while s_random in "ueoai":
            #     s_random = random.choice(total)
            # s_random = "t"
            pass
        elif x == 1:
            pass
        else:
            if result[-1] not in "ueoai" and result[-2] not in "ueoai":
                while s_random not in "ueoai":
                    s_random = random.choice(total)
            if result[-1] in "ueoai" and result[-2] in "ueoai":
                while s_random in "ueoai":
                    s_random = random.choice(total)
        total = total.replace(s_random, "")
        result += s_random
    return result

for i in range(10):
    print("q" + random_name(total) + "py")