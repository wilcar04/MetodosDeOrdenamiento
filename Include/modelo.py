from typing import List


class Modelo:

    @staticmethod
    def quick(lista):
        # Caso Base
        base = len(lista)
        if base <= 1:
            return lista

        pivote = lista.pop()
        lista1 = []
        lista2 = []

        for i in lista:
            if i <= pivote:
                lista1.append(i)
            else:
                lista2.append(i)

        lista1 = Modelo.quick(lista1)
        lista2 = Modelo.quick(lista2)


        return lista1 + [pivote] + lista2

    @staticmethod
    def bucket_sort(lista: List[int]) -> List[int]:
        max_lista = max(lista)
        min_lista = min(lista)

        rango_cubeta = (max_lista - min_lista) / (len(lista) - 1)

        cubetas = [[] for _ in range(len(lista))]

        for i in lista:
            indice = int((i - min_lista) / rango_cubeta)
            if indice == len(lista):
                indice -= 1
            cubetas[indice].append(i)

        resultado = []
        for cubeta in cubetas:
            cubeta = Modelo.quick(cubeta)
            resultado.extend(cubeta)


        return resultado

    @staticmethod
    def merge(array: List[int], left: int, middle: int, right: int) -> None:
        left_size = middle - left + 1
        right_size = right - middle

        # Crear arrays temporales
        left_array = [0] * left_size
        right_array = [0] * right_size

        # Copiar los datos a los arrays temporales
        for i in range(left_size):
            left_array[i] = array[left + i]

        for j in range(right_size):
            right_array[j] = array[middle + 1 + j]

        # Mezclar los arrays temporales de vuelta al array original
        i = 0
        j = 0
        k = left

        while i < left_size and j < right_size:
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de left_array si hay alguno
        while i < left_size:
            array[k] = left_array[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de right_array si hay alguno
        while j < right_size:
            array[k] = right_array[j]
            j += 1
            k += 1

    @staticmethod
    def merge_sort(array: List[int]) -> List[int]:
        def _merge_sort(array: List[int], left: int, right: int) -> None:
            if left < right:
                middle = left + (right - left) // 2

                _merge_sort(array, left, middle)
                _merge_sort(array, middle + 1, right)
                Modelo.merge(array, left, middle, right)

        _merge_sort(array, 0, len(array) - 1)
        return array

    @staticmethod
    def heapify(array: List[int], size: int, root_index: int) -> None:
        largest = root_index
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2

        # Verificar si el hijo izquierdo del nodo raíz existe y si es mayor que la raíz
        if left_child < size and array[root_index] < array[left_child]:
            largest = left_child

        # Verificar si el hijo derecho del nodo raíz existe y si es mayor que la raíz
        if right_child < size and array[largest] < array[right_child]:
            largest = right_child

        # Cambiar la raíz, si es necesario
        if largest != root_index:
            array[root_index], array[largest] = array[largest], array[root_index]
            Modelo.heapify(array, size, largest)

    @staticmethod
    def heap_sort(array: List[int]) -> List[int]:
        n = len(array)

        # Construir un max heap
        for i in range(n // 2 - 1, -1, -1):
            Modelo.heapify(array, n, i)

        # Extraer los elementos uno por uno
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            Modelo.heapify(array, i, 0)


        return array

    @staticmethod
    def counting_sort(array: List[int]) -> List[int]:
        # Encuentra el mínimo y el máximo en el array para determinar el rango
        min_val = min(array)
        max_val = max(array)
        range_val = max_val - min_val + 1

        # Inicializa el array de conteo y el array de salida
        count = [0] * range_val
        output = [0] * len(array)

        # Almacena el conteo de cada elemento en el array de conteo
        for num in array:
            count[num - min_val] += 1

        # Almacena el conteo acumulativo
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Coloca los elementos en el array de salida en orden
        for num in reversed(array):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1

        return output

    @staticmethod
    def counting_sort_for_radix(array: List[int], digit_place: int) -> None:
        size = len(array)
        output = [0] * size
        count = [0] * 10

        # Almacenar el conteo de ocurrencias en count[]
        for i in range(size):
            index = array[i] // digit_place
            count[index % 10] += 1

        # Cambiar count[i] para que ahora contenga la posición real
        # de este dígito en el array de salida
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Construir el array de salida
        i = size - 1
        while i >= 0:
            index = array[i] // digit_place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        # Copiar el array de salida al array original
        for i in range(size):
            array[i] = output[i]

    @staticmethod
    def radix_sort(array: List[int]) -> List[int]:
        # Encontrar el número máximo para saber el número de dígitos
        max_num = max(array)

        # Hacer un ordenamiento por conteo para cada dígito. Nota que en lugar
        # de pasar el número del dígito, se pasa exp. exp es 10^i
        # donde i es el número del dígito actual
        digit_place = 1
        while max_num // digit_place > 0:
            Modelo.counting_sort_for_radix(array, digit_place)
            digit_place *= 10


        return array