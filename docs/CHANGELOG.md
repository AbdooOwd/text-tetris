# --Changelog for *Tetris Original Game* --

* Here you will see all the stuff that changed over the time (Format is in DD/MM/YYYY)

## [ 10 / 09 / 2023] - Second *(less non-working)* protoype

### Added
* `move_slots` For multiple slots moving.
* `show` Generates a game layout __and__ prints it.
* **"Terminal Updating"**: Instead of just re-printing the game.
* Some [notes](./notes.md) about the project *(From a dev's POV)*.


## Fixed
* `move_block` Since it just copied the block and didn't delete it's old position.
    * And I made it more *optimized*.


## [ 14 / 05 / 2023 ] - First *(non-working)* prototype

### - Available

* `GameLayout` Class which is the whole game object.
* `generate` Function which is the function that returns the game grid/board using the class.
* `clear` Function which clears the game grid.
