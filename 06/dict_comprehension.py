# dictionar = {}
# for num in range(1, 11):
#     dictionar[num] = num * num
#
# print(dictionar)

# ECHIVALENT CU

# dictionar = {num: num * num for num in range(1, 11)}
dictionar = {num: num * num if num % 2 else 0 for num in range(1, 11)}
print(dictionar)