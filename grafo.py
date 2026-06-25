import random
import math


# ==========================
# CLASE NODO
# ==========================

class Nodo:

    def __init__(self, id, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.id)


# ==========================
# CLASE ARISTA
# ==========================

class Arista:

    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino


# ==========================
# CLASE GRAFO
# ==========================

class Grafo:

    def __init__(self, dirigido=False):

        self.dirigido = dirigido
        self.nodos = {}
        self.aristas = []

    def agregarNodo(self, id, x=None, y=None):

        if id not in self.nodos:
            self.nodos[id] = Nodo(id, x, y)

    def existeArista(self, origen, destino):

        for a in self.aristas:

            if a.origen.id == origen and a.destino.id == destino:
                return True

            if (not self.dirigido and
                    a.origen.id == destino and
                    a.destino.id == origen):
                return True

        return False

    def agregarArista(self, origen, destino):

        if origen == destino:
            return

        if self.existeArista(origen, destino):
            return

        self.aristas.append(
            Arista(
                self.nodos[origen],
                self.nodos[destino]
            )
        )

    def guardarGV(self, archivo):

        tipo = "digraph" if self.dirigido else "graph"
        conector = "->" if self.dirigido else "--"

        with open(archivo, "w", encoding="utf-8") as f:

            f.write(f"{tipo} G {{\n")

            for nodo in self.nodos.values():
                f.write(f'    {nodo.id};\n')

            for arista in self.aristas:
                f.write(
                    f"    {arista.origen.id} {conector} {arista.destino.id};\n"
                )

            f.write("}\n")

# ==========================
# MODELO MALLA
# ==========================

def grafoMalla(m, n, dirigido=False):

    g = Grafo(dirigido)

    for i in range(m):
        for j in range(n):
            g.agregarNodo(f"{i}_{j}")

    for i in range(m):
        for j in range(n):

            if i < m - 1:
                g.agregarArista(
                    f"{i}_{j}",
                    f"{i+1}_{j}"
                )

            if j < n - 1:
                g.agregarArista(
                    f"{i}_{j}",
                    f"{i}_{j+1}"
                )

    return g




# ==========================
# MODELO ERDOS-RENYI
# ==========================

def grafoErdosRenyi(n, m, dirigido=False):

    g = Grafo(dirigido)

    for i in range(n):
        g.agregarNodo(i)

    while len(g.aristas) < m:

        origen = random.randint(0, n - 1)
        destino = random.randint(0, n - 1)

        if origen != destino:
            g.agregarArista(origen, destino)

    return g

# ==========================
# MODELO GILBERT
# ==========================

def grafoGilbert(n, p, dirigido=False):

    g = Grafo(dirigido)

    for i in range(n):
        g.agregarNodo(i)

    if dirigido:

        for i in range(n):
            for j in range(n):

                if i != j and random.random() <= p:
                    g.agregarArista(i, j)

    else:

        for i in range(n):
            for j in range(i + 1, n):

                if random.random() <= p:
                    g.agregarArista(i, j)

    return g

# ==========================
# MODELO GEOGRAFICO
# ==========================

def grafoGeografico(n, r, dirigido=False):

    g = Grafo(dirigido)

    # Crear nodos con coordenadas aleatorias
    for i in range(n):

        x = random.random()
        y = random.random()

        g.agregarNodo(i, x, y)

    ids = list(g.nodos.keys())

    for i in range(len(ids)):

        for j in range(i + 1, len(ids)):

            nodo1 = g.nodos[ids[i]]
            nodo2 = g.nodos[ids[j]]

            distancia = math.sqrt(
                (nodo1.x - nodo2.x) ** 2 +
                (nodo1.y - nodo2.y) ** 2
            )

            if distancia <= r:
                g.agregarArista(nodo1.id, nodo2.id)

    return g

# ==========================
# MODELO BARABASI-ALBERT
# ==========================

def grafoBarabasiAlbert(n, d, dirigido=False):

    g = Grafo(dirigido)

    if d < 2:
        d = 2

    # Crear los primeros d nodos
    for i in range(d):
        g.agregarNodo(i)

    # Conectarlos todos contra todos
    for i in range(d):
        for j in range(i + 1, d):
            g.agregarArista(i, j)

    # Agregar el resto de nodos
    for nuevo in range(d, n):

        g.agregarNodo(nuevo)

        # Calcular el grado de cada nodo existente
        grados = {}

        suma = 0

        for idNodo in list(g.nodos.keys())[:-1]:

            grado = 0

            for arista in g.aristas:

                if arista.origen.id == idNodo or arista.destino.id == idNodo:
                    grado += 1

            grados[idNodo] = grado
            suma += grado

        conectados = set()

        while len(conectados) < d:

            r = random.uniform(0, suma)

            acumulado = 0

            for nodo, grado in grados.items():

                acumulado += grado

                if acumulado >= r:

                    if nodo not in conectados:

                        g.agregarArista(nuevo, nodo)
                        conectados.add(nodo)

                    break

    return g

# ==========================
# MODELO DOROGOVTSEV-MENDES
# ==========================

def grafoDorogovtsevMendes(n, dirigido=False):

    g = Grafo(dirigido)

    # Crear los tres primeros nodos
    for i in range(3):
        g.agregarNodo(i)

    # Formar el triángulo inicial
    g.agregarArista(0, 1)
    g.agregarArista(1, 2)
    g.agregarArista(2, 0)

    # Agregar el resto de los nodos
    for nuevo in range(3, n):

        g.agregarNodo(nuevo)

        # Elegir una arista al azar
        arista = random.choice(g.aristas)

        # Conectar el nuevo nodo con ambos extremos
        g.agregarArista(nuevo, arista.origen.id)
        g.agregarArista(nuevo, arista.destino.id)

    return g


#Main Malla
#if __name__ == "__main__":

#    g = grafoMalla(5, 5)

#    g.guardarGV("malla.gv")

#    print("Modelo de malla generado correctamente. :D")
#


#main Erdos
#if __name__ == "__main__":

#   g = grafoErdosRenyi(20, 40)

 #   g.guardarGV("erdos.gv")

  #  print("Modelo Erdos-Renyi generado correctamente.")


#main Gilbert
#if __name__ == "__main__":

#    g = grafoGilbert(20, 0.25)

#    g.guardarGV("gilbert.gv")

#    print("Modelo Gilbert generado correctamente.")

#main Geografico
#if __name__ == "__main__":

#    g = grafoGeografico(30, 0.30)

#    g.guardarGV("geografico.gv")

#    print("Modelo Geográfico generado correctamente.")


#main Barabasi
#if __name__ == "__main__":

#    g = grafoBarabasiAlbert(40, 3)

#    g.guardarGV("barabasi.gv")

#    print("Modelo Barabasi-Albert generado correctamente.")


#main Dorog
#if __name__ == "__main__":

#    g = grafoDorogovtsevMendes(40)

#    g.guardarGV("dorogovtsev.gv")

#    print("Modelo Dorogovtsev-Mendes generado correctamente.")