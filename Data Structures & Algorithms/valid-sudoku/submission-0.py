class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                curBox = (r//3)*3 + (c//3)
                if val in rows[r] or val in cols[c] or val in boxes[curBox]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[curBox].add(val)
        return True 