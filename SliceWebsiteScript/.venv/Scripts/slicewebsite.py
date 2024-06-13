url = input("Ingrese una URL: ")
url = url.lower()

# Encontrar la posición del primer y segundo punto
primera_pos = url.find('.')
segunda_pos = url.find('.', primera_pos + 1)

# Extraer la subcadena entre el primer y segundo punto
if primera_pos != -1 and segunda_pos != -1:
    resultado = url[primera_pos + 1:segunda_pos]
else:
    resultado = url

print(resultado)  # Salida: el sitio escrito sin los protocolos http:// o https:// y el www,com,ar,etc
