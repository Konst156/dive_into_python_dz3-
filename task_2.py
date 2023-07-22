# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def find_duplicates(lst):
    counts = {}
    duplicates = []

    # Подсчет количества повторений каждого элемента
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Добавление элементов, которые встречаются более одного раза, в новый список
    for num, count in counts.items():
        if count > 1:
            duplicates.append(num)

    return duplicates


lst = [1, 2, 2, 3, 4, 4, 5]
result = find_duplicates(lst)
print(result)