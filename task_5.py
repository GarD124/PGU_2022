#5.
#Вводим через запятую список слов. Формируем из этого списка множество..
#Выводим на экран сколько слов в этом списке с просьбой сформировать 2-ой список с таким же количеством символов.
#После этого делаем словарь из этих двух массивов, где 1-й - ключи, 2-ой - значения.
#Выводим этот словарь.

words_list_1 = input("Введите список слов: ").split(",")
words_len = len(words_list_1)
print(f"Список содержит {words_len} слов")

words_list_2 = input(f"Введите второй список состоящий из {words_len} слов: ").split(",")
if words_len != len(words_list_2):
    print("Второй список не соответствывает требованиям длинны")
    exit()

result_dict = dict(zip(words_list_1, words_list_2))
print(f"Итоговый словарь: {result_dict}")