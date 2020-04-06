# Python3 Program to find all occurrences of the word in
# a matrix
ROW = 3
COL = 5

# check whether given cell (row, col) is a valid
# cell or not.
def is_valid(row, col, prevRow, prevCol):

    # return true if row number and column number
    # is in range
    # return (row >= 0) and (row < ROW) and (col >= 0) and \
    #        (col < COL) and not (row== prevRow and col == prevCol)
    print("prev =", prevRow, prevCol)
    return 0 <= row < ROW and 0 <= col < COL and (row == prevRow or col-prevCol == 1) and not(row == prevRow and col == prevCol)

# These arrays are used to get row and column
# numbers of 8 neighboursof a given cell
rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
colNum = [-1, 0, 1, -1, 1, -1, 0, 1]

dir = [[-1, 0], [1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

# A utility function to do DFS for a 2D boolean
# matrix. It only considers the 8 neighbours as
# adjacent vertices

#       DFS(mat, i, j, -1, -1, word, "", 0, n)
def DFS(mat, row, col, prevRow, prevCol, word, path, index, n):

    # return if current character doesn't match with
    # the next character in the word
    #print("index=", index, n, mat[row][col], word[index])
    #pass for same mat and word
    if (index > n or mat[row][col] != word[index]):
        return
    # append current character position to path
    path += word[index] + "(" + str(row)+ ", " + str(col) + ") "
    #print("path =", path)
    # current character matches with the last character\
    # in the word
    if (index == n):
        print(path)
        print(word, index, n)
        print(row, col)
        return
    # Recur for all connected neighbours
    for k in range(8):
        #print("k=", k)
        if (is_valid(row + rowNum[k], col + colNum[k],prevRow, prevCol)):

            DFS(mat, row + rowNum[k], col + colNum[k],row, col, word, path, index + 1, n)

# The main function to find all occurrences of the
# word in a matrix
def findWords(mat,word):
    # traverse through the all cells of given matrix
    for i in range(ROW):
        for j in range(COL):
            # occurrence of first character in matrix
            if (mat[i][j] == word[0]):
                DFS(mat, i, j, -1, -1, word, "", 0, len(word)-1)
                #DFS(mat, row, col,prevRow, prevCol, word,path, index, n)

# Driver code
mat = [['B', 'N', 'E', 'Y', 'S'],
        ['H', 'E', 'D', 'E', 'S'],
        ['S', 'G', 'N', 'D', 'E']]
word = list("DES")
#print("word= ", word)
findWords(mat, word)
