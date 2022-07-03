# sin usar el modulo colorama

print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo") 
print("\x1b[1;33m"+"Texto en negrita de color amarillo") 
print("\033[4;35m"+"Texto en negrita y subrayado de color morado") 
print("\033[3;37;40m"+"Texto cursivo subrayado de color blanco")
print("\x1b[0;32;44m"+"Texto de color cian sobre azul")
#print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
print("\033[1;33m"+"Texto en negrita color amarillo"+'\033[0;m') 
print("\033[;36m"+"Texto normal de color cian")
print("\033[4;35;47m"+"Texto subr morado sobre blanco"+'\033[0;m') 
print("\033[4;35m"+"Texto normal subr color morado"+'\033[0;m')
print("\033[3;35m"+'texto cursivo color morado'+'\033[0;m')
print("\033[6;37;41m"+'texto normal color blanco sobre rojo'+'\033[0;m')

def construye_tabla_formatos():
    # construye una tabla con todos los formatos posibles
    for estilo in range(8):
        for colortexto in range(30,38):
            cad_cod = ''
            for colorfondo in range(40,48): 
                fmto = ';'.join([str(estilo), 
                                 str(colortexto),
                                 str(colorfondo)]) 
                cad_cod+="\033["+fmto+"m "+fmto+" \033[0m" 
            print(cad_cod)
        print('\n')

construye_tabla_formatos()

