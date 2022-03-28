from random import randint


def func_2(mas):
    len_mas = len(mas)
    n=0
    res_str = ""
    while n <= len_mas-8:
        s = mas[n:n+8]
        res_str += chr(eval("0b"+s))
        n+=8
    return res_str


def func_1(mas):
    str_res = ""
    for s in mas:
        code = bin(ord(s))
        code = code[2:]
        len_s = len(code)
        if len_s <= 8:
            code = "0"*(8-len_s)+code
        str_res += code
    return str_res


def XOR(mas_1, mas_2):
    len_one = len(mas_1)
    str_res = ""
    for i in range(0, len_one):
        if mas_1[i] == "0" and mas_2[i] == "0":
            str_res+= "0"

        if mas_1[i] == "1" and mas_2[i] == "1":
            str_res+= "0"

        if mas_1[i] == "0" and mas_2[i] == "1":
            str_res+= "1"

        if mas_1[i] == "1" and mas_2[i] == "0":
            str_res+= "1"
    return str_res

word = "Maxim"

if len(word) % 2 != 0:
    word += "/"
len_word = int(len(word)/2)
k=""

for i in range(0, len_word):
    k += chr(randint(65, 90))

L = func_1(word[:len_word])
R = func_1(word[len_word:])
print("R -- ", func_2(R))
K = func_1(k)
F = XOR(L, K)
R_1 = XOR(F, R)
L_1 = R
print("L -- ", func_2(L))
print("R_1 -- ", func_2(R_1))
print("L_1 -- ", func_2(L_1))

print("Было -- ", word)
print("Стало -- ", func_2(L_1)+func_2(R_1))
# расшифровка
F=XOR(L_1, K)
R_2 = XOR(F, R_1)
print(func_2(R_2)+func_2(L_1))
