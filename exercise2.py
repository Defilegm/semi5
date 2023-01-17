arr = [' '  for i in range (9)]
firstplayername = input("Введите имя первого игрока: ")
secondplayername = input("Введите имя второго игрока: ")


if firstplayername == secondplayername:
    secondplayername += '1'
print(f'{firstplayername} играет крестиками')
print(f'{secondplayername} играет ноликами')
        

def showtable(matrix):
    print(f'\t {arr[0]} | {arr[1]} | {arr[2]}')
    print(f'\t___|___|___')
    print(f'\t {arr[3]} | {arr[4]} | {arr[5]}')
    print(f'\t___|___|___')
    print(f'\t {arr[6]} | {arr[7]} | {arr[8]}')
    print('\t   |   |')
    return matrix


def checknum():
    num = (input())
    if (num.isdigit() == False) or (int(num) > 9 or int(num)<1 ):
        print('Некорректный ввод, введите номер клетки (от 1 до 9): ')
        return checknum()
    return int(num)

def move(matrix,x = firstplayername, i = 1):
    if (matrix[0] == matrix[1]== matrix[2] == 'x') or (matrix[0] == matrix[1]== matrix[2] == 'o') :
        print(f'Игра окончена! Победил игрок {x}!')
        showtable(matrix)
        return 0
    elif (matrix[3] == matrix[4]==  matrix[5]== 'x') or (matrix[3] == matrix[4]==  matrix[5] == 'o')  :
        print(f'Игра окончена! Победил игрок {x}!')
        showtable(matrix)
        return 0
    elif (matrix[6] == matrix[7]==matrix[8]== 'x') or (matrix[6] == matrix[7]==matrix[8] == 'o') :
        print(f'Игра окончена! Победил игрок {x}!')
        showtable(matrix)
        return 0
    elif (matrix[0] == matrix[4]== matrix[8]== 'x') or (matrix[0] == matrix[4]== matrix[8] == 'o') :
        print(f'Игра окончена! Победил игрок {x}!')
        showtable(matrix)
        return 0
    elif (matrix[0] == matrix[3]==matrix[6]== 'x') or (matrix[0] == matrix[3]==matrix[6] == 'o') :
        print(f'Игра окончена! Победил игрок {x}!')
        showtable(matrix)
        return 0
    elif (matrix[1] == matrix[4]==matrix[7]== 'x') or (matrix[1] == matrix[4]==matrix[7] == 'o') :
        print(f'Игра окончена! Победил игрок {x}!')
        
        showtable(matrix)
        
        return 0
    elif (matrix[2] == matrix[5]== matrix[8]== 'x') or (matrix[0] == matrix[1]== matrix[2] == 'o') :
        print(f'Игра окончена! Победил игрок {x}!')
        showtable(matrix)
        return 0
    elif (matrix[2] ==  matrix[4]== matrix[6]== 'x') or (matrix[2] ==  matrix[4]== matrix[6] =='o') :
        print(f'Игра окончена! Победил игрок {x}!')
        showtable(matrix)
        return 0
    if i == 10:
        print('Ничья!')
        showtable(matrix)
        return 0
    
    print(f'ход номер {i}')
    showtable(matrix)

    if x == firstplayername:
        print(f'ход игрока {x}. Введите cвободное поле заполнения крестиком(буква "x")(от 1 до 9): ')
        index = checknum()
        while True:
            if (matrix[index-1] == 'x') or (matrix[index-1] =='o'):
                print('Поле занятно, повторите попытку ввода: ')
                index = checknum()
            else:
                break
        matrix[index-1] = 'x'    
        print()
        return move(matrix,x = secondplayername,i = i + 1)
    if x == secondplayername:
        print(f'ход игрока {x}. Введите cвободное поле заполнения ноликом(буква "o")(от 1 до 9): ')
        index = checknum()
        while True:
            if (matrix[index-1] == 'x') or (matrix[index-1] =='o'):
                print('Поле занятно, повторите попытку ввода: ')
                index = checknum()
            else:
                break
        matrix[index-1] = 'o'    
        print()
        return move(matrix,x = firstplayername,i = i + 1)
move(arr)