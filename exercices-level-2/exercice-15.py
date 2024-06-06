'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable,
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
índice de masa corporal calculado
redondeado con dos decimales. '''

print('¿Cuánto pesas (en kilogramos)?')
kg = float(input())
print('¿Cuánto mides (en metros)?')
estatura = float(input())
imc = kg / estatura
print(f'Tu imc es: {imc}')