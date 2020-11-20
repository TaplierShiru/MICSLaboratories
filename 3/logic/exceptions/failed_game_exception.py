

class FiledGameException(Exception):
    """
    If Player loose game, throw this marvelous error!

    """

    def __init__(self):
        super(FiledGameException, self).__init__()

