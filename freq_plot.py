import numpy as np
import matplotlib.pyplot as plt

def freq_plot(w,h,figure_name=' '):
#Crtanje amplitudske karakteristike
    plt.figure(figure_name+' Amplitudska karakteristika')
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.ylabel('Amplituda [dB]')
    plt.xlabel('Frekvencija [rad/odmjerku]')
    plt.title('Amplitudska karakteristika')

#Crtanje fazne karakteristike
    plt.figure(figure_name+' fazna karakteristika')
    angles = np.unwrap(np.angle(h))
    plt.plot(w, angles, 'g')
    plt.ylabel('Faza [rad])', color='g')
    plt.xlabel('Frekvencija [rad/odmjerku]')
    plt.title('Fazna karakteristika')   


