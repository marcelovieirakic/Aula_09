
## crie uma funcao que realize uma soma
## biblioteca pydantic valida as entradas de dados do python para nao precisarmos fazer manualmente
# def fsomar( numero1: float, numero2: float, numero3: float ) -> float:
#     """
#     comentarios de como utilizar a funcao
#     """
#     resultado = numero1 + numero2 + numero3
#     return resultado

# minha_soma = fsomar(7.2,4,8)
# print(minha_soma)

# def converter_temp( temperatura: float ) -> float:
#     resultado = ( temperatura * 9/5 ) + 32
#     return resultado

# tempf = converter_temp(10.52)
# print(tempf)

# Define a função converter_temp que recebe uma lista de temperaturas em Celsius
from typing import List
def converter_temp(temperaturas: list[float]) -> list: 
    """
    converter celsius para fah
    """
    # Cria uma lista de temperaturas convertidas para Fahrenheit usando list comprehension
    resultado = [(temp * 9/5) + 32 for temp in temperaturas]
    # Retorna a lista de temperaturas convertidas
    return resultado

# Chama a função converter_temp passando uma lista de temperaturas em Celsius
temps_fahrenheit = converter_temp([10.52, 20.75, 30.1])

# Imprime a lista de temperaturas em Fahrenheit
print(temps_fahrenheit)

