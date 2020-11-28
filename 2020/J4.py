#2020
#J4_Cyclist_Shifts

T = input()
S = input()

output = "no"
for i in range (len(T)-len(S)+1):
    string_comparison = T[i:i+len(S)]
    for k in range (len(S)):
        if S == string_comparison:
            output = "yes"
            break
        S = S[1:] + S[0]

print(output)