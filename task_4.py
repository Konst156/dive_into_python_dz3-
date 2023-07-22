# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

def fill_backpack(items, max_weight):
    # Сортировка вещей по массе
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    backpack = []
    total_weight = 0

    # Добавление вещей в рюкзак, пока не превышена максимальная грузоподъемность
    for item in sorted_items:
        if total_weight + item[1] <= max_weight:
            backpack.append(item)
            total_weight += item[1]

    return backpack


# Пример использования функции
items = {
    'спальник': 2,
    'палатка': 4,
    'еда': 3,
    'вода': 1,
    'фонарик': 1,
    'топор': 2
}

max_weight = 8

result = fill_backpack(items.items(), max_weight)
print(result)
