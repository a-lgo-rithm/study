totalPrice = int(input())
totalNumber = int(input())

currentPrice = 0
currentNumber = 0

for i in range(1, totalNumber + 1):
    userInput = input()

    price, number = userInput.split(' ')
    price = int(price)
    number = int(number)

    currentPrice += price * number
    currentNumber += number

if currentPrice == totalPrice:
    print("Yes")
else:
    print("No")
