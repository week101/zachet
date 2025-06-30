def count_dgt(num):
    return {d: str(num).count(d) for d in set(str(num))}

number = 23434234232313123124
print(count_dgt(number))