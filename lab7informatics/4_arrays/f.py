'''
Задача №68. Количество элементов больших обоих соседей
Необходимо вывести количество элементов массива, у которых два соседа и которые при этом строго больше обоих своих соседей.
'''
n, cnt = int(input()), 0
a = list(map(int, input().split()))
for i in range(1, n - 1):
    if (a[i] > a[i - 1] and a[i] > a[i + 1]):
        cnt += 1
print(cnt)

