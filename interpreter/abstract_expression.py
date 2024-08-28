# An abstract expression by Farseen Ashraf


class AbstractExpression:
    """
    All Terminal and Non-Terminal expressions will implement on
    'interpret' method
    """
    @staticmethod
    def interpret():
        """
        The 'abstract' method gets called recursively
        for each AbstractExpression
        """
