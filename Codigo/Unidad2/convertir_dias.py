numero_dias=input("numero de dias a convertir: ")
numero_dias=int(numero_dias)

num_años=numero_dias//365
num_semanas=(numero_dias%365)//7
num_dias_restante=(numero_dias%365)%7

print("años: " + str(num_años))
print("semanas: " + str(num_semanas))
print("dias: " + str(num_dias_restante))
