#20.Определить количество женщин ,
# севших в порту Квинстаун, в возрастном интервале
# медиана  10 лет и сколько из них выжило
import csv

all_women = []
with open('test.csv', newline='') as File:
    mid = []
    reader = csv.reader(File)
    for row in reader:
        mid.append(row[4])
        if row[3] == 'female' and row[10] == 'Q':
            all_women.append([row[0], row[4]])
mid.sort()
if len(mid) % 2 == 0:
    age = (int(mid[len(mid) // 2]) + int(mid[(len(mid) // 2) + 1])) // 2
else:
    age = int(mid[len(mid) // 2])

need_woman = []
survived = 0
for woman in all_women:
    try:
        if age - 10 <= int(woman[1]) <= age + 10:
            need_woman.append(woman)
    except ValueError:
        pass
with open('gender_submission.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        for i in need_woman:
            if row[0] == i[0] and row[1] == '1':
                survived += 1
print('количество женщин, севших в порту Квинстаун, в возрастном интервалемедиана  10 лет: ' + str(len(need_woman)))
print('количество выживших женщин, севших в порту Квинстаун, в возрастном интервалемедиана  10 лет: ' + str(survived))


