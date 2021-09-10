import time
import os
clear = lambda: os.system('cls')

start = 1
command = 1
playagaini = 1
playagaininput = 1

while playagaini == 1:
    playagaininput = 1

    clear()

    time.sleep(1)

    print("-Welcome to Heads or Tails")
    time.sleep(0.5)
    print('-Type "flip" to start flipping!')
    while command == 1:
        cstart = input('-')
        if cstart == 'flip':
            clear()
            print('% Flipping! %')
            time.sleep(0.5)
            clear()
            print('$ Flipping! $')
            time.sleep(0.5)
            clear()
            print('% Flipping! %')
            time.sleep(0.5)
            clear()
            print('$ Flipping! $')
            result = 'Heads'
            time.sleep(0.5)
            command = 2
            clear()
        elif cstart == 'Flip':
            clear()
            print('% Flipping! %')
            time.sleep(0.5)
            clear()
            print('$ Flipping! $')
            time.sleep(0.5)
            clear()
            print('% Flipping! %')
            time.sleep(0.5)
            clear()
            print('$ Flipping! $')
            result = 'Tails'
            time.sleep(0.5)
            command = 2
            clear()    
        elif cstart != 'flip' or 'Flip':
            command = 1

    time.sleep(0.2)

    print("-" + result)

    time.sleep(0.8)

    while playagaininput == 1:
        playagainc = input('Do you want to play again? Y/n: ')
        if playagainc == 'y':
            playagaini = 1
            command = 1
            playagaininput = 2
        elif playagainc == 'n':
            playagaini = 2
            time.sleep(2)
            exit()
        elif playagainc != 'y' or 'n':
            playagaininput = 1
            clear()

