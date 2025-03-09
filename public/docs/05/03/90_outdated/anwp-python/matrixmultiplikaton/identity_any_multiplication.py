'''Aufgabe 17.05.2024: Matrixmultiplikation. 
a) Eine beliebige 4x4 Matrix mit der der Identitätsmatrix multiplizieren. Das Ergebnis anzeigen. 
b) zwei beliebige 4x4 Matrizen multiplizieren. 
Immer Datentyp Liste verwenden. In einer Liste muss man immer per Zeile arbeiten
Holger alwas says deviede and conquer. Aufteilen und dann zusammenführen.'''

# Identitätsmatrix 4x4
identy_matrix_row_1 = [1, 0, 0, 0]
identy_matrix_row_2 = [0, 1, 0, 0]
identy_matrix_row_3 = [0, 0, 1, 0]
identy_matrix_row_4 = [0, 0, 0, 1]

# beliebige 4x4 Matrix 1
any_matrix_row_1 = [1, 2, 3, 4]
any_matrix_row_2 = [5, 6, 7, 8]
any_matrix_row_3 = [9, 10, 11, 12]
any_matrix_row_4 = [13, 14, 15, 16]

# beliebige 4x4 Matrix 2
any_matrix_row_1 = [4, 3, 2, 1]
any_matrix_row_2 = [8, 7, 6, 5]
any_matrix_row_3 = [12, 11, 10, 9]
any_matrix_row_4 = [16, 15, 14, 13]

# Matrixmultiplikation
multiplied_matrix_row_1 = [a * b for a, b in zip(identy_matrix_row_1, any_matrix_row_1)] # to do explaining the meaning of a, b and zip
multiplied_matrix_row_2 = [a * b for a, b in zip(identy_matrix_row_2, any_matrix_row_2)]
multiplied_matrix_row_3 = [a * b for a, b in zip(identy_matrix_row_3, any_matrix_row_3)]
multiplied_matrix_row_4 = [a * b for a, b in zip(identy_matrix_row_4, any_matrix_row_4)]

# Ergebnis anzeigen
print ("Matrixmultiplikation: Identitätsmatrix 4x4 * beliebige 4x4 Matrix")
print(multiplied_matrix_row_1) # [1, 0, 0, 0]
print(multiplied_matrix_row_2) # [0, 6, 0, 0]
print(multiplied_matrix_row_3) # [0, 0, 11, 0]
print(multiplied_matrix_row_4) # [0, 0, 0, 16]

# beliebige 4x4 Matrizen
next_matrix_row_1 = [1, 2, 3, 4]
next_matrix_row_2 = [5, 6, 7, 8]
next_matrix_row_3 = [9, 10, 11, 12]
next_matrix_row_4 = [13, 14, 15, 16]

# Matrixmultiplikation
next_multiplied_matrix_row_1 = [a * b for a, b in zip(multiplied_matrix_row_1, next_matrix_row_1)]
next_multiplied_matrix_row_2 = [a * b for a, b in zip(multiplied_matrix_row_2, next_matrix_row_2)]
next_multiplied_matrix_row_3 = [a * b for a, b in zip(multiplied_matrix_row_3, next_matrix_row_3)]
next_multiplied_matrix_row_4 = [a * b for a, b in zip(multiplied_matrix_row_4, next_matrix_row_4)]

# Ergebnis anzeigen
print ("Matrixmultiplikation: beliebige 4x4 Matrix * beliebige 4x4 Matrix")
print(next_multiplied_matrix_row_1) # [1, 0, 0, 0]
print(next_multiplied_matrix_row_2) # [0, 36, 0, 0]
print(next_multiplied_matrix_row_3) # [0, 0, 121, 0]
print(next_multiplied_matrix_row_4) # [0, 0, 0, 256]

