#import random
#num = random.randrange(0, 9)
#from  random import randrange as p 
#num = p(0,100)
from rand import num, guess_limit, guess, guess_number     #, start_time, end_time
from rand import start, end
guess = int(input(f'Guess a number 0-5: '))
while guess_number < guess_limit:
  #  guess = int(input('GUess a number 1-20: '))
  #  guess = int(input(f'Guess # {guess_number+1} a number 1-20: last guess:{guess} '))
   
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 0-5: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 0-5: '))
    
    if guess == num:
      #  start_time,  end_time
      
       print(f'You Win! You Guessed it: {guess}  in {round(end - start , 1)} seconds')
    #  print(f'You Win! You Guessed it: {guess}  in {round(end, 1)} seconds')
    break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')