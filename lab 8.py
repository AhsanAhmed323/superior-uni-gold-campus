class MinMaxGame:
    def _init_(self):
       
        self.board = [0] * 9  

    def is_terminal(self): 
        return False  
    def evaluate(self):
        return 0 

    def get_possible_moves(self):
        return [i for i in range(len(self.board)) if self.board[i] == 0]

    def make_move(self, move, player):
        self.board[move] = player

    def undo_move(self, move):
        self.board[move] = 0

    def display_board(self):
        print(self.board)


def min_max(game, depth, is_maximizing):
    if game.is_terminal():
        return game.evaluate()

    if is_maximizing:
        best_score = float('-inf')
        for move in game.get_possible_moves():
            game.make_move(move, 1)  
            score = min_max(game, depth + 1, False)
            game.undo_move(move)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in game.get_possible_moves():
            game.make_move(move, -1)  
            score = min_max(game, depth + 1, True)
            game.undo_move(move)
            best_score = min(best_score, score)
        return best_score


# Example usage:
if _name_ == "_main_":
    game = MinMaxGame()
    best_move = None
    best_value = float('-inf')

    for move in game.get_possible_moves():
        game.make_move(move, 1) 
        move_value = min_max(game, 0, False)
        game.undo_move(move)
        if move_value > best_value:
            best_value = move_value
            best_move = move

    print(f"Best move is: {best_move} with value {best_value}"