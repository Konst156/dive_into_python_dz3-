# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

from collections import Counter

friends = {
    'Алексей': ('палатка', 'спальник', 'фонарик', 'карта'),
    'Владимир': ('палатка', 'спальник', 'фонарик', 'компас', "карта"),
    'Сергей': ('палатка', 'спальник', 'фонарик', 'карта', 'компас', "нож")
}

# Вещи, взятые всеми тремя друзьями
common_items = set.intersection(*[set(items) for items in friends.values()])

# Уникальные вещи, есть только у одного друга

all_items = set().union(*friends.values())
item_counter = Counter()

for items in friends.values():
    item_counter.update(items)

not_unique_items = set(item for item, count in item_counter.items() if count >= 2)
unique_items = all_items - not_unique_items

# Вещи, есть у всех друзей кроме одного, и имя друга, у которого данная вещь отсутствует
# Для каждой вещи проверяем, у кого она отсутствует
missing_items = {}
for item in all_items:
    for friend, items in friends.items():
        if item not in items:
            if item not in missing_items:
                missing_items[item] = [friend]
            else:
                missing_items[item].append(friend)

# Удаляем вещи, которые отсутствуют у более чем одного друга
missing_items = {item: friends for item, friends in missing_items.items() if len(friends) == 1}

print("Вещи, взятые всеми тремя друзьями:")
print(common_items)

print("Уникальные вещи, есть только у одного друга:")
print(unique_items)

print("Вещи, которые есть у всех друзей кроме одного: ")
print(all_items - missing_items.keys())
print("Имя друга, у которого вещь отсутствует:")
print(f" {missing_items}")

