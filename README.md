# AURORA-SIGER-FASE-2

Modelagem do cenário de pouso e fila de módulos
Nesta etapa, será modelado o sistema responsável por organizar o pouso dos módulos da missão Aurora Siger em Marte. O objetivo é simular a chegada de diferentes unidades operacionais à órbita marciana e definir critérios para autorização de pouso com base em condições técnicas e operacionais.
Os módulos representam componentes fundamentais para a construção inicial da colônia, sendo definidos como: Habitação, Energia, Laboratório, Logística e Suporte Médico. Cada módulo possui uma função específica dentro da base e, portanto, níveis distintos de criticidade.
Para possibilitar a análise e tomada de decisão, cada módulo será representado por um conjunto de atributos, incluindo: nível de combustível (essencial para o pouso), massa (impacta no consumo e na complexidade da operação), criticidade da carga (relacionada à importância do módulo para a sobrevivência e operação da base) e horário estimado de chegada à órbita.
O sistema considera que os módulos ainda estão em fase de descida e, portanto, não exercem suas funções operacionais na base. Dessa forma, variáveis como geração de energia elétrica não são consideradas nesta etapa, sendo o foco exclusivamente na segurança do pouso.
Para organização dos dados, será utilizada uma estrutura de fila (queue), representando os módulos aguardando autorização de pouso. Essa fila segue o princípio FIFO (First In, First Out), porém pode sofrer alterações de ordem conforme critérios de prioridade definidos pelo sistema.
Além da fila principal, foram utilizadas listas auxiliares para representar diferentes estados dos módulos durante a simulação:
    • Lista de módulos pousados, contendo aqueles que já realizaram o pouso com sucesso; 
    • Lista de módulos em espera, composta por módulos que ainda aguardam autorização; 
    • Lista de módulos em alerta, reunindo aqueles em situação crítica, como baixo nível de combustível.
