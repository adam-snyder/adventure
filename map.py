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

    def show(self):
        print(f'{self.width} x {self.height} map')
        for yy in range(self.height):
            line = []
            for xx in range(self.width):
                symbol = self.grid[yy][xx].draw()
                # if yy == y and xx == x:
                #     symbol = ' * '
                line.append(symbol)
            print(' '.join(line))
        print('\n')


if __name__ == '__main__':
    map = Map()
    map.generate()
    map.show()