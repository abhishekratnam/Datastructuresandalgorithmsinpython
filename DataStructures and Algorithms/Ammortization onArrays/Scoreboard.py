class Scoreboard:
    """Fixed -length sequence of high scores in nondecreasing order."""

    def __init__(self,capacity=10):
        """Initialize scoreboard with given max capacity


        All entries are initially None.



        """
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self,k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        score = entry.get_score()
        #Does new entry qualify as a high score?
        #answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            #shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and seld._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry










            