Um exemplo dessa estrutura é apresentado a seguir:
fila_pouso = [
{"nome": "Energia", "combustivel": 15, "massa": 2000, "criticidade": "alta"},
{"nome": "Habitação", "combustivel": 70, "massa": 1500, "criticidade": "alta"}
]
A decisão de autorização de pouso será baseada em regras lógicas que consideram, prioritariamente, o nível de combustível (indicador de risco imediato), seguido pela criticidade do módulo e, em casos de empate, pela massa e horário de chegada. Essa abordagem garante que módulos em situação crítica ou de maior impacto operacional sejam priorizados.
Dessa forma, o sistema simula um ambiente controlado de pouso, no qual múltiplos módulos competem por recursos limitados (como janela de pouso), exigindo decisões rápidas, estruturadas e fundamentadas em critérios técnicos.
Definição dos atributos dos módulos de pouso
Para viabilizar a análise e o gerenciamento do processo de pouso dos módulos na superfície marciana, foi necessário definir um conjunto de atributos que representassem as principais características operacionais de cada unidade. Esses atributos são fundamentais para a aplicação das regras de decisão do sistema, permitindo avaliar riscos, estabelecer prioridades e organizar a sequência de pousos de forma eficiente.
O primeiro atributo considerado é a prioridade de pouso, que representa o nível de urgência associado a cada módulo. Essa prioridade está diretamente relacionada à função do módulo na colônia, sendo maior para aqueles considerados essenciais à sobrevivência e operação inicial da base, como os módulos de energia, habitação e suporte médico.
Outro atributo fundamental é o nível de combustível, expresso em percentual. Esse parâmetro é crítico para a tomada de decisão, pois indica a capacidade do módulo de realizar manobras seguras de descida e pouso. Módulos com baixos níveis de combustível representam maior risco operacional e, portanto, tendem a receber prioridade no processo de autorização de pouso.
A massa do módulo também é considerada, uma vez que impacta diretamente no consumo de combustível e na complexidade da operação de pouso. Módulos mais pesados exigem maior esforço dos sistemas de propulsão, podendo demandar decisões diferenciadas em situações de empate com outros critérios.
A criticidade da carga refere-se à importância funcional do módulo para a missão. Esse atributo está relacionado ao papel que o módulo desempenha na estrutura da colônia, sendo classificado, por exemplo, em níveis como alta, média ou baixa criticidade. Essa classificação auxilia na priorização estratégica dos pousos, especialmente em cenários onde múltiplos módulos apresentam condições semelhantes.
Por fim, o horário estimado de chegada à órbita é utilizado como critério adicional de organização. Esse atributo permite ordenar os módulos de acordo com sua sequência de chegada, sendo utilizado principalmente como fator de desempate quando outros critérios apresentam equivalência.
Organização dos módulos em estruturas de dados lineares
Para garantir um gerenciamento eficiente do processo de pouso dos módulos, foi necessária a utilização de estruturas de dados lineares adequadas, capazes de representar o fluxo de chegada, análise e decisão do sistema. Essas estruturas permitem organizar os módulos de forma lógica, facilitando a aplicação de algoritmos de controle e priorização.
A principal estrutura adotada é a fila (queue), utilizada para representar os módulos que se encontram aguardando autorização de pouso. Essa estrutura segue o princípio FIFO (First In, First Out), no qual o primeiro módulo a chegar à órbita é, inicialmente, o primeiro a ser considerado para pouso. No entanto, essa ordem pode ser ajustada dinamicamente conforme os critérios de prioridade definidos pelo sistema, como nível de combustível e criticidade da carga.
Além da fila principal, foram utilizadas listas auxiliares para representar os diferentes estados operacionais dos módulos ao longo do processo de decisão. Essas listas permitem classificar os módulos conforme sua situação após a análise das condições de pouso.
A lista de módulos pousados armazena aqueles que já receberam autorização e concluíram o processo de descida com sucesso. Essa estrutura é importante para o acompanhamento da evolução da base e para controle histórico das operações realizadas.
A lista de módulos em espera reúne aqueles que, apesar de estarem aptos para pouso, não foram priorizados no momento devido a limitações operacionais ou à presença de módulos mais críticos. Esses módulos permanecem na fila de controle e podem ser reavaliados em ciclos posteriores.
Por sua vez, a lista de módulos em alerta é destinada àqueles que apresentam risco elevado, como baixo nível de combustível ou condições operacionais adversas. Esses módulos exigem atenção imediata do sistema, podendo ter sua prioridade elevada automaticamente para evitar falhas na missão.
2. Definição e representação das regras de decisão por meio de portas lógicas
O processo de autorização de pouso dos módulos exige a definição de regras claras e objetivas, capazes de avaliar as condições operacionais de forma rápida e confiável. Para isso, foram estabelecidas condições críticas baseadas em variáveis fundamentais, como nível de combustível, condições atmosféricas simuladas, disponibilidade da área de pouso e integridade dos sensores do módulo.
O nível de combustível é um dos principais fatores de decisão, pois está diretamente relacionado à capacidade do módulo de realizar uma descida segura. Módulos com combustível abaixo de um determinado limite são considerados em situação crítica, podendo ter prioridade elevada ou exigir autorização imediata de pouso.
As condições atmosféricas simuladas representam fatores externos que podem impactar a segurança da operação, como tempestades de poeira ou variações extremas de temperatura. Quando essas condições são desfavoráveis, o sistema pode bloquear temporariamente o pouso, independentemente das demais variáveis.
A disponibilidade da área de pouso também é um critério essencial, uma vez que o sistema considera que apenas um módulo pode pousar por vez. Caso a área esteja ocupada ou indisponível, o pouso deve ser automaticamente adiado.
Por fim, a integridade dos sensores garante que o módulo possui capacidade adequada de navegação e controle durante a descida. Falhas nos sensores representam alto risco, resultando no bloqueio imediato da autorização de pouso.
Essas condições foram traduzidas em expressões booleanas, permitindo a implementação de um sistema de decisão baseado em lógica digital. De forma geral, a autorização de pouso pode ser representada pela seguinte expressão:
AUTORIZAR_POUSO = (combustível_suficiente AND sensores_ok AND area_disponivel AND condicoes_atmosfericas_favoraveis)
Além disso, situações de alerta podem ser representadas por expressões que identificam risco elevado, como:
ALERTA = (combustível_baixo OR sensores_com_falha)
A utilização de operadores lógicos como AND, OR e NOT permite combinar múltiplas condições e simular o comportamento de sistemas reais de controle. Por exemplo, o operador AND exige que todas as condições sejam verdadeiras para que o pouso seja autorizado, enquanto o operador OR identifica cenários de risco quando ao menos uma condição crítica é atendida.
Do ponto de vista visual, essas expressões podem ser representadas por meio de diagramas de portas lógicas, nos quais cada variável de entrada corresponde a um sinal e a saída representa a decisão final do sistema. Essa abordagem facilita a compreensão do fluxo de decisão e evidencia como diferentes fatores são combinados para determinar a autorização ou o adiamento do pouso.
Dessa forma, a aplicação de lógica booleana e portas lógicas no sistema MGPEB permite estruturar um modelo de decisão robusto, transparente e alinhado aos princípios fundamentais da computação e da engenharia de sistemas.
3. Implementação do protótipo do MGPEB em Python
Para validar o modelo proposto, foi desenvolvido um protótipo em Python capaz de simular o gerenciamento do pouso dos módulos. O sistema utiliza estruturas lineares, algoritmos simples de busca e ordenação, além de regras lógicas para decisão de pouso.

