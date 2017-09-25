import logging
import logging.handlers

LOG_LEVEL = {
    "CRITICAL", logging.CRITICAL,
    "ERROR", logging.ERROR,
    "WARNING", logging.WARNING,
    "INFO", logging.INFO,
    "DEBUG", logging.DEBUG,
    "NOTSET", logging.NOTSET,
}


def get_logger(name, level, debug=False):
    """

    :param name: nombre del log. string
    :param level:
    :param debug:
    :return:
    """
    # Definimos el nombre del archivo log
    LOG_FILENAME = name + ".out"
    # establecemos el formato
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    logger = logging.getLogger('%sLogger' % name[:name.find(".")].capitalize())

    # Seteamos el nivel del logger (DEBUG, INFO, ERROR, WARNING...)
    logger.setLevel(LOG_LEVEL[level])

    #Definimos la rotacion de logs y el peso maximo por archivo
    fileHandler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=5, )
    # Seteamos el formato ya declarado
    fileHandler.setFormatter(logFormatter)

    logger.addHandler(fileHandler)

    if debug:
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        logger.addHandler(consoleHandler)
    return logger