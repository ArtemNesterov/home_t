# words = ['Hi', 'Good', 'Dad', 'Hello']
# def my_fanction(str):
#     return str.lower()
#
# def my_fanction1(str):
#     return str.upper()
#
#
# lowered_my = list(map(my_fanction, words))
# uppered_my = list(map(my_fanction1, words))
#
# print(lowered_my)
# print(uppered_my)




# Задание №2
num1 = [4, 6, 7, 5, 2]
def SimpNum(x):
    a = 2 # определяем простое число
    while x % a:
        a += 1 # увеличиваем шаг на 1
    return a == x

def my_sq(num):
    if SimpNum(num):
        return num ** 2 # если простое число
    return num # если не простое

sq_num = list(map(my_sq, num1))
print(sq_num)

