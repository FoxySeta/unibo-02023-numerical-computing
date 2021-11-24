# Università di Bologna
# Corso di laurea in Informatica
# 02023 - Calcolo numerico
# 25/11/2021
# 
# Stefano Volpe #969766
# lab5.py

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, metrics
from scipy import signal
from numpy import fft
from scipy.optimize import minimize

def es0():
    '''
    Esercizio 1
    - Caricare l'immagine camera() dal modulo skimage.data, rinormalizzandola nel
      range.
    - Applicare un blur di tipo gaussiano con deviazione standard il cui
      kernel ha dimensioni utilizzando le funzioni fornite: gaussian_kernel(),
      psf_fft() ed A().
    - Aggiungere rumore di tipo gaussiano, con deviazione standard, usando la
      funzione np.random.normal().
    - Calcolare il Peak Signal Noise Ratio (PSNR) ed il Mean Squared Error (MSE)
      tra l'immagine degradata e l'immagine originale usando le funzioni
      peak_signal_noise_ratio e mean_squared_error disponibili nel modulo
      skimage.metrics.
    '''
    # Crea un kernel Gaussiano di dimensione kernlen e deviazione standard sigma
    def gaussian_kernel(kernlen, sigma):
        x = np.linspace( - (kernlen // 2), kernlen // 2, kernlen)    
        # Kernel gaussiano unidmensionale
        kern1d = np.exp( - 0.5 * (x ** 2 / sigma))
        # Kernel gaussiano bidimensionale
        kern2d = np.outer(kern1d, kern1d)
        # Normalizzazione
        return kern2d / kern2d.sum()

    # Esegui l'fft del kernel K di dimensione d aggiungendo gli zeri necessari 
    # ad arrivare a dimensione shape
    def psf_fft(kern2d, d, shape):
        # Aggiungi zeri
        K_p = np.zeros(shape)
        K_p[:d, :d] = kern2d

        # Sposta elementi
        p = d // 2
        K_pr = np.roll(np.roll(K_p, - p, 0), - p, 1)

        # Esegui FFT
        K_otf = fft.fft2(K_pr)
        return K_otf

    # Moltiplicazione per A
    def A(x, K):
        x = fft.fft2(x)
        return np.real(fft.ifft2(K * x))

    # Moltiplicazione per A trasposta
    def AT(x, K):
        x = fft.fft2(x)
        return np.real(fft.ifft2(np.conj(K) * x))

    # Immagine in floating point con valori tra 0 e 1
    X = data.camera().astype(np.float64) / 255.0
    m, n = X.shape

    # Genera il filtro di blur
    K = # TODO

    # Genera il rumore
    sigma = 0.02
    noise = # TODO

    # Aggiungi blur e rumore
    b = # TODO
    PSNR = # TODO

    # Visualizziamo i risultati
    plt.figure(figsize = (30, 10))

    ax1 = plt.subplot(1, 2, 1)
    ax1.imshow(X, cmap = 'gray', vmin = 0, vmax = 1)
    plt.title('Immagine Originale')

    ax2 = plt.subplot(1, 2, 2)
    ax2.imshow(b, cmap = 'gray', vmin = 0, vmax = 1)
    plt.title(f'Immagine Corrotta (PSNR: {PSNR:.2f})')

    plt.show()
    PSNR = # TODO
    MSE = # TODO
    print('This is the MSE: ', MSE)
    print('This is the PSNR: ', PSNR)

def es1():
    '''
    Esercizio 2
    - Importare la function minimize da scipy.optimize e visualizzarne l'help.
    - Usando la function minimize con il metodo CG minimizzare la funzione
    f: R^n -> R definita come:
        f(x) = \\sum_i_n(x_i - 1)^2
    - Analizzare la struttura restituita in output dalla function minimize.
    '''
    def f(X):
        res = # TODO
        return np.sum(res)

    def df(X):
        res = # TODO
        return res

    x0 = np.array([2, -10])
    res = # TODO

    print(res)
    type(res)
    res.x
