from Point import *
from Data import *
import numpy
from random import uniform
import matplotlib.pyplot as plt


# find min and max coordinates to generate random center in C_means_algorithm
def find_min_max_coordinate_in_dataset(dataset):
    coordinate_len = len(dataset[0])

    coordinates = []  # x, y, z, ...
    for l in range(coordinate_len):
        coordinates.append(dataset[:, l])

    min_max_in_coordinates = []
    for i in range(len(coordinates)):
        min_max_in_coordinates.append((numpy.min(coordinates[i]), numpy.max(coordinates[i])))

    if coordinate_len == 2:
        min_coordinates = (min_max_in_coordinates[0][0], min_max_in_coordinates[1][0])
        max_coordinates = (min_max_in_coordinates[0][1], min_max_in_coordinates[1][1])
    elif coordinate_len == 3:
        min_coordinates = (min_max_in_coordinates[0][0], min_max_in_coordinates[1][0], min_max_in_coordinates[2][0])
        max_coordinates = (min_max_in_coordinates[0][1], min_max_in_coordinates[1][1], min_max_in_coordinates[2][1])
    elif coordinate_len == 4:
        min_coordinates = (min_max_in_coordinates[0][0], min_max_in_coordinates[1][0], min_max_in_coordinates[2][0],
                           min_max_in_coordinates[3][0])
        max_coordinates = (min_max_in_coordinates[0][1], min_max_in_coordinates[1][1], min_max_in_coordinates[2][1],
                           min_max_in_coordinates[3][1])

    return min_coordinates, max_coordinates


# generate random center for each k cluster
def generate_random_center(min_coordinate, max_coordinate, k):
    random_center_arr = []
    coordinate_size = len(min_coordinate)

    for i in range(k):
        if coordinate_size == 2:
            center = (uniform(min_coordinate[0], max_coordinate[0]), uniform(min_coordinate[1], max_coordinate[1]))

        elif coordinate_size == 3:
            center = (uniform(min_coordinate[0], max_coordinate[0]), uniform(min_coordinate[1], max_coordinate[1]),
                      uniform(min_coordinate[2], max_coordinate[2]))

        elif coordinate_size == 4:
            center = (uniform(min_coordinate[0], max_coordinate[0]), uniform(min_coordinate[1], max_coordinate[1]),
                      uniform(min_coordinate[2], max_coordinate[2]), uniform(min_coordinate[3], max_coordinate[3]))

        random_center_arr.append(center)

    return numpy.array(random_center_arr)


def calculate_belonging_rate(coordinate, centers_arr, m):
    number_of_clusters = len(centers_arr)

    belonging_arr = numpy.array([
        [1 / numpy.sum([
            (numpy.linalg.norm(coordinate - centeri) / numpy.linalg.norm(coordinate - centerj)) ** (2 / (m - 1))
            for centerj in centers_arr])
         for centeri in centers_arr]])

    return belonging_arr[0]


# update belonging rate for all points
def update_belonging_rate(points, centers_arr, m):
    for point in points:
        u = calculate_belonging_rate(point.coordinate, centers_arr, m)
        point.prob = u


def update_centers(points, centers_arr, m):
    number_of_clusters = len(centers_arr)
    new_centers_arr = []

    for i in range(number_of_clusters):
        numerator, denominator = 0, 0
        for point in points:
            numerator += (point.prob[i] ** m) * point.coordinate
            denominator += (point.prob[i] ** m)

        new_centers_arr.append(numerator / denominator)

    return new_centers_arr


# calculate error (cost function)
def calculate_cost_function(points, centers_arr, m):
    number_of_clusters = len(centers_arr)
    cost = 0
    for point in points:
        t = numpy.sum(
            [(point.prob[i] ** m) * (numpy.linalg.norm(point.coordinate - centers_arr[i]) ** 2)
             for i in range(number_of_clusters)]
        )
        cost += t

    return cost


# k is number of cluster, n is number of loop
def C_means_algorithm(k, m, n, dataset, points):
    min_coordinate, max_coordinate = find_min_max_coordinate_in_dataset(dataset)
    centers = generate_random_center(min_coordinate, max_coordinate, k)

    cost_function_arr = []
    for i in range(n):
        update_belonging_rate(points, centers, m)
        centers = update_centers(points, centers, m)
        cost_in_this_level = calculate_cost_function(points, centers, m)
        cost_function_arr.append(cost_in_this_level)

    return points, centers, cost_function_arr


