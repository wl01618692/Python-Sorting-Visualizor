import copy
from .data import Data

def insertion_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    for i in range(1, Data.data_count):
        # FRAME OPERATION BEGIN
        frames.append(copy.deepcopy(ds))
        frames[-1][i].set_color('r')
        # FRAME OPERATION END
        for j in range(i, 0, -1):
            if ds[j].value < ds[j-1].value:
                ds[j], ds[j-1] = ds[j-1], ds[j]
                # FRAME OPERATION BEGIN
                frames.append(copy.deepcopy(ds))
                frames[-1][j-1].set_color('r')
                # FRAME OPERATION END
            else:
                break
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
    # FRAME OPERATION END