namePhrase = "My name is: "
myName = "Andrew"
print(namePhrase + myName)

extraCredit = int(input("How much extra credit did you earn?"))
if extraCredit < 5:
    print("That's not enough extra credit.")
elif extraCredit > 20:
    print("That's too much extra credit.")

userPassword = input("Please enter a new password: ")
userCheck = input("Please enter your password to confirm: ")
if userPassword == userCheck:
    print("That is correct.")
else:
    print("That is incorrect.")

blackjack1 = int(input("Enter a card 1-13: "))
blackjack2 = int(input("Enter another card: "))
sum = blackjack1 + blackjack2
if sum == 21:
    print("BLACKJACK!")
elif sum >21:
    print("BUST!")
elif sum < 21:
    print("The total is: " + str(sum))