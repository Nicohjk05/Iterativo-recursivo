# Solución recursiva al problema de las N reinas
def es_seguro(tablero, fila, col, n):
	# Verifica si es seguro colocar una reina en tablero[fila][col]
	for i in range(fila):
		if tablero[i][col] == 1:
			return False
	# Diagonal superior izquierda
	i, j = fila - 1, col - 1
	while i >= 0 and j >= 0:
		if tablero[i][j] == 1:
			return False
		i -= 1
		j -= 1
	# Diagonal superior derecha
	i, j = fila - 1, col + 1
	while i >= 0 and j < n:
		if tablero[i][j] == 1:
			return False
		i -= 1
		j += 1
	return True

def resolver_n_reinas_recursivo(tablero, fila, n, soluciones):
	if fila == n:
		soluciones.append([fila[:] for fila in tablero])
		return
	for col in range(n):
		if es_seguro(tablero, fila, col, n):
			tablero[fila][col] = 1
			resolver_n_reinas_recursivo(tablero, fila + 1, n, soluciones)
			tablero[fila][col] = 0

def n_reinas_recursivo(n):
	tablero = [[0]*n for _ in range(n)]
	soluciones = []
	resolver_n_reinas_recursivo(tablero, 0, n, soluciones)
	return soluciones

# Solución iterativa al problema de las N reinas usando backtracking manual
def n_reinas_iterativo(n):
	soluciones = []
	tablero = [[0]*n for _ in range(n)]
	fila = 0
	columnas = [0]*n
	while fila >= 0:
		colocado = False
		for col in range(columnas[fila], n):
			if es_seguro(tablero, fila, col, n):
				tablero[fila][col] = 1
				columnas[fila] = col + 1
				colocado = True
				break
		if colocado:
			if fila == n-1:
				soluciones.append([fila[:] for fila in tablero])
				tablero[fila][columnas[fila]-1] = 0
				columnas[fila] = 0
				fila -= 1
			else:
				fila += 1
		else:
			columnas[fila] = 0
			fila -= 1
			if fila >= 0:
				tablero[fila][columnas[fila]-1] = 0
	return soluciones

# Función para imprimir el tablero de manera legible
def imprimir_tablero(tablero):
	for fila in tablero:
		print(' '.join('Q' if x else '.' for x in fila))
	print()

# Ejemplo de uso
if __name__ == "__main__":
	n = 4
	print("Soluciones recursivas para N=4:")
	soluciones_rec = n_reinas_recursivo(n)
	for sol in soluciones_rec:
		imprimir_tablero(sol)
	print("Soluciones iterativas para N=4:")
	soluciones_it = n_reinas_iterativo(n)
	for sol in soluciones_it:
		imprimir_tablero(sol)
