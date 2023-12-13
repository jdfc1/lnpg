notas = [0, 0, 1, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

notas_validas = [nota for nota in notas if nota > 0]
print(notas_validas)