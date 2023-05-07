"""File used to create and export plots and tables directly into latex. Can be
used to automatically update your results each time you run latex.

For copy-pastable examples, see:     example_create_a_table()
example_create_multi_line_plot()     example_create_single_line_plot()
at the bottom of this file.
"""
from pprint import pprint
from typing import Any, List, Optional

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

    multiple_y_series = np.zeros((2, 2), dtype=int)
    # actually fill with data
    multiple_y_series[0] = [1, 2]
    groupLabels = [
        "first_group",
        "second_group",
    ]  # add a label for each dataseries
    single_x_series = [3, 5]

    plot_multiple_dotted_groups(
        extensions=extensions,
        filename=filename,
        label=groupLabels,
        legendPosition=0,
        output_dir=output_dir,
        x=single_x_series,
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
    x: List,
    x_axis_label: str,
    y_axis_label: str,
    y_series: np.ndarray,
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
    for i in range(0, len(y_series)):
        ax.plot(
            x,
            y_series[i, :],
            'r.', # Make it dots instead of lines.
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

