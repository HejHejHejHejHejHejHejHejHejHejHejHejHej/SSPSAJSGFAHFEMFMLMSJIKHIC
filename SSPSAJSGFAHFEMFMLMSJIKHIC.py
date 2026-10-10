import random

N = random.randint(1,100)

for x in range(0,7):
    while True:
        try:
            S = int(input("Svar: "))
            break
        except:
            print("Hej")
            continue

    if S == N:
        print("Hejdå")
        exit()
    elif S >= N:
        print("Lägre")
    elif S <= N:
        print("Höger")