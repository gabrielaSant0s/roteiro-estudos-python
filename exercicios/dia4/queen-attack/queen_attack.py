class Queen:
    def __init__(self, row, column):
        self._row = row
        self._column = column
        self.validate_positions()

    @property
    def row(self):
        return self._row
    
    @property
    def column(self):
        return self._column

    def can_attack(self, another_queen):
        list_positions = []
        for (r,c) in zip (range(self.row-1, -1,-1), range(self.column-1,-1,-1)):
            list_positions.append((r,c))
        for (r,c) in zip (range(self.row+1, 8), range(self.column+1,8)):
            list_positions.append((r,c))
        for (r,c) in zip (range(self.row-1, -1,-1),range(self.column+1,8)):
            list_positions.append((r,c))
        for (r,c) in zip (range(self.row+1, 8), range(self.column-1,-1,-1)):
            list_positions.append((r,c))
        
        position_another_queen = (another_queen.row, another_queen.column)

        if position_another_queen == (self.row, self.column):
            raise ValueError("Invalid queen position: both queens in the same square")
        elif (another_queen.row == self.row):
            return True
        elif (another_queen.column == self.column):
            return True
        elif position_another_queen in list_positions:
            return True
        else:
            return False
    
    def validate_positions(self):
        if self.row < 0:
            raise ValueError("row not positive")
        elif self.column < 0:
            raise ValueError("column not positive")
        elif self.row > 7:
            raise ValueError("row not on board")
        elif self.column > 7:
            raise ValueError("column not on board")
