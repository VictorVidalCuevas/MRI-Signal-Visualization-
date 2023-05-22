# MRI-Signal-Visualization


The provided code is a Python program that displays a graphical interface for visualizing the signal decay in magnetic resonance imaging based on the TR (Repetition Time) and TE (Echo Time) parameters. It utilizes the Matplotlib library to generate the graph and the Tkinter library to create the interface.

The program features two slider controls that allow modifying the values of TR and TE. As the sliders are moved, the signal updates in real-time on the graph. Additionally, a dashed line is displayed at the point corresponding to 63% signal decay (T2), and another dashed line is shown at the TE value.

The user can adjust the values of TR and TE by dragging the sliders and releasing the mouse button. Upon releasing the mouse button, the program recalculates and displays the signal corresponding to the new TR and TE values on the graph.

The program utilizes the update_signal function to calculate and update the signal based on the TR and TE values. This function is executed both when clicking the "Update" button and when releasing the mouse button after dragging the sliders.

In summary, the code provides an interactive and visually appealing way to explore the signal decay in magnetic resonance imaging by adjusting the TR and TE parameters in real-time.

Please note that this code can be used as a starting point for customization or integration into a larger project
