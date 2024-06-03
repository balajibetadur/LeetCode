class Solution:


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_hash():
            hash = {}
            for i in range(9):
                hash[str(i+1)] = 0
            return hash
        
        def get_current_matrix(board, row_ind, col_ind):
            row = (row_ind // 3) * 3
            col = (col_ind // 3) * 3
            res = []
            for i in range(3):
                for j in range(3):
                    if (row + i == row_ind and col + j == col_ind) or board[row + i][col + j] == '.': continue
                    res.append(board[row + i][col + j])

            return res
            
        is_valid = True
        for row in range(9):
            row_hash = get_hash()
            col_hash = get_hash()
            for col in range(9):
                if row_hash.get(board[row][col]) and board[row][col] != '.': 
                    return False
                else: row_hash[board[row][col]] = True
                if col_hash.get(board[col][row]) and board[col][row] != '.': 
                    return False
                else: col_hash[board[col][row]] = True
                if board[row][col] in get_current_matrix(board, row, col) and board[row][col] != '.': 
                    return False
        return True