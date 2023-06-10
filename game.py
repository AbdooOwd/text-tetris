""" Original Plain Text Tetris Game By @AbdooOwd inspired by Alexey Pijatnov """

#* All this project was all made without ChatGPT, except for a little bit of the code


class GameLayout:

    """
        The game class for Tetris
        * `row_num` : Number of rows
        * `col_num` : Number of columns
        * `borders` : Index 0 is the right border and 1 is the left one
        * `slots`   : Index 0 is the empty slot and 1 is the block
    """


    def __init__(
        self, row_num:int=18, col_num:int=10,
        borders:list=["<!", "!>"], slots:list=[" . ", "[ ]"]
        ) -> None:

        """`__init__` function for the `GameLayout` class for Tetris"""

        # Row and column number
        self.rows: int = row_num
        self.columns: int = col_num

        # Grid customization
        self.es: str = slots[0]
        self.block: str = slots[1]
        self.borders: list = borders


        #* To edit blocks
        self.block_slots:  list = [ [], [] ]
        self.empty_slots: list = [ [], [] ]
        
        for j in range(self.rows):
            self.empty_slots.append([])
            self.block_slots.append([])
        
        self.isLastBlock : bool = False # To check if the last placed slot is a block

        #! The grid/GAME
        self.layout: str = ""

    def reset_slots(self):
        #* To edit blocks
        self.block_slots:  list = [ [], [] ]
        self.empty_slots: list = [ [], [] ]
        
        self.isLastBlock : bool = False # To check if the last placed slot is a block

    def generate(self):
        """Generates a Game Board/View/Grid"""
        
        print(f" > 'block_slots' : {self.block_slots}") #! DEV
        print(f" > 'empty_slots' : {self.empty_slots}")

        # Column Storing Stuff
        self.column_list: list = []

        for j in range(self.rows):
            self.column_list.append([])
            
            # Check if 'block_slots' and 'empty_slots' have the same positions
            for i in range(self.columns):
                if self.block_slots != [[], []] and self.empty_slots != [[], []] and i <= len(self.block_slots):
                    if i in self.block_slots[j] and i in self.empty_slots[j]:
                        if self.block_slots[j].index(i) == self.empty_slots[j].index(i):
                            if self.isLastBlock == True:
                                self.empty_slots[j].remove(i)
                            else:
                                self.block_slots[j].remove(i)

            for i in range(self.columns): # Every column in a row
                if self.block_slots != [[],[]] and i in self.block_slots[j]:
                    self.column_list[j].append(self.block) # Add block if is a block slot
                    continue

                elif self.empty_slots != [[],[]] and i in self.empty_slots[j]:
                    self.column_list[j].append(self.es) # Add empty slot
                    continue

                self.column_list[j].append(self.es)
        

        self.str_h: list = []

        for i in range(len(self.column_list)):
            self.str_col = "".join(self.column_list[i])
            self.str_h.append(f"{self.borders[0]}{self.str_col}{self.borders[1]}\n")

        self.layout = "".join(self.str_h)

        return self.layout


    def clear(self):
        """
        Clears the Game Grid
        """

        self.column_list.clear()
        self.layout = ''
        self.block_slots = []

        for i in range(self.columns):
            self.column_list.append(self.es)

        self.str_col = "".join(self.column_list)

        for i in range(self.rows):
            self.layout += f"{self.borders[0]}{self.str_col}{self.borders[1]}\n"


    def set_slots(self, where:list=[0, []]):
        """
        Add blocks on column(s)
        * `where` : Index - 0: int for 1 column - 1: list for one or multiple rows
        """

        for i in where[1]: #Checks if already in the Array
            if i in self.block_slots[where[0]]:
                return
        
        self.block_slots[where[0]].extend(where[1])
        self.isLastBlock = True
    
    
    def set_empty(self, where:list=[0,[]]):
        """
        Add blocks on column(s)
        * `where` : Index - 0: int for 1 column - 1: list for one or multiple rows
        """
        
        for i in where[1]:
            if i in self.empty_slots[where[0]]:
                return

        self.empty_slots[where[0]].extend(where[1])
        self.isLastBlock = False


    def add_tetro(self, tetro:int=0, x:int=999):

        """
        Add Tetrominos based on the given value for `tetro`
        * `tetro` : `0`: 2x2 - `1`: 1x4 - `2`: S - `3`: 5 - `4`: T
        * `x` : The X position, by default its the center (columns number / 2 rounded) 
        """

        if x == 999:
            x = round(self.columns / 2)

        match tetro:
            case 0:
                self.set_slots([0, [x, x+1] ])
                self.set_slots([1, [x, x+1] ])

            case 1:
                self.set_slots([0, [x] ])
                self.set_slots([1, [x] ])
                self.set_slots([2, [x] ])
                self.set_slots([3, [x] ])

            case 2:
                self.set_slots([0, [x]])
                self.set_slots([1, [x, x+1]])
                self.set_slots([2, [x+1]])

            case 3:
                self.set_slots([0, [x+1]])
                self.set_slots([1, [x, x+1]])
                self.set_slots([2, [x]])

            case 4:
                self.set_slots([0, [x-1, x, x+1]])
                self.set_slots([1, [x]])
            case _:
                pass


    def move_block(self, slot:list[int]=[0,0], move:list[int]=[0, 0]):
        """
        Move a slot base on the given values
        * `slot` : Indexes -> `0`: X pos - `1`: Y pos
        * `move` : Where to move - Indexes -> `0`: X pos - `1`: Y pos
        """

        for j in range(self.rows):
            for i in range(self.columns):
                if j == slot[1] and i == slot[0]:
                    self.set_empty([j, [i]])

                if j == move[1] and i == move[0]:
                    self.set_slots([j, [i]])


    def move_slots(self): # TODO: Add this
        pass


    def show(self):
        print(self.generate())
    

    def __str__(self) -> str:
        if self.layout == "":
            return self.generate()
        else:
            return self.layout



if __name__ == "__main__":
    tetris = GameLayout(row_num=12, col_num=5)
    
    tetris.add_tetro(0)
    tetris.show()
    
    tetris.set_empty([0,[2]])
    tetris.show()
    
    tetris.set_slots([0, [2]])
    tetris.show()

    # TESTIT: Gravity by taking the slot X pos and Then (Y - 1) Will be below's slot's X

