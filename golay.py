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
    for row in B:
        print row
        print v
        print sum([1 if i != j else 0 for i, j in zip(row, v)])


if __name__ == '__main__':
    r1 = [0,0,0,0, 0,0,0,0, 0,0,1,1, 1,1,1,1, 1,1,0,1, 1,0,0,1]
    r2 = [0,0,1,1, 1,0,0,0, 0,0,0,0, 0,1,0,0, 1,1,0,0, 1,1,1,0]
    r3 = [1,1,1,1, 0,0,0,0, 0,0,0,0, 0,0,1,1, 1,0,1,0, 0,1,1,1]
    s1 = multiply(make_G(), r1)
    print s1
    s2 = multiply(make_H(), r1)
    print s2
     
    # num_diffs(s2)

