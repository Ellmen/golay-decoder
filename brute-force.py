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

#transpose
def t(mat):
    return map(list, zip(*mat))

def multiply_other_way(c, mat):
    return multiply(t(mat), c)
      
    
def num_diffs(v):
    B = make_B()
    for row in B:
        print row
        print v
        print sum([1 if i != j else 0 for i, j in zip(row, v)])
 
def generate_codewords(G):
    num_rows = len(G)
    row_combs = list(itertools.product([0,1], repeat=num_rows))
    codebook = [];
    
    for comb in row_combs:
      codebook.append(multiply_other_way(comb, G))
    return codebook


if __name__ == '__main__':
    r1 = [0,0,0,0, 0,0,0,0, 0,0,1,1, 1,1,1,1, 1,1,0,1, 1,0,0,1]
    r2 = [0,0,1,1, 1,0,0,0, 0,0,0,0, 0,1,0,0, 1,1,0,0, 1,1,1,0]
    r3 = [1,1,1,1, 0,0,0,0, 0,0,0,0, 0,0,1,1, 1,0,1,0, 0,1,1,1]
    s1 = multiply(make_G(), r1)
    print s1
    s2 = multiply(make_H(), r1)
    print s2
    
    
     
    # num_diffs(s2)
def distance(a, b):
    assert(len(a) == len(b))
    c = []
    for i in range(len(a)):
        c.append((a[i] + b[i])%2)
    return sum(c)
    
golay_codebook = generate_codewords(make_G());

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
        return "Decoded to:", best_codewords[0]
    else:
        return "Rejected; can't decode uniquely"
  
    
print golay_decode([1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,0,0,0, 1,1,1,0])


"""
print(golay_codebook)
a = [[1, 0],[1,1]]
b = [1, 0]
print multiply(a, b)
print multiply_other_way(b, a)
poss = list(itertools.product([0,1], repeat=12))
print poss

print distance([0,0,0,0,1,1],[1,1,1,0,1,1])

matrix = make_G()
codeb =  generate_codewords(matrix)
for i in codeb:
  print i
"""