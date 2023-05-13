
mat = []

# n = int(input('Number of Rows: '))
# for i in range(n):
#     mat.append(list(map(float, input(f'Enter no_of_rows{i+1} elements (Space seperated): ').split())))

f=open('math_input.txt','r')
x = list(map(int,f.readline().split()))
for i in range(x[0]):
    mat.append(list(map(float, f.readline().split())))


def rref(matrix_):
    no_of_rows, no_of_cols,lead = len(matrix_), len(matrix_[0]),0
    
    for r in range(no_of_rows):
        if no_of_cols <= lead:
            return matrix_
        i = r
        while matrix_[i][lead] == 0:
            i += 1
            if no_of_rows == i:
                i,lead = r,lead+1
                if no_of_cols == lead:
                    return matrix_

        matrix_[i], matrix_[r] = matrix_[r], matrix_[i]
        k = matrix_[r][lead]
        mat_r_copy = matrix_[r].copy()
        matrix_[r] = []
        for q in mat_r_copy:
            matrix_[r].append(q/float(k))
            
        for i in range(no_of_rows):
            if i == r:
                ...
            else:
                k = matrix_[i][lead]
                mat_i_copy = matrix_[i].copy()
                matrix_[i] = []
                for l,n in zip(matrix_[r], mat_i_copy):
                    matrix_[i].append(n - k*l)
                matrix_[i] = [round(n,4) for n in matrix_[i]]
            
        lead += 1
        for i in range(len(matrix_)):
            for j in range(len(matrix_[0])):
                matrix_[i][j] = round(matrix_[i][j], 4)
                if matrix_[i][j] == -0.0:
                    matrix_[i][j] = 0.0
                if abs(matrix_[i][j]) <= 0.01:
                    matrix_[i][j] = 0
    return matrix_


def parametric_form(rref_matrix):

    while any(iterable.count(0) == len(rref_matrix[0]) for iterable in rref_matrix):
        rref_matrix.pop(rref_matrix.index([0]*len(rref_matrix[0])))


    free_var = {}
    free_lis = list(range(1,len(rref_matrix[0])+1))
    for i in range(len(rref_matrix)):
        for j in range(len(rref_matrix[0])):
            if rref_matrix[i][j] ==1.0 :
                free_lis.remove(j+1)
                break
    print('Pivot Positions: ',free_lis)
    if len(free_lis)<1:
        print('No Solution')
        exit()
    for i in free_lis:
        free_var[i] = [0 for i in range(len(rref_matrix[0]))]
    
    for j in (free_var.keys()):
        counter = 0
        for k in range(len(rref_matrix)):
            
            if counter+1 in free_lis:
                free_var[j][counter+1] = -rref_matrix[k][j-1]
                counter +=1
            else:
                free_var[j][counter] = -rref_matrix[k][j-1]
            counter+=1

    for i in list(free_var.keys())[::-1]:
        for j in list(free_var.keys())[::-1]:
            if j == i:
                free_var[i][j-1] = 1

            else:
                free_var[i][j-1] = 0

    return free_var


rr = rref(mat)

print('RREF:')
for i in rr:
    print(i,end='\n')

para = parametric_form(rr)
print('x =', end='')
st = ''
for i in para:
    st += f' x{i}{para[i]} +'
print(st[:-2])
