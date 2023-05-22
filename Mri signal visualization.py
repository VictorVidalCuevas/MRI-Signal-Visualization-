#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:01:54 2023

@author: VictorVidal
"""

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para calcular y actualizar la señal
def update_signal(event=None):
    TR = scale_TR.get()
    TE = scale_TE.get()

    t = np.linspace(0, TR, 10000)
    signal = np.exp(-t / TE)

    ax.clear()
    ax.plot(t, signal, label='Señal', color='steelblue', linewidth=2)
    ax.axhline(y=0.632, color='r', linestyle='--', label='63% decaimiento')
    ax.axvline(x=TE, color='g', linestyle='--', label='TE')
    ax.set_xlabel('Tiempo (ms)', fontsize=12)
    ax.set_ylabel('Señal', fontsize=12)
    ax.set_title('Decaimiento de la señal en función de TR y TE', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)
    canvas.draw()

# Crear la ventana de la interfaz
window = tk.Tk()
window.title('Decaimiento de la Señal')
window.geometry('1200x800')

# Crear perilla deslizante para TR
label_TR = tk.Label(window, text='TR (ms):', font=('Arial', 12))
label_TR.pack()
scale_TR = tk.Scale(window, from_=1, to=10000, resolution=1, orient='horizontal', font=('Arial', 12))
scale_TR.pack()
scale_TR.bind("<ButtonRelease>", update_signal)  # Actualizar señal al soltar el botón del mouse

# Crear perilla deslizante para TE
label_TE = tk.Label(window, text='TE (ms):', font=('Arial', 12))
label_TE.pack()
scale_TE = tk.Scale(window, from_=1, to=2000, resolution=1, orient='horizontal', font=('Arial', 12))
scale_TE.pack()
scale_TE.bind("<ButtonRelease>", update_signal)  # Actualizar señal al soltar el botón del mouse

# Crear la figura y el lienzo para el gráfico
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

# Ejecutar la ventana de la interfaz
window.mainloop()
