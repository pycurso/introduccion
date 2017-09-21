"""
Crear la aplicacion chat que permite comunicarse
con la REST API de chat:
https://pyapi.herokuapp.com/chat

Al iniciar, tiene que preguntar el nombre del usuario.
Despues ejecuta el siguiente bucle:
* imprime los ultimos 2 chats.
* espera un mensaje.
* publica el mensaje usando el usuario y vuelve a
  ejecutar el bucle.

Ejemplo:
python main.py
. Cual es su usuario? martin
. ultimos mensajes:
  >> Mariano[Wed, 20 Sep 2017 14:50:18 GMT] "Hola, hay alguien en el chat?"
  >> Leandro[Wed, 20 Sep 2017 14:52:43 GMT] "Hola, soy Leandro."
. Su mensaje?: Hola, soy martin.
. ultimos mensages:
  >> Leandro[Wed, 20 Sep 2017 14:52:43 GMT] "Hola, soy Leandro."
  >> Martin[Wed, 20 Sep 2017 14:54:23 GMT] "Hola, soy Martin."

Ayuda:
txt = raw_input(mensaje)
    Escribe mensaje y devuelve el string
    escrito en consola.
libreria requests!
"""
