import random
count = 0
for number in range(10):

    player=int(input(""" мы играем камень-ножницы-бумага выберете: 1.камень 2.ножницы 3.бумага """)) 
    if player== 1:
        print("вы выбрали камень") 
    elif player == 2:
        print("вы выбрали ножницы") 
    elif player == 3:
        print("вы выбрали бумагу") 
    else:
        print("Я вас не понял ")

    comp = random.randint(1,3)

    if comp== 1:
        print("компьютер выбрал камень") 
    elif comp == 2:
        print("компьютер выбрал ножницы") 
    else:
        print("компьютер выбрал бумагу")

    if player == comp:
        print("ничья")
    elif player== 1 and comp== 2 or comp== 3 and player== 2 or player== 3 and comp== 1: 
        print("вы победили")
        count +=1
    elif  player== 2 and comp== 1 or comp== 2 and player== 3 or player== 1 and comp== 3 : 
        print("вы проиграли") 
    else:
        print("Я вас не понял ")
    if count == 3:
        print("игра окончена")
        break