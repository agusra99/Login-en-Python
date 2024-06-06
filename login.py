import tkinter as tk
from tkinter import ttk,messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        #ventana principal
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0)

        #configuración de grid
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)

        self._crear_componentes()

        #Definir el método crear_componentes
    def _crear_componentes(self):

        #Usuario
        usuario_etiqueta = tk.Label(self,text='Usuario:')
        usuario_etiqueta.grid(row=0,column=0, sticky=tk.E,padx=5,pady=5)
        self.entrada1 = ttk.Entry(self)
        self.entrada1.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)

        #password
        etiqueta_password = tk.Label(self,text='Password:')
        etiqueta_password.grid(row=1,column=0,sticky=tk.E,padx=5,pady=5)
        self.entrada_password = ttk.Entry(self, show='*')
        self.entrada_password.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)
        
        #botón
        boton1= ttk.Button(self,text='Login',command=self._login)
        boton1.grid(row=3,column=0,columnspan=2)


    def _login(self):
        messagebox.showinfo('Datos Login',
            f'Usuario: {self.entrada1.get()},Password: {self.entrada_password.get()}')

if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()