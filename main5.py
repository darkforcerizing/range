import csv


alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def gh(s):
    d = {l: i for i, l in enumerate(str1, 1)}
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
    p_pow = (p_pow * p) % m
    return int(hash_value)


swh=[]
with open(r'C:\Users\Ученик\Downloads\students.csv', encoding="utf8") as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    for row in reader:
        row['id']=gh(row['Name'])
        print(row)
    swh.append(row)
with open(r'C:\Users\Ученик\Downloads\students_with_hash.csv', 'w', newline='', encoding='utf-8') as f1:
    w = csv.DictWriter(f1, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writeheader()
    w.writerows(swh)
