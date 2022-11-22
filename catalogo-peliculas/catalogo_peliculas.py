import tkinter as tk #importo la libreria de tekinder...
from client.gui_app import Frame, barra_menu

def main(): #funcio principal que va a llamar a la interfas grafica...
    root = tk.Tk() #crea la interfas grafica de tekinder...
    root.title('Info') #cambia el titulo de la ventana por defecto...
    root.iconbitmap('images/csr.ico')
    root.resizable(0,0) #proive el crecimiento de la ventana

    barra_menu(root)
    app = Frame(root = root)
    root.mainloop() #despues de sto no se ejecutara nada mas respecto a la ventana grafica


if __name__ == '__main__': #llamado a la funcion principal del programa
    main()