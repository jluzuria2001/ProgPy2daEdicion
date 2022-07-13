'''
f=open('miArchivo.txt','w')
f.write("Hola mundo\n")
f.write("Hola mundo otra vez!")
f.close()
'''

with open("miArchivo.txt", "r+") as f:
    f.write("I love Python")
    #print(contenido)