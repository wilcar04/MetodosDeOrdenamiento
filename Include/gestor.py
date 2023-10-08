import requests
import json
from pandas import DataFrame
from pandas import json_normalize

from typing import List


class GestorDataFrame:
    def __init__(self, link: str):
        self._LINK: str = link
        datos = requests.get(self._LINK)
        data = json.loads(datos.text)
        self._DATA: DataFrame = json_normalize(data)
        self.columna_objetivo = []

    def obtener_lista_de_columna(self, columna: str) -> List:
        self.columna_objetivo = self._DATA[columna].astype(int).tolist()
        return self.columna_objetivo

    def imprimir_todos_los_datos(self) -> None:
        print(self._DATA)

    def imprimir_datos_de_columna(self, columna: str) -> None:
        print(self._DATA[columna])


"""colombia = GestorDataFrame("https://www.datos.gov.co/resource/9e22-dtq8.json")
# colombia.imprimir_todos_los_datos()
colombia.imprimir_datos_de_columna("mes")"""
