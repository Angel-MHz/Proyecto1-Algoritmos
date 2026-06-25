from grafo import *

print("Generando grafos...")

# ==========================
# MALLA
# ==========================

grafoMalla(7,7).guardarGV("grafos/malla50.gv")
grafoMalla(14,14).guardarGV("grafos/malla200.gv")
grafoMalla(22,23).guardarGV("grafos/malla500.gv")

print("Malla OK")

# ==========================
# ERDOS-RENYI
# ==========================

grafoErdosRenyi(50,100).guardarGV("grafos/erdos50.gv")
grafoErdosRenyi(200,400).guardarGV("grafos/erdos200.gv")
grafoErdosRenyi(500,1000).guardarGV("grafos/erdos500.gv")

print("Erdos OK")

# ==========================
# GILBERT
# ==========================

grafoGilbert(50,0.08).guardarGV("grafos/gilbert50.gv")
grafoGilbert(200,0.03).guardarGV("grafos/gilbert200.gv")
grafoGilbert(500,0.01).guardarGV("grafos/gilbert500.gv")

print("Gilbert OK")

# ==========================
# GEOGRAFICO
# ==========================

grafoGeografico(50,0.20).guardarGV("grafos/geografico50.gv")
grafoGeografico(200,0.10).guardarGV("grafos/geografico200.gv")
grafoGeografico(500,0.06).guardarGV("grafos/geografico500.gv")

print("Geografico OK")

# ==========================
# BARABASI
# ==========================

grafoBarabasiAlbert(50,3).guardarGV("grafos/barabasi50.gv")
grafoBarabasiAlbert(200,3).guardarGV("grafos/barabasi200.gv")
grafoBarabasiAlbert(500,3).guardarGV("grafos/barabasi500.gv")

print("Barabasi OK")

# ==========================
# DOROGOVTSEV
# ==========================

grafoDorogovtsevMendes(50).guardarGV("grafos/dorogovtsev50.gv")
grafoDorogovtsevMendes(200).guardarGV("grafos/dorogovtsev200.gv")
grafoDorogovtsevMendes(500).guardarGV("grafos/dorogovtsev500.gv")

print("Dorogovtsev OK")

print("\n========================")
print("PROYECTO TERMINADO :D viva el prof Rolando :D")
print("========================")