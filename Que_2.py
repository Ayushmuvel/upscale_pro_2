R = 3
C = 5
def ro_oth_or(temp,i,j,a):
    # change near by orange to rotten one initial to 3
    # then later on it will converted to 2
    if i-1 > -1 :
        if temp[i-1][j] == 1:
            temp[i-1][j] = 3
            a = 1
    if i+1 < R :
        if temp[i+1][j] == 1:
            temp[i+1][j] = 3
            a = 1
    if j-1 > -1 :
        if temp[i][j-1] == 1:
            temp[i][j-1] = 3
            a = 1
    if j+1 < C :
        if temp[i][j+1] == 1:
            temp[i][j+1] = 3
            a = 1

    return temp,a

def ch_roten_or (temp,ca):
    a = 0
    for i in range(len(temp)):
        for j in range(len(temp[1])):
            if temp[i][j] == 2:
                # find a rotten orange
                temp,a = ro_oth_or(temp,i,j,a)

    if a == 0:
        # when no change taken in the matrix
        one = 0
        two = 0
        # count fresh and rotten orange
        for i in range(R):
            for j in range(C):
                if temp[i][j] == 1:
                    one += 1
                if temp[i][j] == 3 or temp[i][j] == 2:
                    two +=1
        # print(one,two)
        return (ca,one,two)
    else :
        # when change take place in oranges
        # change the rotten orange vale 3 to 2 for standard form
        for i in range(R):
            for j in range(C):
                if temp[i][j] == 3:
                    temp[i][j] = 2
        #print(temp)
        # final recall the function for next frames cycle (time frames)
        return ch_roten_or(temp,ca+1)

# Driver function
if __name__ == "__main__":

    v = [[2, 1, 0, 2, 1],
		 [0, 0, 1, 2, 1],
		 [1, 0, 0, 2, 1]]

    res = ch_roten_or(v,0)

    print(f'time farmes: {res[0]}')
    print(f'fresh oranges: {res[1]}')
    print(f'Rotten oranges: {res[2]}')

