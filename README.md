<a href="https://www.python.org/downloads/release/python-383/"><img src="https://img.shields.io/badge/Python-v3.8-blue"></a>

# N-Queens 
The n queens puzzle is the problem of placing n chess queens on an n*n chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. BackTracking is used to solve <i>N-Queen</i> in this solution.

<h2>Working</h2>
The <i>check</i> function is used to check if the queen is safe in a particular position in the <i>n-queens</i> board.

```python
#For Horizontal check
 for k in range(0, i):
        if(board[k][j] == 'Q'):
            return 1
.
.
#For Right Diagonal Check
for k in range(1, i+1):
        if(j+k<n and board[i-k][j+k] == 'Q'):
            return 1
.
.
#For Left Diagonal Check
for k in range(1, i+1):
        if(j-k>=0 and board[i-k][j-k] == 'Q'):
            return 1
```

Also the value of n should be greater than 3 and less than 14. <i>maximum recursion depth exceeded</i> error will be encountered if n > 14 

For more than one solutions of N-Queen(<b><i>might encounter maximum recursion depth exceeded error</i></b>), Uncomment the following line of code.
```python
.
.
# if (row >= n or row < 0):
    #   return
.
.
# print("\n")
# if(board[0].index('Q') < n-1 and row-1 >= 0):
#   n_queen(board, row-1,n)
.
.
```
