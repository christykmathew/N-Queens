class N_Queen:
	def __init__(self):
		self.n = int(input("\nEnter value of n: "))
		while(self.n<=3 or self.n>13):
		    print("\nN should be greater than 3 and less than 14")
		    self.n = int(input("\nEnter value of n: "))
	def initialise(self):
	    board_input = []
	    for i in range(0, self.n):
	        temp =[]
	        for j in range(0, self.n):
	            temp.append('-')
	        board_input.append(temp)
	    return board_input

	def check(self,board, i, j):
	    flag = 0    
	    for k in range(0, i):
	        if(board[k][j] == 'Q'):
	            return 1
	    
	    for k in range(1, i+1):
	        if(j+k<self.n and board[i-k][j+k] == 'Q'):
	            return 1
	        

	    for k in range(1, i+1):
	        if(j-k>=0 and board[i-k][j-k] == 'Q'):
	            return 1
	    return 0

	def board_draw(self, list):
	    for rows in list:
	        print(" ".join(rows))
	pass