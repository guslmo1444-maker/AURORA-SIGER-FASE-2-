# Projeto Aurora Siger - Fase 2 🚀

## Descrição do Projeto

Este projeto desenvolve o **MGPEB (Módulo de Gerenciamento de Pouso e Estabilização de Base)** para a missão Aurora Siger em Marte.

O objetivo é simular a chegada de módulos à órbita marciana e definir critérios técnicos para autorização de pouso utilizando conceitos de Ciência da Computação.

---

## 1. Modelagem do cenário de pouso

Os módulos representam estruturas essenciais para a construção da colônia:

- Habitação  
- Energia  
- Laboratório  
- Logística  
- Suporte Médico  

Cada módulo possui funções específicas e níveis diferentes de criticidade operacional.

### Atributos dos módulos

- Nível de combustível  
- Massa  
- Criticidade da carga  
- Horário estimado de chegada  

### Estrutura principal

Foi utilizada uma estrutura de **fila (queue)** para organizar os módulos aguardando autorização de pouso.

Princípio utilizado:

**FIFO (First In, First Out)**

A ordem pode ser alterada conforme prioridade operacional.

### Listas auxiliares

- Módulos pousados  
- Módulos em espera  
- Módulos em alerta  

### Exemplo de estrutura

```python
fila_pouso = [
    {"nome": "Energia", "combustivel": 15, "massa": 2000},
    {"nome": "Habitação", "combustivel": 70, "massa": 1500}
]
