"""
Utilizando subprocess
 - Crear una funcion, donde en un thread se cosulte los nuevos mensajes en el chat cada 10 seg y guardarlos en una lista
 - Cuando exista un nuevo mensaje imprimir "Mensajes sin leer: (LEN LISTA)"
 - En el thead principal crear un bucle esperando 3 opciones: 1- mostrar mensajes 2- enviar mensaje 3- salir
   mostrar mensajes: ejecuta la funcion get_chat()
   enviar mensaje_ ejecuta la funcion  send_mensaje()
   salir: Termina el programa
"""