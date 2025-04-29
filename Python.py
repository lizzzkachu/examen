# age = int(input("введите год рождения: "))
# if 1925<=age<1944:
#     print("молчаливое поколение")
# elif 1944<=age<1967:
#     print("поколение бэби-бумеров")
# elif 1967<=age<1984:
#     print("поколение Х")
# elif 1984<=age<2000:
#     print("поколение Y — миллениалы")
# elif 2000<=age<2011:
#     print("поколение Z — зуммеры")
# elif 2011<=age:
#     print("поколение альфа")
# else:
#     print("не верно")


# a = int (input("Введите первое число: "))
# b = int (input("Введите второе число:"))
# for i in range (a + 1,  b):
#     if i % 3 == 0:
#         print (i)

# a = int(input("начало диапазона: "))
# b = int(input("конец диапазона: "))
# if a>b: a, b = b, a
# import random
# c = int (random.randint(a, b))
# count=0
# flag = True
# n = int(input("введите число: "))
# while flag:
#     if c > n:
#         print("заданное число меньше")
#         count += 1
#     elif c < n:
#         print("заданное число больше")
#         count += 1
#     elif c == n:
#         print("вы угадали")
#         count += 1
#     else:
#         print("incorrect")
#         count += 1
#         flag = False
# print("количество попыток: ", count)


n = int(input("введите число"))
print("#" * n)
for i in range(n - 2):
    print("#", " " * (n - 2), "#")
print("#" * n)
