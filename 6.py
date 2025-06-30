def pascal(rowIndex):
    row = [1]
    for index in range(1, rowIndex+1):
        next_val = row[-1] * (rowIndex - index + 1) // index
        row.append(next_val)
    return row

print(pascal(4))