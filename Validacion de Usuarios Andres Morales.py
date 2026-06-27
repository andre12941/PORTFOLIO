"Lista de nombre"


nombre1 = " Andres "
nombre2 = " Juan "
nombre3 = " Pedro " 
nombre4 = " Maria "
nombre5 = " Laura "
ListaNombres = str(nombre1 + nombre2 + nombre3 + nombre4 + nombre5)
 
admitidos = str(nombre1 + nombre4 + nombre5)
rechazados = str (nombre2 + nombre3)
if ListaNombres != admitidos and ListaNombres != rechazados:
    print ('Estos son los admitidos:  ' + admitidos + 
           ' Y estos son los rechazados ' + rechazados)

 
elif ListaNombres == admitidos :
    print('estos son los rechazodos ' + ListaNombres)
    
elif ListaNombres != rechazados:
    print('estos son rechazados')
else: 
   print('estos son los resultado')
  

entrada = input('Introduce tu nombre: ')
print (type(entrada))  

if entrada == nombre1 or  entrada == nombre4 or entrada ==nombre5:
 print('Admitido')
    
elif entrada == nombre2 or entrada==nombre3:
    print ('rechazado')
