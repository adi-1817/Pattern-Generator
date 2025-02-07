import logging

logging.basicConfig(level=logging.DEBUG, format = '%(levelname)s: %(message)s')

class PatternGenerator:
    def __init__(self, size):
        if size<=0:
            raise ValueError("Size must be a positive Integer")
        self.size = size

    def square_pattern(self):
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                print('*', end="")
            print()

    # def square_pattern(self):
    #     return '\n'.join(['*' * self.size for _ in range(self.size)])
    
    def triangle_pattern(self):
        return '\n'.join(['*' * i for i in range(1, self.size + 1)])
    
    def inverted_triangle(self):
        return '\n'.join(['*' * i for i in range(self.size, 0, -1)])
    
    def pyramid_pattern(self):
        return '\n'.join([' ' * (self.size - i - 1) + '*' * (2 * i + 1) for i in range(self.size)])
    
    def hollow_square(self):
        pattern = []
        for i in range(self.size):
            row = ''
            for j in range(self.size):
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1:
                    row += '*'
                else:
                    row += ' '
            pattern.append(row)
        return '\n'.join(pattern)
    
    def diamond_pattern(self):
        top = [' ' * (self.size - i - 1) + '*' * (2 * i+1) for i in range(self.size)]
        bottom = [' ' * (self.size - i - 1) + '*' * (2 * i + 1) for i in range(self.size - 2, -1, -1)]
        return '\n'.join(top + bottom)
    
    def get_patterns(self):
        return {
            'Square Pattern': self.square_pattern,
            'Triangle Pattern': self.triangle_pattern,
            'Inverted Triangle': self.inverted_triangle,
            'Pyramid Pattern': self.pyramid_pattern,
            'Hollow Square': self.hollow_square,
            'Diamond Pattern': self.diamond_pattern,
        }







