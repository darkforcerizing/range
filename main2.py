import csv


with open(r'C:\Users\Ученик\Downloads\students.csv', encoding='utf8') as f:
    r = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    for i in range(len(r)):
        j = i - 1
        k = r[1]
        while float(r[j]['score'] if r[j]['score'] != 'None' else 0) < float(k['score'] if k['score'] != 'None' else 0) and j >= 0:
            r[j+1] = r[j]
            j -= 1

        r[j+1] = k




print('10 класс')
counter = 1
for l in r:
    if '10' in l['class']:
        s, n, p = l['Name'].split()
        print(f'{counter} место: {n[0]}. {s}')
        counter += 1
    if counter == 4:
        break
