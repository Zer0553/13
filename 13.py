#20.Определить количество женщин ,
# севших в порту Квинстаун, в возрастном интервале
# медиана  10 лет и сколько из них выжило
import csv

all_women = []
with open('titanic.csv', newline='') as File:
    all_ages = []
    reader = csv.reader(File)
    for row in reader:
        all_ages.append(str(row[5]))
        if row[4] == 'female' and row[11] == 'Q':
            all_women.append([row[0], row[5], row[1]])
all_ages.sort()
if len(all_ages) % 2 == 0:
    age = (int(all_ages[len(all_ages) // 2]) + int(all_ages[(len(all_ages) // 2) + 1])) // 2
else:
    age = int(all_ages[len(all_ages) // 2])

need_woman = []
survived = 0
for woman in all_women:
    try:
        if age - 10 <= int(woman[1]) <= age + 10:
            need_woman.append(woman)
            if woman[2] == '1':
                survived += 1
    except ValueError:
        pass
print('количество женщин, севших в порту Квинстаун, в возрастном интервалемедиана  10 лет: ' + str(len(need_woman)))
print('количество выживших женщин, севших в порту Квинстаун, в возрастном интервалемедиана  10 лет: ' + str(survived))


