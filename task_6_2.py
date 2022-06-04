# 6. Переделываем задачу номер 3(калькулятор) и номер 5 на функции.

def get_dict(list1, list2):
    return dict(zip(list1, list2))


def compare_lists_len(list1, list2):
    if len(list1) != len(list2):
        return 0
    return 1


words_list_1 = input("Введите список слов: ").split(",")
words_len = len(words_list_1)
print(f"Список содержит {words_len} слов")

words_list_2 = input(f"Введите второй список состоящий из {words_len} слов: ").split(",")
if not compare_lists_len(words_list_1, words_list_2):
    print("Размер списков не совпадает")
    exit()

print(f"Итоговый словарь: {get_dict(words_list_1, words_list_2)}")
