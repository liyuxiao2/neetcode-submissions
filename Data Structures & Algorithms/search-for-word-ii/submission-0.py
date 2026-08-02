class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #add all the words to the trie

        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word
    
        res = []
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return 
            
            next_node = node.children[char]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None #make sure we skip dups
            
            board[r][c] = "#"

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            board[r][c] = char
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, self.root)
        
        return res
                
    