# DESCRIPTION:
# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

# Making a digital chessboard I think is an interesting way of visualising how loops can work together.

# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

# So chessBoard(6,4) should return an array like this:

# [
#     ["O","X","O","X"],
#     ["X","O","X","O"],
#     ["O","X","O","X"],
#     ["X","O","X","O"],
#     ["O","X","O","X"],
#     ["X","O","X","O"]
# ]
# And chessBoard(3,7) should return this:

# [
#     ["O","X","O","X","O","X","O"],
#     ["X","O","X","O","X","O","X"],
#     ["O","X","O","X","O","X","O"]
# ]
# The white spaces should be represented by an: 'O'

# and the black an: 'X'


def chess_board(rows, columns):
    ans=[]
    for i in range(1,rows+1,1):
        l=[]
        for j in range(i,columns+i,1):
            if j%2!=0:
                l.append('O')
            else:
                l.append('X')
        ans.append(l)
    return ans

@test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(chess_board(1, 1),[["O"]])
        test.assert_equals(chess_board(1, 2),[["O","X"]])
        test.assert_equals(chess_board(2, 1),[["O"],["X"]])
        test.assert_equals(chess_board(2, 2),[["O","X"],["X","O"]])
        test.assert_equals(chess_board(6, 6),[['O','X','O','X','O','X'],['X','O','X','O','X','O'],['O','X','O','X','O','X'],['X','O','X','O','X','O'],['O','X','O','X','O','X'],['X','O','X','O','X','O']])