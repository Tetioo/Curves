"""
This module handles task 2 from chapter 4. All the edges of the curves form a perfect Square
"""
import math
import cairo
import logging
from datetime import datetime


WIDTH, HEIGHT = 800, 800
FILE_PATH = 'output_dir/'


def handle_task_two(width: int, height: int, path: str) -> None:
    """
    This function draws the curves in an imaginary Square
    :param path: the directory path to where the file is saved
    :param width: is the width of the Canvas
    :param height: is the height of the Canvas
    :return: None
    """
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(.8, .8, .8)
    context.paint()

    context.rectangle(200, 200, 400, 400)
    context.set_source_rgb(0.8, 0.8, 0.8)
    context.fill()

    context.set_source_rgb(1, 0, 0)
    context.arc(200, 400, 200, (3*math.pi/2), (math.pi/2))
    context.stroke()

    context.set_source_rgb(1, 0, 0)
    context.arc(400, 200, 200, 0, math.pi)
    context.stroke()

    context.set_source_rgb(0, 0, 1)
    context.arc(600, 400, 200, (math.pi / 2), (3*math.pi / 2))
    context.stroke()

    context.set_source_rgb(0, 0, 1)
    context.arc(400, 600, 200, math.pi, 0)
    context.stroke()

    surface.write_to_png(f'{path}curves.png')


if __name__ == '__main__':
    handle_task_two(WIDTH, HEIGHT, FILE_PATH)

    logging.basicConfig(filename=f'{FILE_PATH}code_labs_logging.log', level=logging.INFO)
    logging.info(f'This operation was completed successfully at {datetime.now()}')
