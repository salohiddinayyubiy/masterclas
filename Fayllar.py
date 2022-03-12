# T1
# with open('dars.txt') as fayl:
#     list1 = fayl.read()
# print(list1.split()[-1])

# T2
# filename = "dars.txt"
# count = 0
# with open(filename, 'r') as f:
#     for line in f:
#         count += 1
# print(f"Quidagi fayl {count} qator")

# T3
# with open('dars.txt') as f:
#     a = f.read().split()
# print(max(a, key=len))

# T4
# import shutil
# shutil.copyfile('dars.txt', 'trash.txt')

# T5
# def qosh(list1, list2):
#     list1 = list1[::-1]
#     list2 = list2[::-1]
#     dig = 0
#     numbers = 0
#     for i in range(len(list1)):
#         dig = dig * 10 + list1[i]
#         numbers = numbers * 10 + list2[i]
#     return list(str(dig + numbers)[::-1])
#
#
# list1 = [2, 4, 3]
# list2 = [5, 6, 4]
# print(qosh(list1, list2))

# T6
# def T_not(son):
#     with open(son) as gap:
#         numbers = gap.read().rstrip().split("\n")
#         count = 0
#         for i in range(len(numbers)):
#             if not numbers[i][0] == "T":
#                 count +=1
#     return count
#
#
# num = "dars.txt"
# print(T_not(num))

# T7
# def sana(nma):
#     with open(nma) as salom:
#         a = salom.read().split()
#     return len(a)
#
# mana = "dars.txt"
# print(sana(mana))


# T8
# def sana2(qani):
#     with open(qani) as name:
#         caunt = 0
#         b = name.read().split()
#         for i in b:
#             if i == "is":
#                 caunt +=1
#     return caunt
#
#
# num = "dars.txt"
# print(sana2(num))

# T9
# def sana3(sana):
#     with open(sana) as sun:
#         sanoq = 0
#         son = sun.read().split()
#         for i in son:
#             if len(i) < 5:
#                 sanoq += 1
#     return sanoq
#
#
# numbers = "dars.txt"
# print(sana3(numbers))

# T10
# with open('dars.txt') as num:
#     son = num.read().split()
#     for i in range(len(son)):
#         if son[i][0].isupper():
#             with open('trash.txt', 'a') as dig:
#                 raqam = dig.write(son[i] + '\n')

