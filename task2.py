#2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


#def decoding(txt):
#    number = ''
#    res = ''
#    for i in range(len(txt)):
#        if not txt[i].isalpha():
#            number += txt[i]
#        else:
#            res = res + txt[i] * int(number)
#            number = ''
#    return res


#s = input("Введите текст для кодировки: ")
#print(f"Текст после кодировки: {coding(s)}")
##print(f"Текст после дешифровки: {decoding(coding(s))}")

with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст, необходимый для сжатия: '))
with open('text_words.txt', 'r') as file:
    text = file.readline()
    txt_compress = text.split()

print()
def coding(txt):
    count = 1
    res = ''
    if not txt:
        return ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

txt_compress = coding(text)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compress}')

# Можно вывести результат в консоль

print(f"Текст после кодировки: {coding(text)}")
print(f"Текст после дешифровки: {decoding(coding(text))}")