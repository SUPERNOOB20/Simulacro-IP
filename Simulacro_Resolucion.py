# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def cantidad_de_apariciones(l: list, e: int) -> int:           # Devuelve la cantidad de apariciones de un entero "e" en una lista "l".
    numeroDeApariciones: int = 0
    while e in l:
        l.remove(e)
        numeroDeApariciones += 1
    return numeroDeApariciones
    # pass
    
    
def ultima_aparicion(s: list, e: int) -> int:
    for i in range(len(s) - 1, -1, -1):
        if e == s[i]:
            return i
        
        
def ultima_aparicion2(s: list, e: int) -> int:
    tope = cantidad_de_apariciones((s), (e))
    contador = 0
    for i in range(0, len(s)):
        if e == s[i]:
            contador += 1
            if contador == tope:
                return i
    # pass
    
# print(ultima_aparicion(([-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]), (0)))     # Devuelve 7 :]


# print("oa", ultima_aparicion(([-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]), (0)))     # Devuelve 7 :]
# print("ola", ultima_aparicion2(([-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]), (0)))     # Devuelve 7 :]
# print("ptmdr", cantidad_de_apariciones(([-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]), (0)))

##########################################################################
##########################################################################

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def elementos_exclusivos(s: list, t: list) -> list:
    # cual_es_mas_largo: str = "t"
    # if len(s) >= len(t):
        # cual_es_mas_largo = "s"
    res: list = []
    for i in t:
        if i not in s:
            res.append(i)
    for i in s:
        if i not in t:
            res.append(i)
    res = eliminarRepetidos(res)
    
    return res

def eliminarRepetidos(l: list) -> list:
    sinRepes = []
    for i in l:
        if i not in sinRepes:
            sinRepes.append(i)
    return sinRepes
    # pass

s = [-1, 4, 0, 4, 3, 0, 100, 0, -1, -1]
t = [0, 100, 5, 0, 100, -1, 5]
# print(elementos_exclusivos(s, t))

"""
def pertenece (l: list e: int) -> bool:            # Si e pertenece a l, devuelve True. Si no, devuelve False.
    for i in l:
        if i == e:
            return True
    return False
"""
##########################################################################
##########################################################################

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    # todasLasKeys: list = []
    # todasLasKeys.append(ingles.values())
    # todasLasKeys.append(aleman.values())
    # print(todasLasKeys)
    res: int = 0
    for i in aleman.values():
        if i in ingles.values():
            res += 1
    for i in ingles.values():
        if i in aleman.values():
            res += 1
    return res // 2
    # pass

def contar_traducciones_iguales2(ingles: dict, aleman: dict) -> int:
    contador: int = 0
    for k in aleman:
        for j in ingles:
            if aleman[k] == ingles[j]:
                contador += 1
    return contador

# diccionario = (clave: valor)
# diccionario[clave] == valor


aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}

# print(contar_traducciones_iguales((ingles), (aleman)))
# print(contar_traducciones_iguales2((ingles), (aleman)))

##########################################################################
##########################################################################

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO


"""
##### FORMA 1:
def convertir_a_diccionario2(lista: list) -> dict:
    diccionarioOutput: Dict = {}
    for elemento in lista:
        print(elemento)
        diccionarioOutput.update({elemento: cantidad_de_apariciones2(lista, elemento)})
    return diccionarioOutput


def cantidad_de_apariciones2(l: list, e: int) -> int:           # Devuelve la cantidad de apariciones de un entero "e" en una lista "l".
    numeroDeApariciones: int = 0
    l2: list = l.copy()
    while e in l2:
        l2.remove(e)
        numeroDeApariciones += 1
    return numeroDeApariciones
    # pass
"""

##### FORMA 2:


lista = [-1, 0, 4, 100, 100, -1, -1]

# print("funca bien", cantidad_de_apariciones2(([1,2,3,3,3,2,3,1]), (3)))
# print("funca bien", cantidad_de_apariciones2((lista), (0)))

# print(convertir_a_diccionario(lista))          # se debería devolver res = {-1:3, 0:1, 4:1, 100:2} 

# (mano: hand)
# (dedo: hand)
        