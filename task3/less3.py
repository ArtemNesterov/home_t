f1 = open('/home/artem/lesson3_task/answer', 'r')  # чтение
f2 = open('/home/artem/lesson3_task/answer.txt', 'w')  # запись
for line in f1: # чтение построчно
    arr = line.split() # разбиваю на список
    arr = list(map(int, arr))
    # print(arr)
    l = []
    a = ''
    for i in range(1, arr[2] + 1):

        if not i % arr[0]:
            a += 'F'
        if i % arr[1] == 0:
            a += 'B'
        if a == '':
            a += str(i)
        l.append(a)
        a += 'end ='
    #print(a)
    f2.write(a + '\n')
f1.close()
f2.close()