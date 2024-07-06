def generate_sequence(limit):
    sequence_list = []
    a, b = 0, 1
    for i in range(limit):
        sequence_list.append(a)
        a, b = b, a + b
    return sequence_list
