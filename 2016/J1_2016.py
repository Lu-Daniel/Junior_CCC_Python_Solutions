#2016
#J1_Tournament_selection

win = 0

for i in range(6):
    a = input()
    if "W" in a:
        win += 1

if win == 5 or win == 6:
        print("1")

elif win == 3 or win ==4:
        print("2")

elif win == 1 or win ==2:
        print("3")

else:
    print("-1")



