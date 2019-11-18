inp = open("in.txt", 'r')
out = open("out.txt", 'w')

n = int(input()) # считали размер матрицы
a = [[] for i in range(n)] # создали матрицу

for i in range(n):
    a[i] = list(map(int, inp.readline().split())) #считали матрицу

ans = 0
for i in range(n):
    ans += a[i][i]
    for j in range(i + 1, n): # прошлись по элементам выше главной диагонали
        if a[i][j] < 0:
            a[i][j] = -a[i][j] # если текущий элемент отрицательный делаем положительным

for i in range(n):
    for j in range(n):
        out.write(str(a[i][j])) # вывел матрицу полученную
        out.write(' ')
    out.write('\n')
out.write(str(ans))

inp.close()
out.close()
