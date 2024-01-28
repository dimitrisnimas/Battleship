#DIMITRIOS NIMAS for CSE at Univeristy of Ioannina





from random import randint
import random
players=[1,2]
player_1=['Player 1','CPU']
valid_positions=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']
cpu_valid_positions=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']
cpu_targetting=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']
ships1=[]
ships2=[]
choices_player_a=[]
choices_player_b=[]


print("BATTLESHIP GAME")
print("The objective is to sink the opponent's ships before the opponent sinks yours.")
player=int(input("Input 1 for 1-player game or 2 for 2-player game: "))
if player == 2: #Gia 2 paiktes
    for i in range (1,6):
        print("Player 1 enter the position of your ship no ", end=''),print(i, end=''),
        choice_player_1=input(": " )
        while choice_player_1 not in valid_positions or choice_player_1 in ships1:
            choice_player_1=input("Invalid position, or position already taken. Try again: ")
        else:
            ships1.append(choice_player_1)
    

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    

    for x in range (1,6):
        print("Player 2 enter the position of your ship no ", end=''),print(x, end=''),
        choice_player_2=input(": ")
        while choice_player_2 not in valid_positions or choice_player_2 in ships2:
            choice_player_2=input("Invalid position, or position already taken. Try again: ")
        else:
            ships2.append(choice_player_2)
    

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


    a=random.choice(players)
    print("Player" ,a, "starts first")
    ships_a=ships1
    ships_b=ships2
    pinakas1=[['  ','1 ','2 ','3 ','4 ','5 '],['a',' ',' ',' ',' ',' '],['b',' ',' ',' ',' ',' '],['c',' ',' ',' ',' ',' '],['d',' ',' ',' ',' ',' '],['e',' ',' ',' ',' ',' ']]
    pinakas2=[['  ','1 ','2 ','3 ','4 ','5 '],['a',' ',' ',' ',' ',' '],['b',' ',' ',' ',' ',' '],['c',' ',' ',' ',' ',' '],['d',' ',' ',' ',' ',' '],['e',' ',' ',' ',' ',' ']]
    

    def player1():
        print('   P1   ', end=' '*9),print('   P2   ')
        for i in range(0,6):
            print(pinakas1[0][i],end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas1[x][i], end=' ')
            print('')
        for i in range(0,6):
            print(pinakas2[0][i], end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas2[x][i], end=' ')
            print('')
        

        choice_player_a=input("Player 1 enter the position to throw your missle: ")
        while choice_player_a not in valid_positions or choice_player_a in choices_player_a:
            choice_player_a=input("Invalid position, or missile already thrown there. Try again: ")
        else:
            choices_player_a.append(choice_player_a)


        z=list(choice_player_a)
        q=z[0]
        w=z[1]
        if q=='a':
            q=1
        elif q=='b':
            q=2
        elif q=='c':
            q=3
        elif q=='d':
            q=4
        else:
           q=5
        if w=='1':
            w=1
        elif w=='2':
            w=2
        elif w=='3':
            w=3
        elif w=='4':
            w=4
        else:
            w=5
        if choice_player_a in ships_b:
            pinakas2[q][w]='o'
        else:
            pinakas2[q][w]='x'


        print("Missle thrown at" ,choice_player_a)
        if choice_player_a in ships_b:
            print("Target hit!")
            ships_b.remove(choice_player_a)
        else:
            print("Target missed!")
        if len(ships_b) == 0:
            print("GAME OVER. Player 1 wins.")
        else:
            pass
        return pinakas2
        
        
    def player2():
        print('   P1   ', end=' '*9),print('   P2   ')
        for i in range(0,6):
            print(pinakas1[0][i], end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas1[x][i], end=' ')
            print('')
        for i in range(0,6):
            print(pinakas2[0][i], end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas2[x][i], end=' ')
            print('')
        

        choice_player_b=input("Player 2 enter the position to throw your missle: ")
        while choice_player_b not in valid_positions or choice_player_b in choices_player_b:
            choice_player_b=input("Invalid position, or missile already thrown there. Try again: ")
        else:
            choices_player_b.append(choice_player_b)


        z=list(choice_player_b)
        q=z[0]
        w=z[1]
        if q=='a':
            q=1
        elif q=='b':
            q=2
        elif q=='c':
            q=3
        elif q=='d':
            q=4
        else:
           q=5
        if w=='1':
            w=1
        elif w=='2':
            w=2
        elif w=='3':
            w=3
        elif w=='4':
            w=4
        else:
            w=5
        if choice_player_b in ships_a:
            pinakas1[q][w]='o'
        else:
            pinakas1[q][w]='x'

            
        print("Missle thrown at" ,choice_player_b)
        if choice_player_b in ships_a:
            print("Target hit!")
            ships_a.remove(choice_player_b)
        else:
            print("Target missed!")
        if len(ships_a) == 0:
            print("GAME OVER. Player 2 wins.")
        else:
            pass
        return pinakas1

    if a == 1:
        while len(ships_a) != 0 and len(ships_b) != 0:
            player1()
            if len(ships_b) !=0:
                player2()
            else:
                break
        else:
            pass
    else:
        while len(ships_a) != 0 and len(ships_b) != 0:
            player2()
            if len(ships_a) !=0:
                player1()
            else:
                break
        else:
            pass
            
