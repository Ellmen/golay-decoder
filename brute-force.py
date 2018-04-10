import itertools

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

def dot(v1, v2):
    num = sum([i * j for i, j in zip(v1, v2)])
    return num % 2

def multiply(mat, r):
    v = []
    for row in mat:
        v.append(dot(row, r))

    return v

#transpose
def t(mat):
    return map(list, zip(*mat))

def multiply_other_way(c, mat):
    return multiply(t(mat), c)
      
def generate_codewords(G):
    num_rows = len(G)
    row_combs = list(itertools.product([0, 1], repeat=num_rows))
    codebook = [];
    
    for comb in row_combs:
      codebook.append(multiply_other_way(comb, G))
    return codebook

golay_codebook = generate_codewords(make_G());

def distance(a, b):
    assert(len(a) == len(b))
    d = 0
    for i in range(len(a)):
        d += (a[i] + b[i]) % 2
    return d
    
def golay_decode(word):
    best_dist = len(word)
    best_codewords = [golay_codebook[0]];
    for cw in golay_codebook:
        d = distance(word, cw)
        if d < best_dist:
            best_codewords = [cw]
            best_dist = d
        elif d == best_dist:
            best_codewords.append(cw)
    if len(best_codewords) == 1:
        return "Decoded to: {}".format(best_codewords[0])
    else:
        return "Rejected; can't decode uniquely"

if __name__ == '__main__':
    r1 = [0,0,0,0, 0,0,0,0, 0,0,1,1, 1,1,1,1, 1,1,0,1, 1,0,0,1]
    r2 = [0,0,1,1, 1,0,0,0, 0,0,0,0, 0,1,0,0, 1,1,0,0, 1,1,1,0]
    r3 = [1,1,1,1, 0,0,0,0, 0,0,0,0, 0,0,1,1, 1,0,1,0, 0,1,1,1]
    r4 = [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,0,0,0, 1,1,1,0]
    for _ in range(1000):
        print golay_decode(r1)
        print golay_decode(r2)
        print golay_decode(r3)
        print golay_decode(r4)
