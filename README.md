# Projeto Aurora Siger - Fase 2 🚀

## Descrição do Projeto

Este projeto desenvolve o **Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)** para a missão Aurora Siger em Marte.

O objetivo é simular a chegada de diferentes módulos à órbita marciana e definir critérios técnicos para autorização de pouso utilizando conceitos fundamentais de Ciência da Computação.

---

# 1. Modelagem do cenário de pouso e fila de módulos

Os módulos representam componentes essenciais para a construção inicial da colônia marciana:

- Habitação  
- Energia  
- Laboratório  
- Logística  
- Suporte Médico  

Cada módulo possui funções específicas e diferentes níveis de criticidade operacional.

## Atributos utilizados

Cada módulo foi representado pelos seguintes atributos:

- Nível de combustível  
- Massa  
- Criticidade da carga  
- Horário estimado de chegada  

## Estrutura principal

Foi utilizada uma estrutura de **fila (queue)** para organizar os módulos aguardando autorização de pouso.

A fila segue o princípio:

**FIFO (First In, First Out)**

Entretanto, a ordem pode ser alterada conforme regras de prioridade.

## Listas auxiliares

- Lista de módulos pousados  
- Lista de módulos em espera  
- Lista de módulos em alerta  

## Exemplo
---
```python
fila_pouso = [
    {"nome": "Energia", "combustivel": 15, "massa": 2000},
    {"nome": "Habitação", "combustivel": 70, "massa": 1500}
]
2. Regras de decisão com portas lógicas

O sistema avalia:

Combustível disponível
Condições atmosféricas
Disponibilidade da área de pouso
Integridade dos sensores
Regra principal
AUTORIZAR_POUSO = (
    combustivel_suficiente
    and sensores_ok
    and area_disponivel
    and clima_favoravel
)
Regra de alerta
ALERTA = (
    combustivel_baixo
    or sensores_com_falha
)
Operadores utilizados
AND
OR
NOT

Essas regras simulam o funcionamento de portas lógicas aplicadas ao sistema de pouso.

3. Implementação do protótipo em Python

O sistema foi desenvolvido em Python para simular:

Cadastro dos módulos
Busca por menor combustível
Ordenação por prioridade
Decisão automática de pouso
Estruturas utilizadas
Listas
Filas
Algoritmos de busca
Algoritmos de ordenação
Funções implementadas
Busca
def buscar_menor_combustivel(lista):
Ordenação
def ordenar_por_prioridade(lista):
Decisão de pouso
def decidir_pouso(modulo, area_disponivel, clima_ok):
Resultados da simulação

O sistema classifica os módulos em:

Pousados
Em espera
Em alerta
4. Modelagem matemática aplicada ao pouso

Foi utilizada uma função quadrática para representar a altura durante a descida:

h(t) = h₀ - vt - (1/2)gt²

Onde:

h(t) = altura no tempo t
h₀ = altura inicial
v = velocidade inicial
g = gravidade de Marte
t = tempo
Aplicações práticas

A função auxilia em decisões como:

Acionamento de retrofoguetes
Controle de velocidade
Segurança da aterrissagem
5. Evolução da computação

O projeto foi relacionado à evolução dos computadores:

Primeiros computadores de propósito geral
Sistemas embarcados modernos
Missões espaciais automatizadas
Limitações em Marte
Memória limitada
Baixo processamento
Consumo energético reduzido
Exposição à radiação

Por isso, o sistema utiliza algoritmos simples e eficientes.

6. Princípios ESG

A base Aurora foi projetada considerando sustentabilidade.

Ambiental
Escolha responsável da área de pouso
Redução de impactos ambientais
Social
Segurança dos tripulantes
Distribuição justa de recursos
Governança
Transparência nas decisões
Supervisão humana dos sistemas automáticos
Tecnologias utilizadas
Python
Git
GitHub
Linux
LibreOffice
Arquivos do projeto
CENARIO.py
RELATORIOodt.odt
README.md
