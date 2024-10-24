import random 
options = ['rock', 'paper', 'scissors']

while True:
    print('welcome to rock,paper and scissors game\n pick an option\n'
        '1.rock\n2.paper\n3.scissors')
    user = input('select an option:\n')
    user_picks = ['1', '2', '3']
    if user not in user_picks:
        print('Enter a valid choice')
    else:
        break

    
computer = random.choice(options)


if user == '1':
    pick = options[0]
if user == '2':
    pick = options[1]
if user == '3':
    pick = options[2]

print(f'you picked {pick} and computer picked {computer}')

if pick == computer:
    print(f"it's a tie")

#if user pick is a rock 
if pick == options[0]: 
    if computer == options[1]:
        print(f"paper covers rock, computer wins")
    elif  computer == options[2]:
        print(f"rock crushes scissors, you win")

#if user pick is paper         
if pick == options[1]:
    if computer == options[0]:
        print('paper covers rock, you win')
    elif computer == options[2]:
        print(f"paper covers scissors, computer wins")

#if user pick  is scissors         
if pick == options[2]:
    if computer == options[0]:
        print('rock  crushes scissors, computer wins')
    elif  computer == options[1]:
        print(f'scissors cuts paper, you win')







