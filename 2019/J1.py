#2019
#J1_Winning Score

three_apples = int(input("Enter number of successful 3 point shots from Apples:"))
two_apples = int(input("Enter number of successful 2 point shots from Apples:"))
one_apples = int(input("Enter number of successful 1 point shots from Apples:"))
three_bananas = int(input("Enter number of successful 3 point shots from Bananas:"))
two_bananas = int(input("Enter number of successful 2 point shots from Bananas:"))
one_bananas = int(input("Enter number of successful 1 point shots from Bananas:"))

total_apples = ((three_apples*3)+(two_apples*2)+(one_apples*1))
total_bananas = ((three_bananas*3)+(two_bananas*2)+(one_bananas*1))

if total_apples > total_bananas:
    print("A")

elif total_bananas > total_apples:
    print("B")

else:
    print("T")
