#!/usr/bin/python
import math

boardSize = 8
attemptLimit = 10000
print "Builing a board that is %(boardSize)s x %(boardSize)s" % locals()

rows = range(boardSize)
cols = range(boardSize)
queens = []

def renderBoard(queens):
    for row in rows:
        rowOutput = ""
        for col in cols:
            if boardSize * row + col in queens:
                rowOutput += "[q]"
            else:
                rowOutput += "[ ]"
        print rowOutput

def isPositionValid(queens, position):
    col = position % boardSize
    row = int(math.floor(position / boardSize))

    # Vertical
    for aRow in rows:
        if aRow * boardSize + col in queens:
            return False

    # Horizontal
    for aCol in cols:
        if row * boardSize + aCol in queens:
            return False

    for aRow in rows:
        # Diagonal left to right
        square = aRow * boardSize + aRow - row + col
        if int(math.floor(square / boardSize)) == aRow: # Limit overflow
            if square in queens:
                return False

        # Diagonal right to left
        square = aRow * boardSize + (boardSize - (boardSize - col) - aRow + row)
        if int(math.floor(square / boardSize)) == aRow: # Limit overflow
            if square in queens:
                return False
    return True


def nextValidPosition(queens, start, end):
    squares = range(start, end)
    for square in squares:
        isValid = isPositionValid(queens, square)
        if isValid:
            return square
    return -1

def backTrack(queens):
    highest = max(queens)
    queens.remove(highest)
    nextValid = nextValidPosition(queens, highest+1, boardSize * boardSize - 1)
    if nextValid < 0:
        backTrack(queens)
    else:
        queens.append(nextValid)

attempts = 0
while len(queens) < boardSize and attempts < attemptLimit:
    highest = 0
    if len(queens) > 0:
        highest = max(queens)
    nextValid = nextValidPosition(queens, highest, boardSize * boardSize - 1)
    if nextValid >= 0:
        queens.append(nextValid)
    else:
        backTrack(queens)
    attempts += 1

print "Used %(attempts)s attempts" % locals()
if len(queens) < boardSize:
    print "Didn't manage to place all."
renderBoard(queens)
