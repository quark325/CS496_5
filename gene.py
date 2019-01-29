import run_game

class Genes():
    def __init__(self, status):
        self.status = status
        self.score = 0
        self.what_score()

    #여기서 score을 확인한다. self.score을 만들면될듯?
    def what_score(self):
        self.score = run_game.run_game(self.status, 0)[0]

    def __eq__(self, other):
        return (
                isinstance(other, type(self)) and
                other.status == self.status and
                other.score == self.score
        )
