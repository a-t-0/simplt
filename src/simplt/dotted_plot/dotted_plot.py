"""File used to create and export plots and tables directly into latex. Can be
used to automatically update your results each time you run latex.

For copy-pastable examples, see:     example_create_a_table()
example_create_multi_line_plot()     example_create_single_line_plot()
at the bottom of this file.
"""
from pprint import pprint
from typing import Any, Dict, List, Optional

import colorsys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import lines
from src.simplt.line_plot.line_plot import set_cmap
from typeguard import typechecked


@typechecked
def example_create_multi_group_dotted_plot(
    output_dir: str, filename: str, extensions: List[str]
) -> None:
    """Example that creates a plot with multiple lines.

    Copy paste it in your own code and modify the values accordingly.
    """
    single_x_series = [3., 5.]
    multiple_y_series:Dict[int,Dict[float,List[float]]] = {}

    # actually fill with data
    multiple_y_series[0]={}
    multiple_y_series[0][single_x_series[0]] = [1., 2., 5.]
    multiple_y_series[0][single_x_series[1]] = [0., 6.]

    multiple_y_series[1]={}
    multiple_y_series[1][single_x_series[0]] = [3., 4.]
    multiple_y_series[1][single_x_series[1]] = [1., 5.]

    
    groupLabels = [
        "first_group",
        "second_group",
    ]  # add a label for each dataseries
    
    print(multiple_y_series)
    plot_multiple_dotted_groups(
        extensions=extensions,
        filename=filename,
        label=groupLabels,
        legendPosition=0,
        output_dir=output_dir,
        x_axis_label="x-axis label [units]",
        y_axis_label="y-axis label [units]",
        y_series=multiple_y_series,
    )


# plot graphs
@typechecked
def plot_multiple_dotted_groups(
    extensions: List[str],
    filename: str,
    label: List,
    legendPosition: int,
    output_dir: str,
    x_axis_label: str,
    y_axis_label: str,
    y_series: Dict[int,Dict[float,List[float]]],
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

    # Generate the colors for the dot groups.
    hsv_values = [(float(x)/len(y_series), 1, 1) for x in range(1,len(y_series)+1)]
    rgb_colour_sets = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_values))



    # Geneterate lines.
    for i, group in enumerate(list(y_series.keys())):
    #for i, x_val in enumerate(list(y_series.keys())):
        for x_val,y_coords_of_x in y_series[group].items():
            print(f'{i},x_val={x_val}')
            print(f'{i},y_coords_of_x={y_coords_of_x}')
            x_vals=[x_val]*len(y_coords_of_x)
            y_vals=y_coords_of_x
            ax.scatter(
                x=x_vals,
                y=y_vals,
                #'r.', # Make it dots instead of lines.
                label=label[i],
                color=rgb_colour_sets[i],
                marker=i+10,

            )

    # configure plot layout
    plt.legend(loc=legendPosition)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    for extension in extensions:
        plt.savefig(f"{output_dir}/{filename}{extension}")
    plt.clf()
    plt.close()

