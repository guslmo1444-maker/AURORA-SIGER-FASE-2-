# Projeto Aurora Siger - Fase 2 

## Descrição do Projeto

Este projeto desenvolve o **Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)** para a missão Aurora Siger em Marte.

O objetivo é simular a chegada de diferentes módulos à órbita marciana e definir critérios técnicos para autorização de pouso, utilizando conceitos fundamentais de Ciência da Computação.

---

# 1. Modelagem do cenário de pouso e fila de módulos

Os módulos representam componentes essenciais para a construção da colônia marciana:

- Habitação  
- Energia  
- Laboratório  
- Logística  
- Suporte Médico  

Cada módulo possui funções específicas e diferentes níveis de criticidade operacional.

### Atributos utilizados

Cada módulo foi representado pelos seguintes atributos:

- Nível de combustível  
- Massa  
- Criticidade da carga  
- Horário estimado de chegada  

### Estrutura principal

Foi utilizada uma estrutura de **fila (queue)** para organizar os módulos aguardando autorização de pouso.

A fila segue o modelo:

**FIFO (First In, First Out)**

Entretanto, a ordem pode ser alterada conforme regras de prioridade.

### Listas auxiliares

- Lista de módulos pousados  
- Lista de módulos em espera  
- Lista de módulos em alerta  

### Exemplo

```python
fila_pouso = [
    {"nome": "Energia", "combustivel": 15, "massa": 2000},
    {"nome": "Habitação", "combustivel": 70, "massa": 1500}
]
