import tkinter as tk
import busqueda

class Ventana_basica:
    def __init__(self):
        #Creación de la ventana principal
        self.Ventana1 = tk.Tk()
        self.Ventana1.title("Sistema de cobro")
        self.Ventana1.geometry("300x300")
        
        # Estado de la compra - reemplaza lo que antes eran variables globales
        self.lista_productos = []
        self.precio_final = 0
        self.precio_pendiente = 0   # se usa cuando entras a la fase de pago

        # Variables de Tkinter para leer los Entry
        self.dato_nombre = tk.StringVar()
        self.dato_cantidad = tk.StringVar()
        self.dato_cobro = tk.StringVar()

        #etiquetas
        self.widgets("label", texto="Producto:", x=20, y=20)
        self.widgets("entrada", texto="", x=130, y=20, dato=self.dato_nombre)

        self.widgets("label", texto="Cantidad:", x=20, y=50)
        self.widgets("entrada", texto="", x=130, y=50, dato=self.dato_cantidad)

        self.widgets("boton", texto="Agregar", x=130, y=80,
                      command=self.al_hacer_clic_agregar)

        self.etiqueta_mensaje = tk.Label(self.Ventana1, text="")
        self.etiqueta_mensaje.place(x=20, y=110)

        self.etiqueta_total = tk.Label(self.Ventana1, text="Total: $0.00")
        self.etiqueta_total.place(x=20, y=140)

        self.widgets("label", texto="Cobro:", x=20, y=180)
        self.widgets("entrada", texto="", x=130, y=180, dato=self.dato_cobro)

        self.widgets("boton", texto="Pagar", x=130, y=210,
                      command=self.al_hacer_clic_pagar)

        self.Ventana1.mainloop()

    def widgets(self, widget, texto, x, y, dato=None, command=None):
        match widget:
            case "boton":
                boton = tk.Button(self.Ventana1, text=texto, command=command)
                boton.place(x=x, y=y)
            case "label":
                label = tk.Label(self.Ventana1, text=texto)
                label.place(x=x, y=y)
            case "entrada":
                entrada = tk.Entry(self.Ventana1, textvariable=dato)
                entrada.place(x=x, y=y)

    def al_hacer_clic_agregar(self):
        #Esto lee la variable persistente self.dato_nombre y la asigna a la variable nombre
        nombre = self.dato_nombre.get()
        try:
            #Esto lee lo guardado en la variable self.dato_cantidad y lo conviente a numeros
            cantidad = int(self.dato_cantidad.get())
            #Ademas valida que sean numeros y no letras
        except ValueError:
            self.etiqueta_mensaje.config(text="Cantidad inválida")
            return

        #aqui se hace la llamada a la funcion buscar, convirtiendo self.lista_productos y self.precio_final, ambas variables persistentes
        # en las variables trasformadas tras la función
        self.lista_productos, self.precio_final, mensaje = busqueda.buscar(
            nombre, cantidad, self.lista_productos, self.precio_final
        )
        self.precio_pendiente = self.precio_final   # sincroniza lo que falta por pagar

        self.etiqueta_mensaje.config(text=mensaje)
        self.etiqueta_total.config(text=f"Total: ${self.precio_final:.2f}")

        self.dato_nombre.set("")
        self.dato_cantidad.set("")

    def al_hacer_clic_pagar(self):
        try:
            cobro = float(self.dato_cobro.get())
        except ValueError:
            self.etiqueta_mensaje.config(text="Ingrese un monto válido")
            return

        self.precio_pendiente, mensaje = busqueda.procesar_pago(cobro, self.precio_pendiente)
        self.etiqueta_mensaje.config(text=mensaje)
        self.dato_cobro.set("")


aplicacion = Ventana_basica()