import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# Function takes an m-by-n numpy array and returns True if the
# array is a valid representation of the Game of Life board.
def is_valid_board(ndarray):
    # Check that the board is 2D numpy ndarray
    if ndarray.ndim != 2:
        return False

    # Check that the board is filled with 0.0 or 1.0
    rows = ndarray.shape[0]
    cols = ndarray.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):

            # If a number other than 0.0 or 1.0 is encountered, return false
            if ndarray[i][j] != 0.0:
                if ndarray[i][j] != 1.0:
                    return False

    return True


# Function takes an m-by-n numpy array and returns another
# numpy array that represents the next step of the game
def gol_step(ndarray):
    rows = ndarray.shape[0]
    cols = ndarray.shape[1]
    nextStep = np.empty_like(ndarray)
    nextStep[:] = ndarray

    # Check that the input array is a valid Game of Life board
    if is_valid_board(ndarray):

        # Check the array for Game of Life logic
        for i in range(0, rows):
            for j in range(0, cols):

                # Get the neighbor slice of the array
                neighbors = ndarray.take(range(-1+i, 2+i), mode='wrap', axis=0).take(range(-1+j, 2+j), mode='wrap', axis=1)

                # Determine how many neighboring cells are alive
                liveneighbors = np.count_nonzero(neighbors)
                deadneighbors = len(neighbors) - liveneighbors
                
                # Determine whether the cell being checked is dead or alive
                status = "dead" if ndarray[i,j] == 0 else "alive"

                # Check if cell is dead or alive
                if status == "alive":
                    liveneighbors -= 1       # Adjust for cell currently being examined
                    if liveneighbors < 2:    # Live cell with fewer than 2 live neighbors dies
                        nextStep[i][j] = 0
                    elif liveneighbors > 3:  # Live cell with more than 3 live neighbors dies
                        nextStep[i][j] = 0
                    else:                    # Live cell with 2 or 3 live neighbors remains alive
                        nextStep[i][j] = 1
                else:
                    deadneighbors -=1        # Adjust for cell currently being examined
                    if liveneighbors == 3:   # Dead cell with exactly 3 live neighbors becomes alive
                        nextStep[i][j] = 1

    return nextStep


# Function takes an m-by-n numpy array and draws a GoL
# board corresponding to whether the corresponding cells
# are dead or alive
def draw_gol_board(ndarray):
    cmap = colors.ListedColormap(['white', 'black'])    # Set map colors
    fig, ax = plt.subplots()
    ax.imshow(ndarray, cmap=cmap)
    ax.set_axis_off()
    plt.axis('off')
    plt.show()


# Utility function to create a 100x100 numpy array with all
# cells dead except for the top-left 5x5 section
def create_game_board():
    startboard = np.zeros(shape=(100, 100))
    startboard[1,2] = 1.0
    startboard[2,3] = 1.0
    startboard[3,1] = 1.0
    startboard[3,2] = 1.0
    startboard[3,3] = 1.0
    return startboard


