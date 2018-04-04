def make_B():
    rows = []
    rows.append([0] + [1] * 11)
    rows.append([1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0])

    for i in range(10):
        last_row = rows[-1]
        rows.append([1] + last_row[2:] + [last_row[1]])
    
    return rows

def make_I():
    rows = []
    for i in range(12):
        row = [0]*12
        row[i] = 1
        rows.append(row)
    return rows

def make_G():
    I = make_I()
    B = make_B()
    rows = []
    for i in range(12):
        row = I[i] + B[i]
        rows.append(row)
    return rows

def make_H():
    I = make_I()
    B = make_B()
    rows = []
    for i in range(12):
        row = B[i] + I[i]
        rows.append(row)
    return rows

def dot(v1, v2):
    num = sum([i * j for i, j in zip(v1, v2)])
    return num % 2

def multiply(mat, r):
    v = []
    for row in mat:
        v.append(dot(row, r))
    return v

def num_diffs(v):
    B = make_B()
    diffs = []
    for row in B:
        diffs.append(sum([1 if i != j else 0 for i, j in zip(row, v)]))
    return diffs

def weight(v):
    return sum(v)

def flip_bit(b):
    return 0 if b == 1 else 1

def decode(r):
    new_r = r
    golay = make_G()
    s1 = multiply(golay, r)
    if weight(s1) == 0:
        return new_r
    if weight(s1) <= 3:
        for i, b in enumerate(s1):
            if b == 1:
                new_r[i] = flip_bit(new_r[i])
        return new_r
    diffs = num_diffs(s1)
    for i, diff in enumerate(diffs):
        if diff < 3:
            for j, b in enumerate(make_B()[i]):
                if s1[j] != b:
                    new_r[j] = flip_bit(new_r[j])
            new_r[i + 12] = flip_bit(new_r[i + 12])
            return new_r
    golay_T = make_H()
    s2 = multiply(golay_T, r)
    if weight(s2) <= 3:
        for i, b in enumerate(s2):
            if b == 1:
                new_r[i + 12] = flip_bit(new_r[i + 12])
        return new_r
    diffs = num_diffs(s2)
    for i, diff in enumerate(diffs):
        if diff < 3:
            for j, b in enumerate(make_B()[i]):
                if s2[j] != b:
                    new_r[j + 12] = flip_bit(new_r[j + 12])
            new_r[i] = flip_bit(new_r[i])
            return new_r
    return False

if __name__ == '__main__':
    r1 = [0,0,0,0, 0,0,0,0, 0,0,1,1, 1,1,1,1, 1,1,0,1, 1,0,0,1]
    r2 = [0,0,1,1, 1,0,0,0, 0,0,0,0, 0,1,0,0, 1,1,0,0, 1,1,1,0]
    r3 = [1,1,1,1, 0,0,0,0, 0,0,0,0, 0,0,1,1, 1,0,1,0, 0,1,1,1]
    # golay = make_G()
    # s1 = multiply(make_G(), r1)
    print decode(r1)
    print decode(r2)
    print decode(r3)
