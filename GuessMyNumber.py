x = 100
epsilon = 1
low = 0
high = x
ans = (high + low) // 2

print('Please think of a number between 0 and 100!')

while abs(ans**2 - x) >= epsilon:
    print('Is your secret number ' + str(ans) + '?')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end=' ')
    key = str(input())
    if key == 'l':
        low = ans
        ans = (high + low) // 2
    elif key == 'h':
        high = ans
        ans = (high + low) // 2
    elif key == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' + str(ans))
