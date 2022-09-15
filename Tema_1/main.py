my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('Lista initiala:', my_list)

my_list.sort()
print('Lista ordonata ascendent:', my_list)

my_list.reverse()
print('Lista ordonata descendent:', my_list)

my_list.sort()
print('Lista cu numerele pare:', my_list[1::2])
print('Lista cu numerele impare:', my_list[0::2])
print('Lista cu multiplii de 3:', my_list[2::3])


