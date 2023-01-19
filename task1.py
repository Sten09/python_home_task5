#1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
#
#in
#Number of words: 10
#
#out
#авб абв бав абв вба бав вба абв абв абв
#авб бав вба бав вба

#txt = input("Введите текст через пробел:\n")
#print(f"Исходный текст: {txt}")
#find_txt = "абв"
#lst = [i for i in txt.split() if find_txt not in i]
#print(f'Результат: {" ".join(lst)}')

import random

def words_list(count):    
    txt = "абв"
    lst1 = []
    if count <= 0:
        print("Ошибка! Вы ввели отрицательное число.")
        
    for x in range(count):
        random_txt = random.sample(txt, 3) # k = 3
        lst1.append("".join(random_txt))
    return(' '.join(lst1))
     
def new_list(lst1):
    ex = "абв"
    list2 = [item for item in lst1.split() if ex not in item]
    print(" ".join(list2))
    
result = words_list(int(input("Введите длину списка: ")))
print(result) 
print()
print("Список без слов 'абв': ")
print(new_list(result))