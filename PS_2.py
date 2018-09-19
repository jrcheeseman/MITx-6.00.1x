
# Problem 1

balance = 10970.28
annualInterestRate = 0.164
monthlyPaymentRate = 0.02

i = 0
while i < 12:
    minPayment = balance * monthlyPaymentRate
    unpaidBal = balance - minPayment
    interest = (annualInterestRate / 12) * unpaidBal
    balance = unpaidBal + interest
    i += 1
print('Remaining balance:', round(balance, 2))


# Problem 2

minFixed = 0
tempBal = balance
while tempBal > 0:
    i = 0
    tempBal = balance
    minFixed += 10
    while i < 12:
        unpaidBal = tempBal - minFixed
        interest = (annualInterestRate / 12) * unpaidBal
        tempBal = unpaidBal + interest
        i += 1
print('Lowest Payment:', round(minFixed, 2))


# Problem 3

epsilon = 0.01
lo = balance / 12
hi = (balance * (1 + annualInterestRate / 12) ** 12) / 12
minFixed = (hi + lo) / 2
tempBal = 0

while abs(round(tempBal, 2)) != epsilon:

    i = 0
    tempBal = balance

    while i < 12:
        unpaidBal = tempBal - minFixed
        interest = (annualInterestRate / 12) * unpaidBal
        tempBal = unpaidBal + interest
        i += 1

    if abs(round(tempBal, 2)) == epsilon:
        break
    elif tempBal < 0:
        hi = minFixed
    else:
        lo = minFixed
    minFixed = (hi + lo) / 2

print('Lowest Payment:', round(minFixed, 2))




