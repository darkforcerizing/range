import csv
import random
import string


def initials(s):
    name = s.split()
    return f'{name[0]}_{name[1][0]}{name[2][0]}'


def password():
    ch = string.ascii_letters + string.digits
    pasword = ''.join(random.choice(ch) for i in range(8))
    return pasword


studepassword = []
with open(r'C:\Users\Ученик\Downloads\students.csv', encoding='utf8') as f:
    r = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    for j in r:
        j['login'] = initials(j['Name'])
        j['password'] = password()
        studepassword.append(j)

with open('student_new1.csv', 'w', newline='', encoding='utf8') as f1:
    a = csv.DictWriter(f1, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    a.writeheader()
    a.writerows(studepassword)

