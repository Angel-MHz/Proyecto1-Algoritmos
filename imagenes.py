import os

for archivo in os.listdir("grafos"):
    if archivo.endswith(".gv"):
        nombre = archivo[:-3]
        os.system(f'dot -Tpng grafos/{archivo} -o grafos/{nombre}.png')

print("Imágenes generadas.")