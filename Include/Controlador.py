from typing import List, Tuple, Callable

from pandas import DataFrame

from GestorDataFrame import GestorDataFrame
from Organizador import Organizador
from Excepciones import TextoColumnaVacia, ColumnaNoOrdenable, DecimalesNoPermitidos


class Controlador:
    METODOS_SIN_DECIMALES = ["Count Sort", "Radix Sort"]

    def __init__(self):
        self.gestor_data_frame: GestorDataFrame = GestorDataFrame()

    def boton_link(self, link_entry: str):
        self.gestor_data_frame.subir_link(link_entry)
        return self.gestor_data_frame.obtener_data_api(), self.gestor_data_frame.columnas_organizables

    def boton_heap(self, columna_entry: str):
        return self.organizar_data("Heap Sort", Organizador.heap_sort, columna_entry)

    def boton_quick(self, columna_entry: str):
        return self.organizar_data("Quick Sort", Organizador.quick_sort, columna_entry)

    def boton_bucket(self, columna_entry: str):
        return self.organizar_data("Bucket Sort", Organizador.bucket_sort, columna_entry)

    def boton_count(self, columna_entry: str):
        return self.organizar_data("Count Sort", Organizador.counting_sort, columna_entry)

    def boton_radix(self, columna_entry: str):
        return self.organizar_data("Radix Sort", Organizador.radix_sort, columna_entry)

    def boton_merge(self, columna_entry: str):
        return self.organizar_data("Merge Sort", Organizador.merge_sort, columna_entry)

    def organizar_data(self, nombre_metodo: str, metodo: Callable, columna_entry: str):
        columna: str = columna_entry.lower()

        if columna == "":
            raise TextoColumnaVacia("ERROR: La columna no fue enviada")

        if columna not in self.gestor_data_frame.columnas_organizables:
            raise ColumnaNoOrdenable("ERROR: La columna ingresada no se puede organizar")

        lista_tuplas: List[Tuple] = self.gestor_data_frame.obtener_data_columna_de_en_tuplas(columna)

        if type(lista_tuplas[0][1]) is float and nombre_metodo in Controlador.METODOS_SIN_DECIMALES:
            raise DecimalesNoPermitidos(f"ERROR: {nombre_metodo} no recibe deciamles")

        tuplas_organizadas, tiempo_ejecucion = Organizador.organizar_data(lista_tuplas, metodo)

        return nombre_metodo, str(tiempo_ejecucion), self.gestor_data_frame.crear_dataframe_organizado(tuplas_organizadas)

