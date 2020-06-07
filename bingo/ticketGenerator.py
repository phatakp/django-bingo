from random import shuffle


def generate_ticket():
    bingoNumberPool = list(range(1, 91))
    bingoTicket = [[0 for col in range(9)] for row in range(3)]

    while not generated(bingoTicket):
        num = getNextNumber(bingoNumberPool)
        placeOnTicket(num, bingoTicket)
    return bingoTicket


def generated(bingoTicket):
    for row in range(3):
        if rowVacant(row, bingoTicket):
            return False
    return True


def rowVacant(row, bingoTicket):
    return len([bingoTicket[row][col]
                for col in range(9)
                if bingoTicket[row][col] != 0]) < 5


def getNextNumber(bingoNumberPool):
    shuffle(bingoNumberPool)
    return bingoNumberPool.pop()


def placeOnTicket(num, bingoTicket):
    col = getColumn(num)
    row = getRow(col, bingoTicket)
    if row is not None:
        bingoTicket[row][col] = num
        sortColumn(col, bingoTicket)


def getColumn(n):
    if n == 90:
        return 8
    else:
        return n // 10


def getRow(col, bingoTicket):
    for row in range(3):
        if bingoTicket[row][col] == 0 and rowVacant(row, bingoTicket):
            return row
    return None


def sortColumn(col, bingoTicket):
    for i in range(2):
        for j in range(i + 1, 3):
            num1 = bingoTicket[i][col]
            num2 = bingoTicket[j][col]
            if num1 != 0 and num2 != 0:
                if num1 > num2:
                    bingoTicket[i][col] = num2
                    bingoTicket[j][col] = num1
