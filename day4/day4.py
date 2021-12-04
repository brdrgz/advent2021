class Bingo:
	def __init__(self, game_file):
		self.game_file = game_file
		self.load_game()

	def load_game(self):
		self.game_file.seek(0)
		self.drawn_numbers = list(map(lambda s: int(s), self.game_file.readline().rstrip().split(",")))
		self.boards = self.read_boards()

	def read_boards(self):
		self.game_file.seek(0)
		self.game_file.readline()
		boards = []
		line = self.game_file.readline()
		while (line):
			if len(line.strip()) == 0:
				line = self.game_file.readline()
				continue
			board = []
			for _ in range(5):
				board.append(list(map(lambda s: int(s), line.strip().split())))
				line = self.game_file.readline()
			boards.append(board)
			line = self.game_file.readline()
		return boards

	def winning_board(self):
		for number_to_mark in self.drawn_numbers:
			for board_to_mark in self.boards:
				self.mark_board(board_to_mark, number_to_mark)
				if self.is_winner(board_to_mark):
					print((board_to_mark, self.score(board_to_mark, number_to_mark)))
					return

	def last_winning_board(self):
		winners = set()
		last_board = None
		last_number = None
		for number_to_mark in self.drawn_numbers:
			for board_number,board_to_mark in enumerate(self.boards):
				if board_number not in winners:
					self.mark_board(board_to_mark, number_to_mark)
					if self.is_winner(board_to_mark):
						last_number = number_to_mark
						last_board = board_number
						winners.add(board_number)
		print((self.boards[last_board],self.score(self.boards[last_board], last_number)))

	def mark_board(self, board, number):
		for i in range(5):
			for j in range(5):
				if board[i][j] == number:
					board[i][j] = None

	def is_winner(self, board):
		for row in range(5):
			if board[row].count(None) == 5:
				return True
		for col in range(5):
			marks = 0
			for row in range(5):
				if board[row][col] == None:
					marks += 1
			if marks == 5:
				return True
		return False

	def score(self, board, number):
		score = 0
		for i in range(5):
			for j in range(5):
				if board[i][j]:
					score += board[i][j]
		return score * number

	def print_boards(self):
		print(self.boards)

	def print_drawn_numbers(self):
		print(self.drawn_numbers)

game = Bingo(open("day4input.txt", "r"))
#game.print_boards()
#game.print_drawn_numbers()
game.winning_board()
game.last_winning_board()
#game.print_boards()
#game.print_drawn_numbers()