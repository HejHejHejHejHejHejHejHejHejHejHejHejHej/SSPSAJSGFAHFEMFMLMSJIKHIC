import random
while True:
    N = random.randint(1,100)
    x = 0

    print("gissa talet")

    while True:
        while True:
            try:
                S = int(input("Svar: "))
                break
            except:
                print("du ska icke var dum i huvudet")
                continue

        x = x+1

        if S == N:
            print("Hejdå")
            break
        elif S >= N:
            print("Lägre")
        elif S <= N:
            print("Höger")

        if x == 7:
            break

    print((x - 7)*-1, "poäng")
    q = input("y är den knapp som bör vidröras om denna användare önskar försöka igen: ")
    if q == "y":
        continue
    else:
        exit()