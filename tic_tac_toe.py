# Laboratorio: Juego del Gato (Tic-Tac-Toe)
# Detalle: Juego del Gato utilizando los fundamentos de Python (PCEP)

# Librería Integrada Python para utilizar números aleatorios (se requiere para que la máquina pueda realizar sus movimientos al azar)
from random import randrange

# Diccionario con variables que se utilizan en el juego como mensajes o valores constantes
DICTIONARY = {
    "SIGN_X": "X",
    "SIGN_O": "O",
    "VICTORY": "¡Victoria! 🎉,",
    "DEFEAT": "¡Derrota!, la máquina ha vencido 🤖...🥴",
    "ABORTED": "Juego abandonado, no cuenta...",
    "NEXT": "Continuar juego",
    "DRAW": "¡Empate! ⚔️, sin ganador, ya no hay espacios",
    "INVALID": "Movimiento no permitido... Ingresa un número válido (del 1 al 9) o ingresa 0 para abandonar el juego",
    "SQUARE_TAKEN": "Ese cuadro ya se encuentra utilizado, elige otro"
}



# <board> Variable para retener el tablero del juego, se inicializa una estructura así
"""
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""
board = [list(range(i+1, i + 4)) for i in range(0, 9, 3)]



# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
def DisplayBoard(board):

    # Recorrer la lista <board> con los movimientos actuales
    for row in board:
        # Imprime el siguiente formato
        """
        +-------++-------++-------+
        |       ||       ||       |
        |   1   ||   2   ||   3   |
        |       ||       ||       |
        +-------++-------++-------+
        |       ||       ||       |
        |   4   ||   5   ||   6   |
        |       ||       ||       |
        +-------++-------++-------+
        |       ||       ||       |
        |   7   ||   8   ||   9   |
        |       ||       ||       |
        +-------++-------++-------+
        """
        print("+-------+"*3, "|       |"*3, sep="\n")
        print("|   ", row[0], "   |", "|   ", row[1], "   |", "|   ", row[2], "   |", sep="")
        print("|       |"*3)
    else:
        # Cuando el bucle finaliza aplicamos el else para cerrar la caja del tablero
        print("+-------+"*3)





# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
def EnterMove(board):

    try:

        # Antes de pedir el movimiento al jugador, siempre comprobamos sí existen espacios disponibles en el tablero
        free_spaces = MakeListOfFreeFields(board)

        # Si al obtener nuestros espacios disponibles nos arroja empate, quiere decir que no existen espacios disponibles por jugar
        if (free_spaces == DICTIONARY["DRAW"]):
            # Retornamos que el resultado es un empate
            print(DICTIONARY["DRAW"])
            return DICTIONARY["DRAW"]

        # Movimiento del usuario <user_movement>, inserta un número del 1 al 9
        user_movement = int(input("Selecciona un cuadro libre del 1 al 9 para tu jugada (Ingresa 0 si quieres abandonarlo): ")) 

        # Retornar 0 cuando el movimiento del usuario <user_movement>, es decir, abandonar el juego
        if user_movement == 0: 
            print(DICTIONARY["ABORTED"])
            return DICTIONARY["ABORTED"]
        
        if user_movement > 0 and user_movement < 10:

            # utilizamos la expresión user_movement-1 porque necesitamos que coincida la posición del usuario con la lista
            move = user_movement-1

            if free_spaces[move] == DICTIONARY["SQUARE_TAKEN"]:
                raise ValueError
            else:

                # Se modifica el tablero con el movimiento del usuario (O)
                board[free_spaces[move][0]][free_spaces[move][1]] = DICTIONARY["SIGN_O"]

                result = VictoryFor(board, DICTIONARY["SIGN_O"])

                DisplayBoard(board)

                if result == DICTIONARY["VICTORY"]:
                    print(DICTIONARY["VICTORY"], "¡Ganaste  " + user_name + "! 🥳")
                

                # Retornar el valor del resultado
                return result
        else: 
            # si el usuario introduce un número no dentro del rango permitido (0-9) entonces arrojamos directamente el except utilizando la palabra clave raise
            raise
    except ValueError:
        print(DICTIONARY["SQUARE_TAKEN"])
        return DICTIONARY["SQUARE_TAKEN"]
    except:
        print(DICTIONARY["INVALID"])
        return DICTIONARY["INVALID"]





# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
# cuando se trata de un cuadro ocupado la tupla se compone por el movimiento "X" o "O"
def MakeListOfFreeFields(board):

    temp_board = []
    draw = True
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] in range(1, 10):
                # Espacio libre en el tablero, ingresamos coordenadas
                temp_board.append((fila, columna))
                draw = False
            else:
                # Espacio NO libre, ingresamos el movimiento (X ó O)
                temp_board.append(DICTIONARY["SQUARE_TAKEN"])

    if draw == True:
        return DICTIONARY["DRAW"]

    return temp_board




# La función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
def VictoryFor(board, sign):

    # Condicional cuando hay que comprobar la victoria del jugador O
    if sign == DICTIONARY["SIGN_O"]:

        # Detectamos si existe un O en la esquina superior izquierda
        if board[0][0] == DICTIONARY["SIGN_O"]:

            # Comprobamos victoria desde la esquina superior izquierda hasta esquina superior derech8vea (horizontal)
            if board[0][1] == DICTIONARY["SIGN_O"] and board[0][2] == DICTIONARY["SIGN_O"]:
                return DICTIONARY["VICTORY"]

            # Comprobamos victoria desde la esquina superior izquierda hasta esquina inferior izquierda (vertical)
            if board[1][0] == DICTIONARY["SIGN_O"] and board[2][0] == DICTIONARY["SIGN_O"]:
                return DICTIONARY["VICTORY"]
        
        # Detectamos si existe un O en la esquina inferior derecha
        elif board[2][2] == DICTIONARY["SIGN_O"]:

            # Comprobamos victoria desde la esquina inferior derecha hasta esquina superior derecha (vertical)
            if board[1][2] == DICTIONARY["SIGN_O"] and board[0][2] == DICTIONARY["SIGN_O"]:
                return DICTIONARY["VICTORY"]

            # Comprobamos victoria desde la esquina inferior derecha hasta esquina inferior izquierda (horizontal)
            if board[2][1] == DICTIONARY["SIGN_O"] and board[2][0] == DICTIONARY["SIGN_O"]:
                return DICTIONARY["VICTORY"]

    elif sign == DICTIONARY["SIGN_X"]:
        
        # Detectamos si existe un X en la esquina superior izquierda
        if board[0][0] == DICTIONARY["SIGN_X"]:
            
            # Comprobamos victoria desde la esquina superior izquierda hasta esquina superior derecha (horizontal)
            if board[0][1] == DICTIONARY["SIGN_X"] and board[0][2] == DICTIONARY["SIGN_X"]:
                return DICTIONARY["DEFEAT"]
            
            # Comprobamos victoria desde la esquina superior izquierda hasta esquina inferior izquierda (vertical)
            if board[1][0] == DICTIONARY["SIGN_X"] and board[2][0] == DICTIONARY["SIGN_X"]:
                return DICTIONARY["DEFEAT"]
            
            # Comprobamos victoria desde la esquina superior izquierda hasta esquina inferior derecha (diagonal)
            if board[2][2] == DICTIONARY["SIGN_X"]:
                return DICTIONARY["DEFEAT"]

        # Detectamos si existe un X en la esquina inferior derecha
        elif board[2][2] == DICTIONARY["SIGN_X"]:

            # Comprobamos victoria desde la esquina inferior derecha hasta esquina superior derecha (vertical)
            if board[1][2] == DICTIONARY["SIGN_X"] and board[0][2] == DICTIONARY["SIGN_X"]:
                return DICTIONARY["DEFEAT"]

            # Comprobamos victoria desde la esquina inferior derecha hasta esquina inferior izquierda (horizontal)
            if board[2][1] == DICTIONARY["SIGN_X"] and board[2][0] == DICTIONARY["SIGN_X"]:
                return DICTIONARY["DEFEAT"]  

            # Comprobamos victoria desde la esquina superior derecha hasta esquina superior izquierda (diagonal)
            if board[0][0] == DICTIONARY["SIGN_X"]:
                return DICTIONARY["DEFEAT"]
        
        # Detectamos si hay victoria en vertical desde el centro del tablero (vertical) 
        elif board[2][1] == DICTIONARY["SIGN_X"] and board[0][1] == DICTIONARY["SIGN_X"]:
            return DICTIONARY["DEFEAT"]
    
        # Detectamos si hay victoria en vertical desde el centro del tablero (horizontal)
        elif board[1][0] == DICTIONARY["SIGN_X"] and board[1][2] == DICTIONARY["SIGN_X"]:
            return DICTIONARY["DEFEAT"]
        
        # Detectamos si hay victoria en diagnocal desde esquina inferior izquierda hasta esquina superior derecha (diagonal)
        elif board[2][0] == DICTIONARY["SIGN_X"] and board[0][2] == DICTIONARY["SIGN_X"]:
            return DICTIONARY["DEFEAT"]
    
    return DICTIONARY["NEXT"]





# La función dibuja el movimiento de la máquina y actualiza el tablero.
def DrawMove(board):

    free_spaces = MakeListOfFreeFields(board)

    while True:
        cpu_move = randrange(9)
        if free_spaces[cpu_move] == DICTIONARY["SQUARE_TAKEN"]: 
            continue

        # Se modifica el tablero con el movimiento del usuario (O)
        board[free_spaces[cpu_move][0]][free_spaces[cpu_move][1]] = DICTIONARY["SIGN_X"]

        result = VictoryFor(board, DICTIONARY["SIGN_X"])

        DisplayBoard(board)

        if result == DICTIONARY["DEFEAT"]:
            print(DICTIONARY["DEFEAT"])
            return DICTIONARY["DEFEAT"]
        
        break





# Función para inicializar el juego y mostrar las reglas al usuario
def InitGame(board):

    print("Bienvenido al juego del gato\t X | O", sep="\n", end="\n\n")
    global user_name

    while True:
        # Capturar el nombre del usuario para guardarlo en el juego
        user_name = input("Ingresa tu apodo o nombre: ")
        if (len(user_name) > 0):
            break

    # Mostrar reglas del juego
    print("*"*30, "⚠️\tReglas del Juego 🕹️\t⚠️", "Lá maquina juega las X", "Tú, " + user_name + " serás las O", "En este juego la máquina empieza primero y su primer movimiento siempre es en el centro", "*"*30, sep="\n")

    input("\nPRESIONA ENTER PARA JUGAR...")

    # Ejecutar manualmente el primer movimiento de la máquina en el centro
    board[1][1] = DICTIONARY["SIGN_X"]

    # Mostrar Tablero
    DisplayBoard(board)






######################################################################
############ EMPIEZA A LEER EL CÓDIGO DESDE AQUÍ #####################
######################################################################

# Se ejecuta la función que inicia el juego
InitGame(board)

# Búcle infinito hasta que el juego termina o es abandonado por el usuario
while True:   
    
    # Ejecutar función para realizar el movimiento del usuario
    move_result = EnterMove(board)
    
    if move_result == DICTIONARY["INVALID"] or move_result == DICTIONARY["SQUARE_TAKEN"]: 
        continue

    if move_result == DICTIONARY["ABORTED"] or move_result == DICTIONARY["VICTORY"] or move_result == DICTIONARY["DRAW"]:
        break

    # Si el resultado del movimiento del usuario <move_result> es continuar el juego, entonces ejecutamos la función para que la máquina realice un movimiento
    move_result = DrawMove(board)

    if move_result == DICTIONARY["DEFEAT"]:
        break

input()

