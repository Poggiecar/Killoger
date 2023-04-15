# Killogger
Este es un pequeño programa en Python que registra todas las teclas presionadas en el teclado y el título de la ventana activa en ese momento. El registro se guarda en un archivo de texto llamado "log.txt" en el directorio donde se encuentra el archivo de código.

<strong>Librerías utilizadas</strong><br>
win32gui: Se utiliza para obtener el título de la ventana activa. <br>
pynput: Se utiliza para detectar las teclas presionadas en el teclado.<br>
datetime: Se utiliza para obtener la fecha y hora actual.<br>
threading: Se utiliza para actualizar el título de la ventana activa cada segundo.<br>
time: Se utiliza para hacer una pausa en el bucle de actualización de la ventana activa.<br>
os: Se utiliza para ocultar el archivo "log.txt" del explorador de archivos.<br>


<strong>Funcionamiento</strong> <br>
El programa funciona de la siguiente manera:
Se inicia un hilo en segundo plano que actualiza constantemente el título de la ventana activa utilizando la función get_current_window().<br>
Se utiliza la función on_press() del módulo pynput para detectar cada tecla presionada en el teclado. Si la tecla es una tecla especial (tabulador, shift, etc.), no se registra en el archivo de registro.<br>
Si la tecla presionada es la tecla de espacio o la tecla Enter, se agrega un salto de línea y se escribe la fecha y hora actual seguida del título de la ventana activa.<br>
Si la tecla presionada es una tecla normal, se escribe la tecla presionada en el registro.<br>
Si se presiona la tecla Esc, se detiene el programa y se cierra el archivo de registro.<br>
El archivo "log.txt" se oculta utilizando el comando os.system("attrib +h log.txt") al inicio del programa para evitar que se modifique accidentalmente, si desea ver el archivo de registro, deberá configurar su explorador de archivos para mostrar archivos ocultos.

<strong>Notas</strong> <br>
Este programa está diseñado para fines educativos y no debe utilizarse para espiar a otros usuarios sin su consentimiento.<br>
El archivo de registro puede volverse bastante grande con el tiempo, por lo que se recomienda borrarlo periódicamente si se va a utilizar continuamente.<br>
