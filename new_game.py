from time import sleep
import os

class GameLayout:
    """
        Tetris PYTHON BLUACK
        * It's cool
        * It's homemade
        * It was ez (haha sike)
    """

    def __init__(
            self, row_num: int = 18, col_num: int = 10, block_slot = '[ ]', empty_slot: str = ' . ',
            borders: list[str] = ['<!', '!>']
            ) -> None:
        
        self.rows = row_num
        self.cols = col_num

        self.slots = {
            'empty': empty_slot,
            'block': block_slot,
            'borders': borders
        }

        self.temp = {}

        self.layout: list[list[str]] = []
        self.layout_str: str = ''

        self.generate()
    

    def generate(self):
        """Generates the game grid (most important function)"""
        # First we make the base grid

        for row_i in range(self.rows):
            self.layout.append([]) # add new row

            for col_i in range(self.cols):
                self.layout[row_i].append(self.slots['empty'])
        
        self.temp['rows_list'] = []

        for i in range(len(self.layout)):
            self.temp['rows_list'].append(f"{self.slots['borders'][0]}{"".join(self.layout[i])}{self.slots['borders'][1]}\n")

        self.layout_str = "".join(self.temp['rows_list'])

        return self.layout_str


    def generate_from(self, leLayout: list[list[str]]):
        self.temp['rows_list'] = []

        for i in range(len(leLayout)):
            self.temp['rows_list'].append(f"{self.slots['borders'][0]}{"".join(leLayout[i])}{self.slots['borders'][1]}\n")

        self.layout_str = "".join(self.temp['rows_list'])

        return self.layout_str

    def get_string_game(self):
        """Just returns the string version of the game"""
        return self.layout_str

    def clear_terminal(self):
        """Clears the terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def clear(self):
        """Clears the Game Grid"""

        self.layout.clear()
        self.layout_str = ''

        for i in range(self.cols):
            self.layout.append(self.slots['empty'])

        for i in range(self.rows):
            self.layout_str += f"{self.slots['borders'][0]}{"".join(self.layout[i])}{self.slots['borders'][1]}\n"

    def set_slot(self, x: int = 0, y: int = 0, type: int = 0):
        """
            * `x`: X pos
            * `y`: Y pos
            * `type`: 0 for empty, 1 for block
        """

        if type == 0:
            self.layout[y][x] = self.slots['empty']
        elif type == 1:
            self.layout[y][x] = self.slots['block']
            self.temp['focused_slot'] = [x, y] # We say that the slot we're focusing on us at those coords


    def move_slot(self, from_pos: list[int], to_pos: list[int]):
        if len(from_pos) != 2 or len(to_pos) != 2:
            print("not enough pos bruh")
            return

        if self.check_slot(from_pos[0], from_pos[1]) and not self.check_slot(to_pos[0], to_pos[1]):
            self.set_slot(from_pos[0], from_pos[1], 0)
            self.set_slot(to_pos[0], to_pos[1], 1)

    def move_smol(self, slot: list[int], x: int, y: int):
        """
            * `slot`: the pos of the slot to move
            * `x` : +1 for right, -1 for left
            * `y` : +1 for down, -1 for up
        """

        self.move_slot(slot, [slot[0] + x, slot[1] + y])
    
    def check_slot(self, x: int, y: int):
        if self.layout[y][x] == self.slots['empty']:
            return False
        elif self.layout[y][x] == self.slots['block']:
            return True

    def show(self, fromLayout: bool = True):
        if not fromLayout:
            print(self.generate())
        print(self.generate_from(self.layout))

    def game_step(self):
        if not 'focused_slot' in self.temp:
            self.set_slot(int(self.cols/2), 0, 1)

        # self.move_slot(self.temp['focused_slot'], [self.temp['focused_slot'][0], self.temp['focused_slot'][1] + 1])
        self.move_smol(self.temp['focused_slot'], 0, 1)
        
        self.show()
        sleep(1)
        self.clear_terminal()


    def __str__(self) -> str:
        return self.generate()


if __name__ == "__main__":
    tetris = GameLayout()

    while True:
        tetris.game_step()
