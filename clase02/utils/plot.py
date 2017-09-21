import matplotlib.pyplot as plt

def graficar(func, rango=(0,100), tipo=float):
    """
    Funcion que utiliza el modulo matplotlib para graficar funciones
    :param func: funcion matematica a graficar
    :param rango: tupla. rango a graficar por defecto (0,100)
    :param tipo: int o float. por defecto float
    :return: None
    """
    r = 100
    # lista por comprension
    x = [i/(r*1.0) for i in range(rango[0], rango[1]*r)]
    print x

    q = [func(tipo(i/(r*1.0))) for i in range(rango[0], rango[1]*r)]
    plt.plot(q)
    plt.show()
