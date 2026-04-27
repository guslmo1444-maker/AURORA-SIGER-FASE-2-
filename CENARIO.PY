# ==========================================
# MGPEB - Módulo de Gerenciamento de Pouso
# Missão Aurora Siger
# ==========================================

# =========================
# 1. Cadastro dos módulos
# =========================

fila_pouso = [
    {"nome": "Energia", "combustivel": 15, "massa": 2000, "criticidade": "alta", "horario": 1, "sensores": True},
    {"nome": "Habitação", "combustivel": 70, "massa": 1500, "criticidade": "alta", "horario": 2, "sensores": True},
    {"nome": "Laboratório", "combustivel": 80, "massa": 1200, "criticidade": "baixa", "horario": 3, "sensores": True},
    {"nome": "Logística", "combustivel": 60, "massa": 1800, "criticidade": "media", "horario": 4, "sensores": True},
    {"nome": "Suporte Médico", "combustivel": 50, "massa": 1000, "criticidade": "alta", "horario": 5, "sensores": True}
]

# Listas auxiliares
pousados = []
espera = []
alerta = []

# =========================
# 2. Função de busca
# =========================

def buscar_menor_combustivel(lista):
    """
    Retorna o módulo com menor nível de combustível
    """
    menor = lista[0]
    for modulo in lista:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor

# =========================
# 3. Função de ordenação
# =========================

def calcular_prioridade(modulo):
    """
    Define prioridade com base em:
    - combustível
    - criticidade
    - massa
    """
    prioridade = 0

    # combustível crítico
    if modulo["combustivel"] < 20:
        prioridade += 3

    # criticidade
    if modulo["criticidade"] == "alta":
        prioridade += 2

    # massa elevada
    if modulo["massa"] > 1500:
        prioridade += 1

    return prioridade


def ordenar_fila(lista):
    """
    Ordena a fila por prioridade (maior primeiro)
    """
    lista.sort(key=calcular_prioridade, reverse=True)

# =========================
# 4. Função de decisão (lógica booleana)
# =========================

def decidir_pouso(modulo, area_disponivel, clima_ok):
    """
    Decide se o módulo pode pousar, deve esperar ou está em alerta
    """

    combustivel_suficiente = modulo["combustivel"] > 10
    sensores_ok = modulo["sensores"]

    # Regra principal (AND)
    if combustivel_suficiente and sensores_ok and area_disponivel and clima_ok:
        return "POUSAR"

    # Regra de alerta (OR)
    elif modulo["combustivel"] <= 10 or not sensores_ok:
        return "ALERTA"

    # Caso contrário
    else:
        return "ESPERAR"

# =========================
# 5. Simulação do sistema
# =========================

def simular_pouso(fila):
    area_disponivel = True
    clima_ok = True

    # Ordenar fila antes do processamento
    ordenar_fila(fila)

    for modulo in fila:

        decisao = decidir_pouso(modulo, area_disponivel, clima_ok)

        if decisao == "POUSAR" and area_disponivel:
            pousados.append(modulo)
            area_disponivel = False  # apenas um pouso por vez

        elif decisao == "ALERTA":
            alerta.append(modulo)

        else:
            espera.append(modulo)

# =========================
# 6. Execução
# =========================

simular_pouso(fila_pouso)

# =========================
# 7. Resultados
# =========================

print("=== RESULTADO DO SISTEMA MGPEB ===\n")

print("Módulos pousados:")
for m in pousados:
    print("-", m["nome"])

print("\nMódulos em espera:")
for m in espera:
    print("-", m["nome"])

print("\nMódulos em alerta:")
for m in alerta:
    print("-", m["nome"])

# =========================
# 8. Exemplo de busca
# =========================

menor = buscar_menor_combustivel(fila_pouso)
print("\nMódulo com menor combustível:", menor["nome"])