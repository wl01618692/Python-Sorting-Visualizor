import copy
from .data import Data

def shell_sort(data_set):
    frames = [data_set]
    ds = copy.deepcopy(data_set)

    div = Data.data_count // 2
    while div >= 1:
        for i in range(div):
            # FRAME OPERATION BEGIN
            ds_y = copy.deepcopy(ds)
            for j in range(i, Data.data_count, div):
                ds_y[j].set_color('y')
            # FRAME OPERATION END
            for j in range(i+div, Data.data_count, div):
                # FRAME OPERATION BEGIN
                frames.append(copy.deepcopy(ds_y))
                frames[-1][j].set_color('r')
                # FRAME OPERATION END
                for k in range(j, i, -div):
                    if ds[k].value < ds[k-div].value:      
                        ds[k], ds[k-div] = ds[k-div], ds[k]
                        # FRAME OPERATION BEGIN
                        ds_y[k], ds_y[k-div] = ds_y[k-div], ds_y[k]
                        frames.append(copy.deepcopy(ds_y))
                        frames[-1][k-div].set_color('r')
                        # FRAME OPERATION END
                    else:
                        break
        div //= 2
    frames.append(ds)
    return frames
