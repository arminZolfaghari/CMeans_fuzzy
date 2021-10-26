from Data import *
import numpy


class Point:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.prob = []


def get_all_points(data_file_name):
    data_array = get_data_array(data_file_name)
    points_arr = []
    coordinate_size = len(data_array[0])

    for point in data_array:
        coordinate = numpy.array(point)
        # print(coordinate)
        new_point = Point(coordinate)
        points_arr.append(new_point)

    return points_arr



# s = get_all_points("data1.csv")
# for i in s:
#     print(i.coordinate)
