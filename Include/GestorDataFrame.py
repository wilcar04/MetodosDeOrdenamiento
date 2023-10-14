import pandas as pd
import json
import requests
from pandas import json_normalize, DataFrame
from typing import List, Tuple, Optional


class GestorDataFrame:
    def __init__(self):
        self._link: str = ""
        self._data: Optional[DataFrame] = None
        self.columnas: List[str] = []
        self.columnas_organizables: List[str] = []

    def subir_link(self, link: str):
        self._link = link
        datos = requests.get(self._link)
        data = json.loads(datos.text)
        self._data = json_normalize(data)
        self.columnas = self.obtener_columnas_de_link()
        self.columnas_organizables = self.obtener_columnas_organizables_de_link()

    def obtener_data_api(self) -> DataFrame:
        return self._data

    def obtener_columnas_de_link(self) -> List[str]:
        return self._data.columns.values.tolist()

    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def obtener_columnas_organizables_de_link(self) -> List[str]:
        columnas_organizables: List[str] = []
        for columna in self.columnas:
            for i in range(10):
                valor: str = self._data[columna].tolist()[i]
                if not GestorDataFrame.is_float(valor):
                    break
            else:
                columnas_organizables.append(columna)
        return columnas_organizables

    def obtener_data_columna_de_en_tuplas(self, columna: str) -> List[Tuple]:
        lista_de_tuplas: List[Tuple] = []
        for index, value in enumerate(self._data[columna].tolist()):
            lista_de_tuplas.append((index, int(value)))
        return lista_de_tuplas

    def crear_lista_de_data_organizada(self, tuplas_organizadas: List[Tuple]) -> List[List]:
        data_organizada: List[List] = []
        for row in tuplas_organizadas:
            data_organizada.append(self._data.iloc[row[0]])

        return data_organizada

    def crear_dataframe_organizado(self, tuplas_organizadas: List[Tuple]) -> DataFrame:
        data_organizada = self.crear_lista_de_data_organizada(tuplas_organizadas)
        return pd.DataFrame(data_organizada, columns=self.columnas)
