print('Please think of a number between 0 and 100!')
high = 100
low = 0
guess = (high+low)//2
print('Is your secret number '+ str(guess) +' ?')
res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while res != 'c':
    if res == 'h':
        high = guess
    elif res == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
    guess = (high+low)//2
    print('Is your secret number '+ str(guess) +' ?')
    res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
print('Game over. Your secret number was: ' + str(guess))