from typing import Callable, List, Tuple
import time


class Organizador:
    CANTIDAD_DE_BUCKETS = 10

    @staticmethod
    def organizar_data(lista_tuplas: List[Tuple], metodo: Callable) -> [List[Tuple], int]:
        tuplas_en_buckets: List[List[Tuple]] = Organizador.dividir_en_buckets(lista_tuplas)

        tuplas_organizadas: List[Tuple] = []
        start_time = time.time()
        for bucket in tuplas_en_buckets:
            if len(bucket) == 0:
                continue
            tuplas_organizadas += metodo(bucket)
        tiempo_ejecucion = time.time() - start_time

        return tuplas_organizadas, tiempo_ejecucion

    @staticmethod
    def dividir_en_buckets(lista_tuplas: List[Tuple]) -> List[List[Tuple]]:
        max_lista = Organizador.encontrar_maximo(lista_tuplas)
        min_lista = Organizador.encontrar_minimo(lista_tuplas)

        bucket_rango = (max_lista[1] - min_lista[1]) / (Organizador.CANTIDAD_DE_BUCKETS - 1)

        buckets = [[] for _ in range(Organizador.CANTIDAD_DE_BUCKETS)]

        for i in lista_tuplas:
            index = int((i[1] - min_lista[1]) / bucket_rango)
            if index == Organizador.CANTIDAD_DE_BUCKETS:
                index -= 1
            buckets[index].append(i)

        return buckets

    @staticmethod
    def encontrar_maximo(lista):
        max = lista[0]
        for i in lista:
            if i[1] > max[1]:
                max = i
        return max

    @staticmethod
    def encontrar_minimo(lista):
        min = lista[0]
        for i in lista:
            if i[1] < min[1]:
                min = i
        return min

    @staticmethod
    def Merge(lista_izquierda: List[Tuple], lista_derecha:List[Tuple]):
        lista_resultado = []

        while len(lista_izquierda) > 0 and len(lista_derecha) > 0:
            if lista_izquierda[0][1] < lista_derecha[0][1]:
                lista_resultado.append(lista_izquierda[0])
                lista_izquierda = lista_izquierda[1:]
            else:
                lista_resultado.append(lista_derecha[0])
                lista_derecha = lista_derecha[1:]

        if len(lista_derecha) > 0:
            lista_resultado = lista_resultado + lista_derecha

        if len(lista_izquierda) > 0:
            lista_resultado = lista_resultado + lista_izquierda

        return lista_resultado

    @staticmethod
    def merge_sort(lista_tuplas: List[Tuple]):
        # Caso base
        base = len(lista_tuplas)
        if base <= 1:
            return lista_tuplas

        # Dividir arreglo
        lista_izquierda = lista_tuplas[:len(lista_tuplas) // 2]
        lista_derecha = lista_tuplas[len(lista_tuplas) // 2:]

        lista_izquierda = Organizador.merge_sort(lista_izquierda)
        lista_derecha = Organizador.merge_sort(lista_derecha)

        return Organizador.Merge(lista_izquierda, lista_derecha)

    @staticmethod
    def quick_sort(lista_tuplas: List[Tuple]) -> List[Tuple]:
        # Caso Base
        base = len(lista_tuplas)
        if base <= 1:
            return lista_tuplas

        pivote = lista_tuplas.pop()
        lista_1 = []
        lista_2 = []

        for i in lista_tuplas:
            if i[1] <= pivote[1]:
                lista_1.append(i)
            else:
                lista_2.append(i)

        lista_1 = Organizador.quick_sort(lista_1)
        lista_2 = Organizador.quick_sort(lista_2)

        return lista_1 + [pivote] + lista_2

    @staticmethod
    def heapify(array: List[Tuple], size: int, root_index: int) -> None:
        largest = root_index
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2

        # Verificar si el hijo izquierdo del nodo raíz existe y si es mayor que la raíz
        if left_child < size and array[root_index][1] < array[left_child][1]:
            largest = left_child

        # Verificar si el hijo derecho del nodo raíz existe y si es mayor que la raíz
        if right_child < size and array[largest][1] < array[right_child][1]:
            largest = right_child

        # Cambiar la raíz, si es necesario
        if largest != root_index:
            array[root_index], array[largest] = array[largest], array[root_index]
            Organizador.heapify(array, size, largest)

    @staticmethod
    def heap_sort(lista_tuplas: List[Tuple]) -> List[Tuple]:
        n = len(lista_tuplas)

        # Construir un max heap
        for i in range(n // 2 - 1, -1, -1):
            Organizador.heapify(lista_tuplas, n, i)

        # Extraer los elementos uno por uno
        for i in range(n - 1, 0, -1):
            lista_tuplas[i], lista_tuplas[0] = lista_tuplas[0], lista_tuplas[i]
            Organizador.heapify(lista_tuplas, i, 0)

        return lista_tuplas

    # BONUS: VALORES NEGATIVOS
    @staticmethod
    def counting_sort(lista_tuplas: List[Tuple]):
        min_lista = Organizador.encontrar_minimo(lista_tuplas)
        max_lista = Organizador.encontrar_maximo(lista_tuplas)

        # Ajustar el rango para incluir números negativos ---> representa cuántos números diferentes hay en la lista,
        # incluyendo tanto positivos como negativos. Ejemplo si tenemos la lista [4, 1, 7, 2, 5, 1, 0] lo que hago es
        # buscar el valor maximo y minimo de la lista, en este caso min= 0 y max= 7, los resto y queda 7 y le sumo 1
        # es igual a 8, es decir que hay 8 números diferentes en total posibles numeros diferentes (0,1,2,3,4,5,6,7),
        # estos son los numeros. Tenemos un vector auxiliar que tenga al menos el tamaño del rango más uno para cubrir
        # todos los números posibles. En este caso, necesitamos un vector auxiliar de tamaño 8 para abarcar todos los
        # números del 0 al 7. Calculamos el rango para determinar cuántos elementos debe tener el vector auxiliar.

        rango = max_lista[1] - min_lista[1] + 1
        auxiliar = [0 for _ in range(rango)]
        resultado = [() for _ in range(len(lista_tuplas))]

        for i in lista_tuplas:  # Contar las veces que un elementos aparece en la lista
            auxiliar[i[1] - min_lista[1]] += 1

        for i in range(1, rango):  # Posición Final en el vector
            auxiliar[i] += auxiliar[i - 1]

        for i in range(len(lista_tuplas) - 1, -1, -1):  # Crear lista ordenada
            resultado[auxiliar[lista_tuplas[i][1] - min_lista[1]] - 1] = lista_tuplas[i]
            auxiliar[lista_tuplas[i][1] - min_lista[1]] -= 1

        return resultado

    @staticmethod
    def counting_sort_for_radix(lista_tuplas: List[Tuple], digit_place: int) -> None:
        size = len(lista_tuplas)
        output = [()] * size
        count = [0] * 10

        # Almacenar el conteo de ocurrencias en count[]
        for i in range(size):
            index = lista_tuplas[i][1] // digit_place
            count[index % 10] += 1

        # Cambiar count[i] para que ahora contenga la posición real
        # de este dígito en el array de salida
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Construir el array de salida
        i = size - 1
        while i >= 0:
            index = lista_tuplas[i][1] // digit_place
            output[count[index % 10] - 1] = lista_tuplas[i]
            count[index % 10] -= 1
            i -= 1

        # Copiar el array de salida al array original
        for i in range(size):
            lista_tuplas[i] = output[i]

    @staticmethod
    def radix_sort(lista_tuplas: List[Tuple]) -> List[Tuple]:
        # Encontrar el número máximo para saber el número de dígitos
        max_num = Organizador.encontrar_maximo(lista_tuplas)

        # Hacer un ordenamiento por conteo para cada dígito. Nota que en lugar
        # de pasar el número del dígito, se pasa exp. exp es 10^i
        # donde i es el número del dígito actual
        digit_place = 1
        while max_num[1] // digit_place > 0:
            Organizador.counting_sort_for_radix(lista_tuplas, digit_place)
            digit_place *= 10

        return lista_tuplas

    # BONUS: RECURSIVO
    @staticmethod
    def bucket_sort(lista_tuplas):
        if len(lista_tuplas) == 1:
            return lista_tuplas

        max_lista = Organizador.encontrar_maximo(lista_tuplas)
        min_lista = Organizador.encontrar_minimo(lista_tuplas)

        diferencia = max_lista[1] - min_lista[1]

        if diferencia == 0:
            return lista_tuplas

        bucket_rango = max(1, diferencia // (len(lista_tuplas) - 1))

        buckets = [[] for _ in range(len(lista_tuplas))]

        for i in lista_tuplas:
            if bucket_rango != 0:
                indice = min((i[1] - min_lista[1]) // bucket_rango, len(lista_tuplas) - 1)
            else:
                indice = 0
            buckets[indice].append(i)

        resultado = []
        for bucket in buckets:
            if len(bucket) > 0:
                resultado_bucket = Organizador.bucket_sort(bucket)
                resultado.extend(resultado_bucket)
        return resultado