# plot cost per C (number of clusters) => to find best k
def plot_cost_per_c_number(m, n, dataset, points, max_c_number, num_dataset):
    cost_per_c_arr = []
    for i in range(1, max_c_number):
        cost_per_c_arr.append(C_means_algorithm(i, m, n, dataset, points)[2][-1])


    plt.plot(numpy.arange(1, max_c_number), cost_per_c_arr)
    plt.title('Errors (cost) per m for dataset' + str(num_dataset))
    plt.xlabel('C (number of clusters)')
    plt.ylabel('Error (cost)')
    plt.show()


# plot cost per M => to find best m
def plot_cost_per_m(k, n, dataset, points, max_m_number, num_dataset):
    cost_per_c_arr = []
    for i in range(2, max_m_number):
        cost_per_c_arr.append(C_means_algorithm(k, i, n, dataset, points)[2][-1])

    plt.plot(numpy.arange(2, max_m_number), cost_per_c_arr)
    plt.title('Errors (cost) per m for dataset' + str(num_dataset))
    plt.xlabel('m (number of m)')
    plt.ylabel('Error (cost)')
    plt.show()


def plot_clusters(k, m, n, dataset, points, num_dataset):
    points, centers, cost_function_arr = C_means_algorithm(k, m, n, dataset, points)
    # print(centers)

    clusters = [[] for i in range(k)]
    for point in points:
        max_prob_index = numpy.argmax(point.prob)
        clusters[max_prob_index].append(point.coordinate)

    for cluster in clusters:
        cluster = numpy.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1])

    centers = numpy.array(centers)
    plt.scatter(centers[:, 0], centers[:, 1], color='black')
    plt.title('Clusters(k:{}, m:{}, dataset{})'.format(k, m, num_dataset))
    plt.show()


def plot_fuzzy_clusters(k, m, n, dataset, points, num_dataset):
    points, centers, cost_function_arr = C_means_algorithm(k, m, n, dataset, points)

    for point in points:
        plt.scatter(point.coordinate[0], point.coordinate[1], c=point.prob)

    centers = numpy.array(centers)
    plt.scatter(centers[:, 0], centers[:, 1], color='black')
    plt.title('Clusters(k:{}, m:{}, dataset{})'.format(k, m, num_dataset))
    plt.show()



if __name__ == "__main__":
    # read data from file and store dataset and points
    dataset1, dataset2, dataset3, dataset4 = get_data_array("data1.csv"), get_data_array("data2.csv"), get_data_array(
        "data3.csv"), get_data_array("data4.csv")

    points_dataset1, points_dataset2, points_dataset3, points_dataset4 = get_all_points("data1.csv"), get_all_points(
        "data2.csv"), get_all_points("data3.csv"), get_all_points("data4.csv")

    # part1 : plot cost per C => to find best k(number of clusters)
    # plot_cost_per_c_number(2, 100, dataset1, points_dataset1, 6, 1)    # k = 3
    # plot_cost_per_c_number(2, 100, dataset2, points_dataset2, 6, 2)    # k = 3 or 4
    # plot_cost_per_c_number(2, 100, dataset3, points_dataset3, 6, 3)    # k = 4 or 3
    # plot_cost_per_c_number(2, 100, dataset4, points_dataset4, 6, 4)    # k = 3

    # part2: (extra point) => find best m for dataset1
    # plot_cost_per_m(3, 100, dataset1, points_dataset1, 10, 1)
    plot_clusters(3, 10, 100, dataset1, points_dataset1, 1)
    plot_fuzzy_clusters(3, 20, 100, dataset1, points_dataset1, 1)
    # plot_cost_per_m(3, 100, dataset2, points_dataset2, 10, 2)
    # plot_cost_per_m(4, 100, dataset3, points_dataset3, 10, 2)
    # plot_cost_per_m(3, 100, dataset4, points_dataset4, 10, 2)

    # part3: plot clusters for dataset 1 and 3(2d)
    # plot_clusters(3, 2, 100, dataset1, points_dataset1, 1)
    # plot_clusters(4, 2, 100, dataset3, points_dataset3, 3)

    # part4: (extra point) => plot clusters for dataset1 and 3 (fuzzy plot)
    # plot_fuzzy_clusters(3, 2, 100, dataset1, points_dataset1, 1)
    # plot_fuzzy_clusters(4, 2, 100, dataset3, points_dataset3, 3)
    # plot_fuzzy_clusters(3, 2, 100, dataset3, points_dataset3, 3)
