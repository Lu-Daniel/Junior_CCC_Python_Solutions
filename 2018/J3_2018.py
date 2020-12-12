#2018
#J1_Telemarketer

inpt = input()

res = [int(i) for i in inpt.split() if i.isdigit()]

c1_c1 = int(res[0] - res[0])
c1_c2 = int(res[0])
c1_c3 = int(res[1] + c1_c2)
c1_c4 = int(res[2] + c1_c3)
c1_c5 = int(res[3] + c1_c4)

c2_c2 = int(res[1] - res[1])
c2_c1 = int(abs(c2_c2 - res[0]))
c2_c3 = int(res[1] + c2_c2)
c2_c4 = int(res[2] + c2_c3)
c2_c5 = int(res[3] + c2_c4)

c3_c3 = int(res[2] - res[2])
c3_c1 = int(abs(c3_c3 - res[0] - res[1]))
c3_c2 = int(abs(c3_c3 - res[1]))
c3_c4 = int(res[2] + c3_c3)
c3_c5 = int(res[3] + c3_c4)

c4_c4 = int(res[3] - res[3])
c4_c1 = int(abs(c4_c4 - res[0] - res[1] - res[2]))
c4_c2 = int(abs(c4_c4 - res[1] - res[2]))
c4_c3 = int(abs(c4_c4 - res[2]))
c4_c5 = int(res[3] + c4_c4)

c5_c5 = int(res[3] - res[3])
c5_c1 = int(abs(c5_c5 - res[0] - res[1] - res[2] - res[3]))
c5_c2 = int(abs(c5_c5 - res[1] - res[2] - res[3]))
c5_c3 = int(abs(c5_c5 - res[2] - res[3]))
c5_c4 = int(abs(c5_c5 - res[3]))


print(c1_c1,c1_c2,c1_c3,c1_c4,c1_c5)
print(c2_c1,c2_c2,c2_c3,c2_c4,c2_c5)
print(c3_c1,c3_c2,c3_c3,c3_c4,c3_c5)
print(c4_c1,c4_c2,c4_c3,c4_c4,c4_c5)
print(c5_c1,c5_c2,c5_c3,c5_c4,c5_c5)