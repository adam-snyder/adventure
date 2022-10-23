from blocks import get_block_type


class Map:
    grid = []

    def __init__(self):
        self.width = 0
        self.height = 0

    def generate(self):
        rows = ([
            [0, 6, 2, 2, 2, 2, 2, 5, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 6, 2, 5, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 3, 2, 5],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 3, 2, 5, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [6, 4, 0, 3, 2, 5, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 6, 5, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [3, 2, 4, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        ])

        self.grid = []
        for row in rows:
            blocks = []
            for cell in row:
                blocks.append(get_block_type(cell)())
            self.grid.append(blocks)

        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def show(self, x, y):
        print(f'{self.width} x {self.height} map')
        for yy in range(self.height):
            line = []
            for xx in range(self.width):
                symbol = self.grid[yy][xx].draw()
                if yy == y and xx == x:
                    symbol = ' * '
                line.append(symbol)
            print(' '.join(line))
        print('\n')


    def can_i_move(self, x, y):
        print(x, y)
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return self.grid[y][x].code() == 0
        else:
            return False

    def can_i_move_north(self, x, y):
        return self.can_i_move(x, y - 1)

    def can_i_move_south(self, x, y):
        return self.can_i_move(x, y + 1)

    def can_i_move_east(self, x, y):
        return self.can_i_move(x + 1, y)

    def can_i_move_west(self, x, y):
        return self.can_i_move(x - 1, y)


if __name__ == '__main__':
    map = Map()
    map.generate()
    map.show()