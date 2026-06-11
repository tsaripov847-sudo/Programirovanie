word = input("Введите слово: ")

initial_list = list(word)
inverted_list = initial_list[::-1]

if initial_list == inverted_list:
    print("Это палиндром")
else:
    print("Не палиндром")



