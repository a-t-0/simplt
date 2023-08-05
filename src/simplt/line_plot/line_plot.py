"""File used to create and export plots and tables directly into latex. Can be
used to automatically update your results each time you run latex.

For copy-pastable examples, see:     example_create_a_table()
example_create_multi_line_plot()     example_create_single_line_plot()
at the bottom of this file.
"""
from ctypes import Union
from typing import Any, List, Optional, Tuple

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import lines
from typeguard import typechecked

# pylint: disable=R0902
# pylint: disable=R0903
class Line:
    """Stores a line that can be plotted.
    """

    # pylint: disable=R0913
    def __init__(
        self,
        x_series: List[float],
        y_series: List[float],
        label:str,
        colour: Optional[str] = None,
    ):
        self.x_series: List[float]=x_series
        self.y_series: List[float]=y_series
        if len(self.x_series) !=len(self.y_series):
            raise ValueError("Error, x and y series should be equal nr of nrs.")
        
        self.label:str=label
        self.colour: Union[None,str]= colour



class X_tick:
    """Stores a line that can be plotted.
    """

    # pylint: disable=R0913
    def __init__(
        self,
        x_pos:float,
        x_pos_label:str,
    ):
        self.x_pos: float=x_pos
        self.x_pos_label:str=x_pos_label

class Window_lim:
    """Stores a line that can be plotted.
    """

    # pylint: disable=R0913
    def __init__(
        self,
        x_min:float,
        x_max:float,
        y_min:float,
        y_max:float,
    ):
        self.x_min:float=x_min
        self.x_max:float=x_max
        self.y_min:float=y_min
        self.y_max:float=y_max
        
@typechecked
def example_create_multi_line_plot(
    output_dir: str, filename: str, extensions: List[str]
) -> None:
    """Example that creates a plot with multiple lines.

    Copy paste it in your own code and modify the values accordingly.
    """

    multiple_y_series = np.zeros((2, 2), dtype=int)
    # actually fill with data
    multiple_y_series[0] = [1, 2]
    lineLabels = [
        "first-line",
        "second_line",
    ]  # add a label for each dataseries
    single_x_series = [3, 5]

    plot_multiple_lines(
        extensions=extensions,
        filename=filename,
        label=lineLabels,
        legendPosition=0,
        output_dir=output_dir,
        x=single_x_series,
        x_axis_label="x-axis label [units]",
        y_axis_label="y-axis label [units]",
        y_series=multiple_y_series,
    )


# plot graphs
@typechecked
def plot_multiple_lines(
    extensions: List[str],
    filename: str,
    legendPosition: int,
    output_dir: str,
    lines: List[Line],
    x_axis_label: str,
    y_axis_label: str,
    window_lim:Window_lim,
    title:Optional[str],
    x_ticks:Optional[List[Tuple[float,float]]],
) -> None:
    """

    :param x:
    :param y_series:
    :param x_axis_label:
    :param y_axis_label:
    :param label:
    :param filename:
    :param legendPosition:
    :param y_series:
    :param filename:
    """
    # pylint: disable=R0913
    # TODO: reduce 9/5 arguments to at most 5/5 arguments.
    fig = plt.figure()
    ax = fig.add_subplot(111)
    if title is not None:
        ax.set_title(title)

    # Set line colours in plot object.
    set_cmap(some_plt=plt, nr_of_colours=len(lines), name="hsv")

    # Generate line types.
    lineTypes = generateLineTypes(list(map(lambda line:line.y_series,lines)))

    # Geneterate lines.
    for i in range(0, len(lines)):
        ax.plot(
            lines[i].x_series,
            lines[i].y_series,
            ls=lineTypes[i],
            label=lines[i].label,
            fillstyle="none",
        )

    plt.xlim(window_lim.x_min,window_lim.x_max)
    plt.ylim(window_lim.y_min,window_lim.y_max)

    # configure plot layout
    plt.legend(loc=legendPosition)
    plt.xlabel(x_axis_label)
    # You can specify a rotation for the tick labels in degrees or with keywords.
    # 0=x position of x-tick, 1=text of xtick.
    plt.xticks(list(map(lambda x_tick:x_tick.x_pos,x_ticks)), list(map(lambda x_tick:x_tick.x_pos_label,x_ticks)), rotation='horizontal')
    plt.ylabel(y_axis_label)
    for extension in extensions:
        plt.savefig(f"{output_dir}/{filename}{extension}")
    plt.clf()
    plt.close()


# Generate random line colours
# Source: https://stackoverflow.com/questions/14720331/
# how-to-generate-random-colors-in-matplotlib
@typechecked
def set_cmap(
    *,
    #some_plt: matplotlib.pyplot,
    some_plt: Any,
    nr_of_colours: int,
    name:str,
) -> None:
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.

    :param n: param name:  (Default value = "hsv")
    :param name: Default value = "hsv")
    """
    some_plt.cm.get_cmap(name, nr_of_colours)


@typechecked
def generateLineTypes(y_series: List) -> List:
    """

    :param y_series:

    """
    # generate varying linetypes
    typeOfLines = list(lines.lineStyles.keys())

    while len(y_series) > len(typeOfLines):
        typeOfLines.append("-.")

    # remove void lines
    for i in range(0, len(y_series)):
        if typeOfLines[i] == "None":
            typeOfLines[i] = "-"
        if typeOfLines[i] == "":
            typeOfLines[i] = ":"
        if typeOfLines[i] == " ":
            typeOfLines[i] = "--"
    return typeOfLines
