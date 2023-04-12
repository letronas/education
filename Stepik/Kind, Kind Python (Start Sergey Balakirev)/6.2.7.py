from operator import itemgetter, attrgetter

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

new = [(thing, weight) for thing, weight in things.items()]

# https://docs.python.org/3/howto/sorting.html
new = sorted(new, key=itemgetter(1), reverse=True)


some_weigth = int(input()) * 1000
new_str = ''
for i in new:
    if some_weigth - i[1] >= 0:
        new_str += i[0] + ' '
        some_weigth -= i[1]

print(new_str.strip())
