import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Button


def apply_filters(input_image, sharpen_kernel, edge_detection_kernel, emboss_kernel):
    """
    Apply filters to the input image using the given kernels.
    """
    fig, ax = plt.subplots()
    im = ax.imshow(input_image)
    ax.set_xticks([])
    ax.set_yticks([])

    # create button area
    ax_original = plt.axes([0.00, 0.0, 0.15, 0.07])
    ax_edge = plt.axes([0.20, 0.0, 0.20, 0.07])
    ax_emboss = plt.axes([0.45, 0.0, 0.15, 0.07])
    ax_sharpen = plt.axes([0.65, 0.0, 0.15, 0.07])

    button_sharpen = Button(ax_sharpen, 'Sharpen', color='white', hovercolor='gray')
    button_edge = Button(ax_edge, 'Edge Detection', color='white', hovercolor='gray')
    button_emboss = Button(ax_emboss, 'Emboss', color='white', hovercolor='gray')
    button_original = Button(ax_original, 'Original', color='white', hovercolor='gray')

    def on_original_click(event):
        output_image = input_image
        im.set_data(output_image)
        plt.draw()

    def on_sharpen_click(event):
        # Update the plot data
        output_image = cv2.filter2D(input_image, -1, sharpen_kernel)
        im.set_data(output_image)
        # Redraw the plot
        plt.draw()

    def on_edge_click(event):
        output_image = cv2.filter2D(input_image, -1, edge_detection_kernel)
        im.set_data(output_image)
        plt.draw()

    def on_emboss_click(event):
        output_image = cv2.filter2D(input_image, -1, emboss_kernel)
        im.set_data(output_image)
        plt.draw()

    button_sharpen.on_clicked(on_sharpen_click)
    button_edge.on_clicked(on_edge_click)
    button_emboss.on_clicked(on_emboss_click)
    button_original.on_clicked(on_original_click)

    plt.show()


def main():
    try:
        input1 = input("Type name of image(png format, without .png) in this folder: ")
        input_image = cv2.imread(input1 + '.png', 1)
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

        sharpen_kernel = np.array([[-1, -1, -1],
                                   [-1, 9, -1],
                                   [-1, -1, -1]])
        edge_detection_kernel = np.array([[0, 1, 0],
                                          [1, -4, 1],
                                          [0, 1, 0]])
        emboss_kernel = np.array([[-2, -1, 0],
                                  [-1, 1, 1],
                                  [0, 1, 2]])

        apply_filters(input_image, sharpen_kernel, edge_detection_kernel, emboss_kernel)

        print(f'Filters applied to {input1}.png and images displayed!')
    except:
        print("Error: Could not read the image file.")


if __name__ == '__main__':
    main()
