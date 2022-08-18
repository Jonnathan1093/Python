# Cuenta regresiva
import time # Libreria para el tiempo 

# Realizamos un contador
for contador in range(10, -1, -1):
# Inicia desde el 10, -1 para que llegue hasta el 0, y como va hacia atras -1
    if contador != 0: # 
        # print(contador)
        print(f"\r{contador}", end=" ") # \r para que nos regrese o retorne ahi mismo
        time.sleep(1) #Aqui ponemos el retarde de 1 segundo
    else:
        print(f"\r{contador}", end=" ")
        print("Fin de la cuenta atras")
        
       
        