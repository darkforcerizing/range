import csv
with open(r'C:\Users\Ученик\Downloads\students.csv', encoding="utf8") as f:
    r = csv.DictReader(f, delimiter=',', quotechar='"')
    data = sorted(r, key=lambda x: x['titleProject_id'])



idp = input()
while (idp != 'СТОП'):
    idp = int(idp)
    for el in data:
        if int(el['titleProject_id']) == idp:
            surname, name, midname = el["Name"].split()
            print(f"Проект №{idp} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el['score']}.")
    break
else:
    print('Ничего не найдено')
idp = input()
