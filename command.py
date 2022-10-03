from re import search
from hello import get_choise
import shutil

def my_function():
    while True:
        get_choise()
        n = int(input())
        if n == 1:
            answer = int(input('Из какого файла посмотреть информацию?\n 1 - book.txt или 2 - new_book.txt '))
            if answer == 1:
                with open('book.txt', 'r', encoding = 'utf_8') as f:
                    for line in f.readlines():
                        print(line)
            elif answer ==2:
                with open('new_book.txt', 'r', encoding = 'utf_8') as f:
                    for line in f.readlines():
                        print(line)
            input('\nНажмите enter')

        elif n == 2:
            answer = int(input('В какой из файлов ввести данные?\n 1 - book.txt или 2 - new_book.txt '))
            if answer == 1:
                answer = input('как ввести текст: в строку(1) или в столбец(2)? ')
                f = open('book.txt','a+', encoding = 'utf_8')
                if answer == '1':
                    new_contact = input('Введите данные ').split(' ')
                    f.write('\n\n' + ', '.join(new_contact))
                    f.close()
                elif answer == '2':
                    new_contact = input('Введите данные ').split(' ')
                    f.write('\n\n' + '\n'.join(new_contact))
                    f.close()
            elif answer == 2:
                answer = input('как ввести текст: в строку(1) или в столбец(2)? ')
                f = open('new_book.txt','a+', encoding = 'utf_8')
                if answer == '1':
                    new_contact = input('Введите данные ').split(' ')
                    f.write('\n\n' + ', '.join(new_contact))
                    f.close()
                elif answer == '2':
                    new_contact = input('Введите данные ').split(' ')
                    f.write('\n\n' + '\n'.join(new_contact))
                    f.close()

        elif n == 3:
            f1 = open('book.txt','a+', encoding = 'utf_8')
            f2 = open('new_book.txt','r', encoding = 'utf_8')
            f1.write('\n')
            for line in f2.readlines():
                f1.write(line)
            f1.write('\n')
            f1.close()
            f2.close()
            input('нажмите enter')

        elif n == 4:
            f1 = open('new_book.txt','a+', encoding = 'utf_8')
            f2 = open('book.txt','r', encoding = 'utf_8')
            f1.write('\n')
            for line in f2.readlines():
                f1.write(line)
            f1.write('\n')
            f1.close()
            f2.close()
            input('нажмите enter')
        elif n == 5:
            print('До встречи')
            exit()