# Cadastro dos módulos
# =========================
fila_pouso = [
    {"nome": "Energia", "combustivel": 15, "massa": 2000, "criticidade": "alta", "horario": 1, "sensores": True},
    {"nome": "Habitação", "combustivel": 70, "massa": 1500, "criticidade": "alta", "horario": 2, "sensores": True},
    {"nome": "Laboratório", "combustivel": 80, "massa": 1200, "criticidade": "baixa", "horario": 3, "sensores": True},
    {"nome": "Logística", "combustivel": 60, "massa": 1800, "criticidade": "media", "horario": 4, "sensores": True},
    {"nome": "Suporte Médico", "combustivel": 50, "massa": 1000, "criticidade": "alta", "horario": 5, "sensores": True}
]

pousados = []
espera = []
alerta = []

# =========================
# Função de busca
# =========================

def buscar_menor_combustivel(lista):
    menor = lista[0]
    for modulo in lista:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor

# =========================
# Função de ordenação (simples)
# =========================

def ordenar_por_prioridade(lista):
    # Critérios: combustível baixo, criticidade, massa
    def calcular_prioridade(m):
        prioridade = 0

        if m["combustivel"] < 20:
            prioridade += 3
        if m["criticidade"] == "alta":
            prioridade += 2
        if m["massa"] > 1500:
            prioridade += 1

        return prioridade

    # Ordena do maior para o menor (mais prioridade primeiro)
    lista.sort(key=calcular_prioridade, reverse=True)

# =========================
# Função de decisão (lógica booleana)
# =========================

def decidir_pouso(modulo, area_disponivel, clima_ok):

    combustivel_suficiente = modulo["combustivel"] > 10
    sensores_ok = modulo["sensores"]

    # Regra principal (AND)
    if combustivel_suficiente and sensores_ok and area_disponivel and clima_ok:
        return "POUSAR"

    # Regra de alerta (OR)
    elif modulo["combustivel"] <= 10 or not sensores_ok:
        return "ALERTA"

    else:
        return "ESPERAR"

# =========================
# Simulação do sistema
# =========================

area_disponivel = True
clima_ok = True

# Ordena a fila antes da decisão
ordenar_por_prioridade(fila_pouso)

for modulo in fila_pouso:

    decisao = decidir_pouso(modulo, area_disponivel, clima_ok)

    if decisao == "POUSAR" and area_disponivel:
        pousados.append(modulo)
        area_disponivel = False  # só um pouso por vez

    elif decisao == "ALERTA":
        alerta.append(modulo)

    else:
        espera.append(modulo)

# =========================
# Resultados
# =========================

print("Pousados:")
for m in pousados:
    print(m["nome"])

print("\nEm espera:")
for m in espera:
    print(m["nome"])

print("\nEm alerta:")
for m in alerta:
    print(m["nome"])

Explicação do funcionamento
O sistema inicia com o cadastro dos módulos em uma lista que representa a fila de pouso. CadaAnexo de estruturas de dados (pode ser parte do relatório), descrevendo como listas, filas e pilhas foram utilizadas no projeto, com exemplos concretos.L módulo possui atributos relevantes para a tomada de decisão.
Em seguida, é implementado um algoritmo de busca simples para identificar módulos com menor nível de combustível, demonstrando a aplicação de busca linear.
A ordenação da fila é realizada com base em critérios definidos, como combustível, criticidade e massa, utilizando uma função de prioridade que permite reorganizar os módulos antes da tomada de decisão.
A função decidir_pouso aplica regras lógicas baseadas em operadores booleanos (AND, OR), simulando o funcionamento de portas lógicas. Essa função determina se o módulo deve pousar, entrar em alerta ou permanecer em espera.
Por fim, o sistema simula o processo de pouso, distribuindo os módulos entre listas de pousados, espera e alerta, conforme as condições avaliadas.

