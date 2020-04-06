

r_move = [2, 2, -2, -2, 1, 1, -1 -1]
c_move = [1, -1, 1, -1, 2, -2, 2,-2]

class KnightTour(object):
    def __init__(self, start, target, size):
        self.start = start
        self.target = target
        self.size = size

    def knight_move(self):
        pass

    def valid_move(self, i, j):
        if i < self.size and j < self.size and pos[i][j] is False:
            return True
        return False


        
