with open('input.txt') as fin:
    rows = int(fin.readline())
    matr = [[] for i in range(rows)]
    for i in range(rows):
        matr[i] = [int(t) for t in fin.readline().split()]
    one_ticket = [0] * rows
    two_tickets = [0] * rows
    three_tickets = [0] * rows
    suma = [0] * rows
    for i in range(rows):
        one_ticket[i] = matr[i][0]
        two_tickets[i] = matr[i][1]
        three_tickets[i] = matr[i][2]
    if rows == 1:
        suma[0] = one_ticket[0]
    elif rows == 2:
        suma[1] = min(one_ticket[0] + one_ticket[1], two_tickets[0])
    elif rows == 3:
        suma[2] = min(one_ticket[0] + one_ticket[1] + one_ticket[2], two_tickets[0] + one_ticket[2], two_tickets[1] + one_ticket[0], three_tickets[0])
    elif rows > 3:
        suma[0] = one_ticket[0]
        suma[1] = min(one_ticket[0] + one_ticket[1], two_tickets[0])
        suma[2] = min(one_ticket[0] + one_ticket[1] + one_ticket[2], two_tickets[0] + one_ticket[2],
                      two_tickets[1] + one_ticket[0], three_tickets[0])
        for i in range(3, rows):
            suma[i] = min(suma[i - 1] + one_ticket[i], suma[i - 2] + two_tickets[i - 1], suma[i - 3] + three_tickets[i - 2])
with open('output.txt', 'w') as fout:
    fout.write(str(suma[rows - 1]))


