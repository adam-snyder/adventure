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
    def __init__(self):
        Block.__init__(self)

    def code(self):
        return 0

    def draw(self):
        return '   '

