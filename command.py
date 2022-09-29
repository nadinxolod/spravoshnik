from re import search
from hello import num 
import shutil 
if num == 1:
    with open('book.txt', 'r', encoding = 'utf_8') as f:
        for line in f.readlines():
            print(line)

elif num == 3:
    answer = input('как ввести текст: в строку или в столбец?')
    f = open('book.txt','a+', encoding = 'utf_8')
    if answer.lower() == 'строка':
        new_contact = input().split(' ')
        f.write('\n' + ', '.join(new_contact))
    elif answer.lower() == 'столбец':
        new_contact = input().split(' ')
        f.write('\n' + '\n'.join(new_contact))
    f.close()
# elif num == 2:

elif num == 4:
    # file = open('book.txt','r', encoding = 'utf_8')  
    # f = open('new_book.txt','r+', encoding = 'utf_8')
    # f.write(str(file.readlines()))
    # f.close()
    # file.close()  

    shutil.copy2('book.txt', 'new_book.txt')
