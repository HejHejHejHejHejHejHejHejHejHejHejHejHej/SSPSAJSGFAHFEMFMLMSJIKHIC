import random
from bcolors import bcolors
import subprocess
CLEAR = "cls"
subprocess.run(CLEAR, shell=True)
while True:
    N = random.randint(1,100)
    x = 0

    print(bcolors.YELLOW, bcolors.I + """
          =============          
           gissa talet           
          =============          \033[0m
          """)

    while True:
        while True:
            try:
                S = int(input(bcolors.YELLOW + "Svar: "))
                break
            except:
                print(bcolors.DEFAULT + "du ska icke var dum i huvudet")
                continue

        if S == 0:
            subprocess.run(CLEAR, shell=True)
            exit()
        if S == N:
            print(bcolors.GREEN + "Rätt")
            break

        x = x+1

        if x == 7:
            break

        if S >= N:
            print(bcolors.RED + "Lägre\n")
        elif S <= N:
            print(bcolors.BLUE + "Högre\n")

    if x == 0:
        print(bcolors.X + str((x - 7)*-1), "poäng\n")
    elif x == 1:
        print(bcolors.Q + str((x - 7)*-1), "poäng\n")
    elif x == 2:
        print(bcolors.W + str((x - 7)*-1), "poäng\n")
    elif x == 3:
        print(bcolors.E + str((x - 7)*-1), "poäng\n")
    elif x == 4:
        print(bcolors.R + str((x - 7)*-1), "poäng\n")
    elif x == 5:
        print(bcolors.T + str((x - 7)*-1), "poäng\n")
    elif x == 6:
        print(bcolors.Y + str((x - 7)*-1), "poäng\n")
    elif x == 7:
        print(bcolors.U + str((x - 7)*-1), "poäng\n")

    
    q = input(bcolors.YELLOW + "y är den knapp som bör vidröras om denna användare önskar försöka igen, (q)avsluta:")
    if q == "q":
        subprocess.run(CLEAR, shell=True)
        exit()

    subprocess.run(CLEAR, shell=True)