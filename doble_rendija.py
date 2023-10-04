import math
import Clasico_a_Cuantico


def main():
    dinamica = [[0, 0, 0, 0, 0, 0, 0, 0], [1 / math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
       [1 / math.sqrt(2), 0, 0, 0, 0, 0, 0, 0], [0, -1 + 1j / (math.sqrt(6)), 0, 1, 0, 0, 0, 0],
       [0, -1 - 1j / (math.sqrt(6)), 0, 0, 1, 0, 0, 0],
       [0, 1 - 1j / (math.sqrt(6)), -1 + 1j / (math.sqrt(6)), 0, 0, 1, 0, 0],
       [0, 0, -1 - 1j / (math.sqrt(6)), 0, 0, 0, 1, 0],
       [0, 0, 1 - 1j / (math.sqrt(6)), 0, 0, 0, 0, 1]]

    estado = [1,0,0,0,0,0,0,0]
    clicks = 1
    resp = Clasico_a_Cuantico.cuantico(dinamica,estado,clicks)
    print(resp)



main()

