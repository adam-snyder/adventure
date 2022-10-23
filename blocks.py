def get_block_type(code):
    if code == 0:
        return EmptyBlock
    elif code == 1:
        return WallBlockH
    elif code == 2:
        return WallBlockV
    elif code == 3:
        return WallBlockQ1
    elif code == 4:
        return WallBlockQ2
    elif code == 5:
        return WallBlockQ3
    elif code == 6:
        return WallBlockQ4


class Block:
    def __init__(self):
        pass

    def encounter(self):
        pass

    def succeed(self):
        pass

    def fail(self):
        pass

    def code(self):
        raise Exception('Must define code()')

    def draw(self):
        raise Exception('Must define draw()')


class EmptyBlock(Block):
    def code(self):
        return 0

    def draw(self):
        return '   '


class WallBlockH(Block):
    def code(self):
        return 1

    def draw(self):
        return ' | '


class WallBlockV(Block):
    def code(self):
        return 2

    def draw(self):
        return '---'


class WallBlockQ1(Block):
    def code(self):
        return 3

    def draw(self):
        return ' |-'


class WallBlockQ2(Block):
    def code(self):
        return 4

    def draw(self):
        return '-| '


class WallBlockQ3(Block):
    def code(self):
        return 5

    def draw(self):
        return '-| '


class WallBlockQ4(Block):
    def code(self):
        return 6

    def draw(self):
        return ' |-'


class ItemBlock(Block):
    def code(self):
        return 100

    def draw(self):
        return ' $ '
