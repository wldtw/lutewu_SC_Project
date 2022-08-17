import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    return (width-GRAPH_MARGIN_SIZE*2) * year_index / (len(YEARS)) + GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # fixed horizontal line low
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # fixed horizontal line high
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for year in YEARS:
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)), 0,
                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)) + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=year, anchor='nw')  # tkinter.NW will do


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    rank_single_height = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK
    color_num = 0
    for name in lookup_names:
        if color_num < 4:
            color_num += 1
        else:
            color_num = 0
        if name in name_data:
            temp_d = name_data[name]
            print(temp_d)
            for i in range(len(YEARS)):
                '''
                require two data to draw line
                number i can not exceed the the max index in the YEARS list
                so i have to set i != len-1
                
                and also
                when it find no data in particular year
                I have to seperate in to 4 parts
                
                any way to write more efficiently?
                '''
                if i != len(YEARS)-1:
                    year = str(YEARS[i])
                    year_plus_1 = str(YEARS[i+1])

                    if year in temp_d and year_plus_1 in temp_d:
                        # line
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           float(temp_d[year]) * rank_single_height+GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i+1])),
                                           float(temp_d[year_plus_1]) * rank_single_height+GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[color_num])

                        # text: name & rank
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           float(temp_d[year]) * rank_single_height+GRAPH_MARGIN_SIZE,
                                           text=f'{name} {temp_d[year]}', anchor='nw', fill=COLORS[color_num])
                    elif year in temp_d and year_plus_1 not in temp_d:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           float(temp_d[year]) * rank_single_height + GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i + 1])),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[color_num])

                        # text: name & rank
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           float(temp_d[year]) * rank_single_height + GRAPH_MARGIN_SIZE,
                                           text=f'{name} {temp_d[year]}', anchor='nw', fill=COLORS[color_num])

                    elif year not in temp_d and year_plus_1 in temp_d:
                        # line
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i + 1])),
                                           float(temp_d[year_plus_1]) * rank_single_height + GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[color_num])

                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=f'{name} *', anchor='sw', fill=COLORS[color_num])
                    else:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i + 1])),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           width=LINE_WIDTH, fill=COLORS[color_num])
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           text=f'{name} *', anchor='sw', fill=COLORS[color_num])
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(YEARS[i])),
                                       float(temp_d[year_plus_1]) * rank_single_height + GRAPH_MARGIN_SIZE,
                                       text=f'{name} {temp_d[year_plus_1]}', anchor='nw', fill=COLORS[color_num])



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
