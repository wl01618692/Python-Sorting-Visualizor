# Sorting Visualizer
There are some python scripts which can visualize several famous sorting algorithms and generate the animations via Matplotlib.  

## Environment Configuring
* Install [Python 3](https://www.python.org/downloads/)
* Install [Matplotlib](https://matplotlib.org/users/installing.html) via pip
## Usage
Under the root directory of the project, run the commands like the following format to call all functions:  
```
python output.py arg1 arg2
```
Details of the three arguments above:  
* There are two posible options as "*arg1*":
    * `play` : Play an animation of a specific sorting algorithm or all algorithms in a new window, as a "figure" to Matplotlib.
    * `save-html` : Save the animation as a HTML page with a sequence of images.
* There are nine posible options as "*arg2*":
    * `all` *(default)* : Show the visualization of all sorting algorithms in the animation.
    * `bubble-sort` : Only show the visualization of bubble sorting algorithm in the animation. The following arguments have similar functions.
    * `comb-sort`
    * `heap-sort`
    * `insertion-sort`
    * `merge-sort`
    * `quick-sort`
    * `selection-sort`
    * `shell-sort`
    * `monkey-sort`