else: #Gia 1 paikti
    for i in range (1,6):
        print("Player 1 enter the position of your ship no ", end=''),print(i, end=''),
        choice_player_1=input(": ")
        while choice_player_1 not in valid_positions or choice_player_1 in ships1:
            choice_player_1=input("Invalid position, or position already taken. Try again: ")
        else:
            ships1.append(choice_player_1)


    for x in range (1,6):
        choice_cpu=random.choice(cpu_valid_positions)
        ships2.append(choice_cpu)
        cpu_valid_positions.remove(choice_cpu)


    a=random.choice(player_1)
    print(a, "starts first")
    ships_a=ships1
    ships_b=ships2
    pinakas1=[['  ','1 ','2 ','3 ','4 ','5 '],['a',' ',' ',' ',' ',' '],['b',' ',' ',' ',' ',' '],['c',' ',' ',' ',' ',' '],['d',' ',' ',' ',' ',' '],['e',' ',' ',' ',' ',' ']]
    pinakas2=[['  ','1 ','2 ','3 ','4 ','5 '],['a',' ',' ',' ',' ',' '],['b',' ',' ',' ',' ',' '],['c',' ',' ',' ',' ',' '],['d',' ',' ',' ',' ',' '],['e',' ',' ',' ',' ',' ']]

    
    def player():
        print('   P   ', end=' '*9),print('   CPU   ')
        for i in range(0,6):
            print(pinakas1[0][i], end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas1[x][i], end=' ')
            print('')
        for i in range(0,6):
            print(pinakas2[0][i], end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas2[x][i], end=' ')
            print('')


        choice_player_a=input("Player enter the position to throw your missle: ")
        while choice_player_a not in valid_positions or choice_player_a in choices_player_a:
            choice_player_a=input("Invalid position, or missile already thrown there. Try again: ")
        else:
            choices_player_a.append(choice_player_a)

            z=list(choice_player_a)
        q=z[0]
        w=z[1]
        if q=='a':
            q=1
        elif q=='b':
            q=2
        elif q=='c':
            q=3
        elif q=='d':
            q=4
        else:
           q=5
        if w=='1':
            w=1
        elif w=='2':
            w=2
        elif w=='3':
            w=3
        elif w=='4':
            w=4
        else:
            w=5
        if choice_player_a in ships_b:
            pinakas2[q][w]='o'
        else:
            pinakas2[q][w]='x'
        return pinakas2

            
        print("Missle thrown at" ,choice_player_a)
        if choice_player_a in ships_b:
            print("Target hit!")
            ships_b.remove(choice_player_a)
        else:
            print("Target missed!")
        if len(ships_b) == 0:
            print("GAME OVER. Player wins.")
            
        else:
            pass
        

    def cpu():
        print('   P   ', end=' '*9),print('   CPU   ')
        for i in range(0,6):
            print(pinakas1[0][i], end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas1[x][i], end=' ')
            print('')
        for i in range(0,6):
            print(pinakas2[0][i], end='')
        print('')
        for x in range(1,6):
            for i in range(0,6):
                print(pinakas2[x][i], end=' ')
            print('')

            
        choice_cpu=random.choice(cpu_targetting)

        z=list(choice_cpu)
        q=z[0]
        w=z[1]
        if q=='a':
            q=1
        elif q=='b':
            q=2
        elif q=='c':
            q=3
        elif q=='d':
            q=4
        else:
           q=5
        if w=='1':
            w=1
        elif w=='2':
            w=2
        elif w=='3':
            w=3
        elif w=='4':
            w=4
        else:
            w=5
        if choice_cpu in ships_a:
            pinakas1[q][w]='o'
        else:
            pinakas1[q][w]='x'
        print("Missle thrown at" ,choice_cpu)
        cpu_targetting.remove(choice_cpu)
        if choice_cpu in ships_a:
            print("Target hit!")
            ships_a.remove(choice_cpu)
        else:
            print("Target missed!")
        if len(ships_a) == 0:
            print("GAME OVER. CPU wins.")
            
        else:
            pass
        return pinakas1
        

    if a=='Player 1':
        while len(ships_a) != 0 and len(ships_b) != 0:
            player()
            if len(ships_b) !=0:
                cpu()
            else:
                break
        else:
            pass
    else:
        while len(ships_a) != 0 and len(ships_b) != 0:
            cpu()
            if len(ships_a) !=0:
                player()
            else:
                break
        else:
            pass

            
    


