# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

string = '111112222334445'     
string2 = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'

def code(s):
    output = ''
    count = 1
    currentelem = s[0]
    for i in range(len(s)):
        currentelem = s[i]
        if i == len(s)-1:
            
            output += str(count)
            output += s[i]
            break
        if s[i] == s[i+1]:
            
            count += 1
            continue
        output+=str(count)
        output+=currentelem
        count = 1
    return output
print(code(string))

def decodefornum(s):

    output = ''
    i = 0
    while i <  (len(s)):
        if i == len(s) - 1:
            break
        count = int(s[i])
        elem = s[i+1]
        while int(count) > 0:
            output += elem
            count -= 1
        i += 2
    return output
def decodeforstr(s):
    output = ''
    i = 0
    count = 0
    while i  <  (len(s)):
        if i == len(s) - 1:
            break
        while s[i].isdigit():
             count = str(count)+  str(s[i])
             i+=1
             
        elem = s[i]
        while int(count) > 0:
            int(count)
            output += elem
            count = int(count) -  1
        i += 1
    return output
print(decodefornum(code(string)))

print(decodeforstr(code(string2)))



        
             






