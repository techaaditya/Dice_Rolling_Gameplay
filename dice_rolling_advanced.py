import random

sessions=0
while True:
    choice=input('Roll the dice ? (y/n): ').lower()
    if choice=='y':
        try:
            roll=int(input('Enter the no. of dice: '))
            if roll<=0:
                print('Enter positive count only,')
                continue
            for i in range(1,roll+1):
                a=random.randint(1,6)
                print(f'Dice {i}:{a}')
            print(f'dice rolled : {roll}')
            sessions+=1
        except ValueError:
            print('Invalid Input;Enter integers only')

    elif choice=='n':
        print(f'Total Gameplay Sessions:{sessions}')
        print('Thank you for playing !')
        break
    else:
        print('Invalid Input !')