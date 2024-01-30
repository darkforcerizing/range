import csv


with open(r'C:\Users\Ученик\Downloads\students.csv', encoding='utf8') as f:
    r = csv.reader(f, delimiter=',')
    ans = list(r)[1:]
    count = {}
    summ = {}
    for id, name, titleProject_id, clas, score in ans:
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")


        count[clas] = count.get(clas, 0) + 1
        summ[clas] = summ.get(clas, 0) + (int(score)if score != 'None' else 0)


    for i in ans:
        if i[-1] == 'None':
            i[-1] = round(summ[i[-2]]/count[i[-2]], 3)

with open('student_new.csv', 'w', newline='') as f1:
    d = csv.writer(f1)
    d.writerow(['id','Name','titleProject_id','class','score'])
    d.writerows(ans)
