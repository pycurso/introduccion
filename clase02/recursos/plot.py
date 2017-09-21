import matplotlib.pyplot as plt

def graficar(func):
    q = [func(i / 1.0) for i in range(100)]
    plt.plot(q)
    plt.show()
