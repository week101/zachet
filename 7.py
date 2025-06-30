def reverse(s, k):
    result = []
    segment_length = 2 * k

    for segment_start in range(0, len(s), segment_length):
        segment = s[segment_start:segment_start + segment_length]

        if len(segment) < k:
            reversed_part = segment[::-1]
        else:
            reversed_part = segment[:k][::-1] + segment[k:]

        result.append(reversed_part)

    return ''.join(result)


s = "abcdefg"
k = 2
print(reverse(s, k))