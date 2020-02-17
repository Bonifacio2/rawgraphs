import matplotlib.pyplot as plt


def barchart(data_frame, bottom_data, side_data):
    x_data = data_frame[bottom_data]
    y_data = data_frame[side_data]
    return plt.bar(x_data, y_data)
