from matplotlib import pyplot as plt
from matplotlib import animation
from sorting.data import Data
from sorting.selectionsort import selection_sort
from sorting.bubblesort import bubble_sort
from sorting.insertionsort import insertion_sort
from sorting.shellsort import shell_sort
from sorting.mergesort import merge_sort
from sorting.quicksort import quick_sort
from sorting.heapsort import heap_sort
from sorting.combsort import comb_sort
from sorting.monkeysort import monkey_sort
import random
import os
import sys
import re

stype_dic = {'all': 100,
             'insertion-sort': 0, 'shell-sort': 1, 'selection-sort': 2,
             'merge-sort': 3, 'quick-sort': 4, 'heap-sort': 5,
             'bubble-sort': 6, 'comb-sort': 7}
titles = [r'Insertion Sort', r'Shell Sort', r'Selection Sort',
          r'Merge Sort', r'Quick Sort', r'Heap Sort',
          r'Bubble Sort ', r'Comb Sort', r'Monkey Sort', ]
funs = [insertion_sort, shell_sort, selection_sort,
        merge_sort, quick_sort, heap_sort,
        bubble_sort, comb_sort, monkey_sort]


def draw_all_charts(original_data, frame_interval):
    axs = []
    frames = []
    fig = plt.figure(1, figsize=(16, 9))
    names = []
    max_name_length = 0
    frame_counts = []
    max_frame_length = 0

    data_set = [Data(d) for d in original_data]
    for i in range(9):
        axs.append(fig.add_subplot(331 + i))
        axs[-1].set_xticks([])
        axs[-1].set_yticks([])
    plt.subplots_adjust(0.01, 0.02, 0.99, 0.95, 0.05, 0.15)

    for i in range(8):
        frames.append(funs[i](data_set))
    frames.append(funs[8](data_set, max(len(f) for f in frames)))

    for i in range(9):
        names.append(re.findall(r'\w+ Sort', titles[i])[0] + ':')
        if len(names[-1]) > max_name_length:
            max_name_length = len(names[-1])
        frame_counts.append(len(frames[i]))
        if len(str(frame_counts[-1])) > max_frame_length:
            max_frame_length = len(str(frame_counts[-1]))
    # Output
    for i in range(9):
        print('%-*s %*d frames' % (max_name_length, names[i], max_frame_length, frame_counts[i]))

    def animate(fi):
        bars = []
        for i in range(9):
            if (len(frames[i]) > fi):
                axs[i].cla()
                axs[i].set_title(titles[i])
                axs[i].set_xticks([])
                axs[i].set_yticks([])
                bars += axs[i].bar(list(range(Data.data_count)),  # X
                                   [d.value for d in frames[i][fi]],  # data
                                   1,  # width
                                   color=[d.color for d in frames[i][fi]]  # color
                                   ).get_children()
        return bars

    anim = animation.FuncAnimation(fig, animate, frames=max(len(f) for f in frames), interval=frame_interval)
    return plt, anim


if __name__ == "__main__":
    if len(sys.argv) > 1:
        showtype = 100
        # Check command line argument
        if len(sys.argv) > 2:
            if sys.argv[2] in stype_dic:
                showtype = stype_dic[sys.argv[2]]
            else:
                exit()

        # We want to show all sorting algorithm
        showtype_str = 'all'
        # The dataset if generated with rand
        datatype = 'random'
        dataset = list(range(1, Data.data_count + 1))
        random.shuffle(dataset)

        if sys.argv[1] == 'play':
            frameInterval = 100
            if showtype == 100:
                plt, _ = draw_all_charts(dataset, frameInterval)
            plt.show()

        elif sys.argv[1] == 'save-html':
            filename = "random-dataset-animation"
            fps = 25
            if showtype == 100:
                _, anim = draw_all_charts(dataset, 100)

            # save animation as html form
            anim.save(filename + '.html', writer=animation.HTMLWriter(fps=fps))
            print('The file has been successfully saved in %s' % os.path.abspath(filename + '.html'))
    else:
        exit()
