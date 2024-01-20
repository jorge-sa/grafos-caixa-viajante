from tkinter import filedialog as fd

def open_file_selection():
    return fd.askopenfile()

#build cities distance matrix
def build_graph_matrix():
    file = open_file_selection()

    dist_matrix = list()
    for item in file:
        dist_matrix.append([float(x) for x in item.split()])
    else:
        dist_matrix.pop()

    return dist_matrix