# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import email.errors
import os
from tkinter import Toplevel, Text
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from typing import Callable, List

from pandas import DataFrame
from pandastable import Table, TableModel
import sys

from Controlador import Controlador

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "build" / "assets" / "frame0"


class Interfaz:

    def __init__(self):
        self.controlador = Controlador()

        self.window = self.contruir_ventana()
        self.canvas = self.construir_canvas()

        self.heap_button = self.construir_boton_heap()
        self.quick_button = self.construir_boton_quick()
        self.bucket_button = self.construir_boton_bucket()
        self.count_button = self.construir_boton_count()
        self.radix_button = self.construir_boton_radix()
        self.merge_button = self.construir_boton_merge()

        self.link_button = self.construir_boton_link()

        self.construir_imagenes()
        self.construir_texto()

        self.link_entry = self.construir_link_entry()
        self.columna_entry = self.construir_columna_entry()

        self.window.resizable(False, False)
        self.window.mainloop()

    @staticmethod
    def relative_to_assets(path: str) -> str:
        return os.path.join(ASSETS_PATH, path)

    @staticmethod
    def mostrar_datos_sin_organizar(data: DataFrame):
        new_window = Toplevel()
        new_window.title("Datos en Link")
        new_window.geometry('1200x1000')
        f = Frame(new_window)
        f.pack(fill=BOTH, expand=1)
        table = pt = Table(f, dataframe=data, showtoolbar=True, showstatusbar=True)
        pt.show()

    @staticmethod
    def mostrar_columnas_organizables(columnas: List[str]):
        # Obtiene el DataFrame como una cadena
        df_str = str(columnas)

        # Crea una nueva ventana
        new_window = Toplevel()
        new_window.title("Columnas Organizables")

        # Crea un widget Text y añade el DataFrame
        text_widget = Text(new_window)
        text_widget.insert("end", df_str)
        text_widget.pack()

    @staticmethod
    def mostrar_datos_organizados(nombre_metodo: str, tiempo_ejecucion: str, data: DataFrame):
        new_window = Toplevel()
        new_window.title(f"Método {nombre_metodo} ({tiempo_ejecucion} segundos)")
        new_window.geometry('1200x1200')
        f = Frame(new_window)
        f.pack(fill=BOTH, expand=1)
        table = pt = Table(f, dataframe=data, showtoolbar=True, showstatusbar=True)
        pt.show()

    @staticmethod
    def color_negative_red(val):
        """
        Takes a scalar and returns a string with
        the css property `'color: red'` for negative
        strings, black otherwise.
        """
        color = 'blue' if val > 90 else 'black'
        return 'color: % s' % color

    @staticmethod
    def contruir_ventana():
        window = Tk()

        window.geometry("1080x780")
        window.configure(bg="#FFC7C7")

        return window

    def construir_canvas(self):
        canvas = Canvas(
            self.window,
            bg="#FFC7C7",
            height=780,
            width=1080,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        return canvas

    def construir_boton_heap(self):
        button_image_1 = PhotoImage(
            file=Interfaz.relative_to_assets("button_1.png"))

        Heap_button = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_heap,
            relief="flat"
        )
        Heap_button.place(
            x=695.0,
            y=75.0,
            width=248.0,
            height=98.0
        )

        Heap_button.image = button_image_1

        return Heap_button

    def construir_boton_quick(self):
        button_image_2 = PhotoImage(
            file=Interfaz.relative_to_assets("button_2.png"))

        Quick_button = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_quick,
            relief="flat"
        )
        Quick_button.place(
            x=682.0,
            y=173.0,
            width=275.0,
            height=115.0
        )

        Quick_button.image = button_image_2
        return Quick_button

    def construir_boton_bucket(self):
        button_image_3 = PhotoImage(
            file=Interfaz.relative_to_assets("button_3.png"))

        Bucket_button = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_bucket,
            relief="flat"
        )
        Bucket_button.place(
            x=695.0,
            y=280.0,
            width=248.0,
            height=102.0
        )

        Bucket_button.image = button_image_3
        return Bucket_button

    def construir_boton_count(self):
        button_image_4 = PhotoImage(
            file=Interfaz.relative_to_assets("button_4.png"))

        Count_button = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_count,
            relief="flat"
        )
        Count_button.place(
            x=689.0,
            y=483.0,
            width=244.0,
            height=104.0
        )

        Count_button.image = button_image_4
        return Count_button

    def construir_boton_radix(self):
        button_image_5 = PhotoImage(
            file=Interfaz.relative_to_assets("button_5.png"))

        Radix_button = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_radix,
            relief="flat"
        )
        Radix_button.place(
            x=689.0,
            y=587.0,
            width=259.0,
            height=108.0
        )

        Radix_button.image = button_image_5
        return Radix_button

    def construir_boton_merge(self):
        button_image_7 = PhotoImage(
            file=Interfaz.relative_to_assets("button_7.png"))

        Merge_button = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_merge,
            relief="flat"
        )
        Merge_button.place(
            x=689.0,
            y=377.0,
            width=268.0,
            height=113.0
        )

        Merge_button.image = button_image_7

        return Merge_button

    def construir_boton_link(self):
        button_image = PhotoImage(file=Interfaz.relative_to_assets("button_8.png"))
        Submit_button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_link,
            relief="flat"
        )
        Submit_button.place(x=212.0, y=267.0, width=289.0, height=67.0)

        Submit_button.image = button_image
        return Submit_button

    def construir_imagenes(self):
        self.image_image_1 = PhotoImage(
            file=Interfaz.relative_to_assets("image_1.png"))

        image_1 = self.canvas.create_image(
            117.39537048339844,
            656.2723999023438,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=Interfaz.relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            539.0,
            388.0,
            image=self.image_image_2
        )

    def construir_texto(self):
        self.canvas.create_text(
            200,
            347.5,
            anchor="nw",
            text="Columna a ordenar",
            fill="#7C838A",
            font=("Poppins Medium", 20 * -1)
        )

        self.canvas.create_text(
            194.0,
            186.0,
            anchor="nw",
            text="link con datos\n",
            fill="#7C838A",
            font=("Poppins Medium", 20 * -1)
        )

        self.canvas.create_text(
            216.0,
            147.0,
            anchor="nw",
            text="Ordena un DataFrame de datos",
            fill="#000000",
            font=("Poppins SemiBold", 18 * -1)
        )

    def construir_link_entry(self):
        Link_datos = Entry(
            bd=0,
            bg="#E0E0E0",
            fg="#000716",
            highlightthickness=0
        )
        Link_datos.place(
            x=199.0,
            y=227.0,
            width=325.0,
            height=33.0
        )
        self.entry_image_1 = PhotoImage(
            file=Interfaz.relative_to_assets("entry_1.png"))

        entry_bg_1 = self.canvas.create_image(
            361.5,
            244.5,
            image=self.entry_image_1
        )
        return Link_datos

    def construir_columna_entry(self):
        Analizar_columna = Entry(
            bd=0,
            bg="#E0E0E0",
            fg="#000716",
            highlightthickness=0
        )
        Analizar_columna.place(
            x=199.0,
            y=386.0,
            width=325.0,
            height=33.0
        )
        self.entry_image_2 = PhotoImage(
            file=Interfaz.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            361.0,
            402.0,
            image=self.entry_image_2
        )
        return Analizar_columna

    def boton_heap(self):
        self.catalizador(self.controlador.boton_heap)

    def boton_quick(self):
        self.catalizador(self.controlador.boton_quick)

    def boton_bucket(self):
        self.catalizador(self.controlador.boton_bucket)

    def boton_count(self):
        self.catalizador(self.controlador.boton_count)

    def boton_radix(self):
        self.catalizador(self.controlador.boton_radix)

    def boton_merge(self):
        self.catalizador(self.controlador.boton_merge)

    def catalizador(self, metodo: Callable):
        try:
            nombre_metodo, tiempo_ejecucion, dataframe_organizado = metodo(self.columna_entry.get())
            self.mostrar_datos_organizados(nombre_metodo, tiempo_ejecucion, dataframe_organizado)
        except Exception as e:
            self.ventana_error(e)

    def boton_link(self):
        dataframe_sin_organizar, columnas_organizables = self.controlador.boton_link(self.link_entry.get())
        self.mostrar_datos_sin_organizar(dataframe_sin_organizar)
        self.mostrar_columnas_organizables(columnas_organizables)

    @staticmethod
    def ventana_error(mensaje):
        # Crea una nueva ventana
        new_window = Toplevel()
        new_window.title("Error")

        # Crea un widget Text y añade el resultado
        text_widget = Text(new_window)
        text_widget.insert("end", mensaje)
        text_widget.pack()

    def mostrar_columnas(self):
        pass

    def submit(self):
        pass
