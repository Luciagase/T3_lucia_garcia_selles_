#6) Eliminación de espacios en nombres: Almacena el nombre de una persona, incluyendo algunos espacios en blanco al principio y al final del nombre. Investiga para que se puede de utilizar la combinación de caracteres: "\t" y "\n", y haz uso de ellas al menos una vez. Imprime el nombre una vez para que se muestre el espacio en blanco alrededor del nombre. Luego, imprime el nombre utilizando cada una de las tres funciones de eliminación de espacios: "lstrip()" (izquierda), "rstrip()" (derecha) y "strip()" (ambos lados).
nombre2="      Lucia       " 
nombre="\tLucia\n" #\t tabulador \n salto de línea
print(nombre2) 
print(nombre)
print(nombre.lstrip()) #lstrip() elimina espacios en blanco a la izquierda
print(nombre.rstrip()) #rstrip() elimina espacios en blanco a la derecha
print(nombre.strip()) #strip() elimina espacios en blanco a ambos lados