from numpy import genfromtxt


# read file and store in array
def get_data_array(data_file_name):
    path = "./data/" + data_file_name
    data_array = genfromtxt(path, delimiter=',')

    return data_array


# print(get_data_array("data1.csv"))
