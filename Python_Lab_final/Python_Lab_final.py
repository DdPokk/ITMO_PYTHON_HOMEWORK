# Алгоритм 5. Вычисление минимакса

Finish = 99999
Max = -9999
Min = 9999

T = int(input('T = '))
while T != Finish:
    if T > Max:
        Max = T
    if T < Min:
        Min = T
    T = int(input('T = '))
print('Max =', Max, 'Min =', Min)


