from pathlib import Path
from analizadorLexico import AnalizadorLexico
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class GUI:
    contenido = ""
    analizador = AnalizadorLexico()
    def relative_to_assets(selfm, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def __init__(self):
        window = Tk()
        window.geometry("955x660")
        window.configure(bg="#FFFFFF")
        canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=660,
            width=955,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            0.0,
            0.0,
            955.0,
            64.0,
            fill="#C4C4C4",
            outline="")
        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        # analizar
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.analizador.analizar(self.contenido),
            relief="flat"
        )
        button_1.place(
            x=119.1319580078125,
            y=64.65231323242188,
            width=119.13199615478516,
            height=64.65232849121094
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))

        # reportes
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=238.26400756835938,
            y=64.65231323242188,
            width=119.13199615478516,
            height=64.65232849121094
        )

        canvas.create_rectangle(
            226.0,
            176.0,
            910.0,
            622.0,
            fill="#E5E5E5",
            outline="")

        canvas.create_rectangle(
            28.0,
            176.0,
            188.0,
            622.0,
            fill="#E5E5E5",
            outline="")

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        # original
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=37.65667724609375,
            y=207.3333740234375,
            width=141.7259979248047,
            height=63.16606521606445
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        # mirrox
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=36.9720458984375,
            y=303.1971130371094,
            width=141.7259979248047,
            height=63.16606521606445
        )

        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        # mirrory
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=36.9720458984375,
            y=399.0609130859375,
            width=141.7259979248047,
            height=63.16606521606445
        )

        canvas.create_text(
            16.0,
            10.0,
            anchor="nw",
            text="Bitxelart",
            fill="#000000",
            font=("Roboto", 48 * -1)
        )

        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        # double mirror
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=35.0,
            y=495.0,
            width=146.71630859375,
            height=63.16606521606445
        )

        button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        # Cargar
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.cargarArchivo(),
            relief="flat"
        )
        button_7.place(
            x=0.0,
            y=64.65231323242188,
            width=119.13199615478516,
            height=64.65232849121094
        )
        window.resizable(False, False)
        window.mainloop()

    def cargarArchivo(self):
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.pxla"), ("todos", "*.*")))
        try:
            archivo = open(nombre_archivo, "r")
            self.contenido += archivo.read()
        except FileNotFoundError:
            print("archivo no encontrado")


gui = GUI()
