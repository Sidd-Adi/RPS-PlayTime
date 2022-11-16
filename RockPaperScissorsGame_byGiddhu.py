import random
import sys
list = ('rock','paper','scissor')
print('Welcome to the Rock Paper Scissor Game!')
print('Quick mode is activated, you can also type p,r,s instead of paper, rock and scissor.')
try:
    n = int(input('How many times do you want to play? '))
except ValueError or NameError:
    print('Type an integer!')
    sys.exit()
z = 0
i = 0
easy_game = {'r':'rock','p':'paper','s':'scissor'}
while i < n:
    y = random.choice(list)
    x = input('Type your choice - rock, paper or scissor: ')
    user_input = x.lower()
    l = f'I chose {y}, {y} beats {easy_game.get(user_input,user_input)}...You Lost!'
    w = f'I chose {y}, {easy_game.get(user_input,user_input)} beats {y}...You Won!'
    if easy_game.get(user_input,user_input) == 'rock'  or easy_game.get(user_input,user_input) == 'paper' or easy_game.get(user_input,user_input) == 'scissor': 
        if easy_game.get(user_input,user_input) == y:
            print(f"I have also chosen {y}, it's a tie!")
            z+=0.5
        elif easy_game.get(user_input,user_input) == 'rock' and y == 'paper':
            print(l)
            z+=0
        elif easy_game.get(user_input,user_input) =='rock' and y == 'scissor':
            print(w)
            z+=1
        elif easy_game.get(user_input,user_input) == 'paper' and y == 'rock':
            print(w)
            z+=1
        elif easy_game.get(user_input,user_input) == 'paper' and y == 'scissor':
            print(l)
            z+=0
        elif easy_game.get(user_input,user_input) == 'scissor' and y == 'paper':
            print(w)
            z+=1
        elif easy_game.get(user_input,user_input) == 'scissor' and y == 'rock':
            print(l)
            z+=0
        i+=1
    else:
        print('Please type a valid input - rock, paper or scissor')
print('Your score is '+str(z))
if z < n/2:
    print('Sorry, you lost the series, better luck next time!')
elif z == n/2:
    print('Nice! The series is a tie!')
else:
    print('Congrats! You won the series!')