4. Modelagem de funções matemáticas aplicadas ao pouso
Para complementar a análise do processo de pouso dos módulos, foi selecionado um fenômeno físico relevante: a variação da altura do módulo em função do tempo durante a descida. Esse fenômeno é fundamental para compreender o comportamento do módulo ao se aproximar da superfície marciana e para auxiliar na tomada de decisões operacionais, como o acionamento de retrofoguetes e a redução da velocidade.
Considerando um modelo simplificado, a descida pode ser representada por uma função quadrática, típica de movimentos sob ação da gravidade. A função pode ser expressa da seguinte forma:
h(t) = h₀ - vt – (1/2)gt²

onde:
    • h(t) representa a altura do módulo no instante t; 
    • h₀ é a altura inicial (início da descida); 
    • v é a velocidade inicial de descida; 
    • g é a aceleração gravitacional de Marte; 
    • t é o tempo. 
Essa função descreve uma curva decrescente ao longo do tempo, indicando que a altura diminui de forma acelerada devido à ação da gravidade. À medida que o tempo aumenta, o termo quadrático (t²) passa a ter maior influência, resultando em uma descida cada vez mais rápida.
Do ponto de vista qualitativo, o gráfico dessa função apresenta uma trajetória parabólica decrescente. No início da descida, a variação da altura é mais lenta, mas, com o passar do tempo, a velocidade aumenta, tornando a descida mais crítica. Caso nenhuma intervenção seja realizada, o módulo atingirá a superfície com velocidade elevada, comprometendo a segurança do pouso.
Essa modelagem permite identificar pontos críticos durante a descida, especialmente o momento em que a velocidade se torna elevada demais. A partir dessa análise, torna-se possível definir o instante ideal para o acionamento dos retrofoguetes, que atuam reduzindo a velocidade e garantindo um pouso controlado.
Além disso, essa função auxilia na definição de políticas operacionais dentro do MGPEB. Por exemplo, se múltiplos módulos estiverem em fase de descida simultaneamente, o sistema pode limitar a quantidade de pousos em andamento, evitando sobrecarga operacional e aumentando a segurança da missão.
Portanto, a utilização de funções matemáticas para modelar o comportamento físico dos módulos durante o pouso contribui diretamente para a tomada de decisões mais precisas, permitindo antecipar riscos e otimizar o controle do processo de descida. Essa abordagem integra conceitos matemáticos à engenharia de sistemas, fortalecendo a robustez do módulo de gerenciamento de pouso.
5. Contextualização do MGPEB à luz da evolução da computação
O desenvolvimento do MGPEB pode ser relacionado à evolução da computação, desde os primeiros computadores de propósito geral até os atuais sistemas embarcados utilizados em missões espaciais. Os primeiros computadores, embora limitados em desempenho e capacidade, estabeleceram as bases para os algoritmos e estruturas de dados utilizados atualmente.
Com o avanço tecnológico, surgiram sistemas embarcados, projetados para executar funções específicas com alta confiabilidade. Em missões como a simulação em Marte, esses sistemas operam sob fortes restrições, como baixa capacidade de processamento, memória limitada, consumo reduzido de energia e exposição à radiação.
Diante dessas limitações, o MGPEB foi projetado com foco em simplicidade e eficiência, utilizando estruturas lineares, algoritmos básicos de busca e ordenação, e lógica booleana para tomada de decisão. Essas escolhas garantem um sistema mais previsível, robusto e adequado a ambientes críticos, onde a confiabilidade é essencial.

6. Incorporação de princípios ESG na concepção da base Aurora
A base Aurora deve operar com foco em sustentabilidade, responsabilidade e ética. A escolha da área de pouso deve evitar regiões sensíveis de Marte, reduzindo impactos ambientais. A gestão de energia e recursos deve priorizar eficiência e uso controlado, como energia solar e reaproveitamento de materiais.
No aspecto social, é essencial garantir segurança, bem-estar e acesso igualitário aos recursos para todos os tripulantes. Já na governança, as decisões devem ser transparentes, com regras claras e supervisão humana, mesmo com uso de sistemas automatizados.
Assim, a aplicação de princípios ESG assegura uma operação mais sustentável e responsável da colônia marciana.
