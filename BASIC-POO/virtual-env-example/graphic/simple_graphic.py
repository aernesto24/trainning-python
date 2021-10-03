"""This is an example to generate a simple graph on Python using Bokeh
Example from Platzi Training"""

from bokeh.plotting import figure, output_file, show

def run():
    output_file('simple_graphic.html')
    fig = figure()

    values_to_graph = int(input('How many values do you want to graph?: '))
    x_vals = list(range(values_to_graph))
    y_vals = []

    for i in x_vals:
        val = int(input('Provide a value for Y correspndent to ' + str(i) + ' :'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_color='red', line_width=2)
    show(fig)


if __name__ == '__main__':
    run()