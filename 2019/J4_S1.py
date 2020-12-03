#J4/S1_Flipper
#2019

I = input()
V = I.count("V")
H = I.count("H")

V_div = V%2
H_div = H%2

if V_div == 0:
    if H_div == 0:
        print("1 2\n3 4")
    else:
        print("3 4\n1 2")
else:
    if H_div == 0:
        print("2 1\n4 3")
    else:
        print("4 3\n2 1")