# 💱 Conversor de Moedas (Python)

Este projeto é um sistema de conversão de moedas via linha de comando (CLI), desenvolvido para praticar lógica de programação, manipulação de dados e estruturação de código em Python.

## 🚀 Histórico de Versões

### Versão 1.0: A Lógica Inicial
O foco desta versão foi validar a lógica matemática e o fluxo básico do programa.
* **Funcionalidade:** Conversão de Moedas Estrangeiras (Dólar, Euro, etc.) para Real Brasileiro (BRL).
* **Estrutura:** Uso extensivo de condicionais (`if/elif/else`) para verificar qual moeda foi escolhida.
* **Armazenamento:** As taxas e nomes estavam fixos dentro das condições lógicas.
* **Entrada de Dados:** `input` simples dentro de um loop `while`.

### Versão 1.1: Refatoração e Organização (Versão Atual)
O objetivo desta versão foi limpar o código (Clean Code), tornando-o mais eficiente e fácil de manter.
* **Dicionários:** Substituição das cadeias de `if/elif` por Dicionários (`dict`), atuando como um banco de dados para Nomes, Taxas e Símbolos.
* **Tuplas:** Uso de tuplas `(Origem, Destino)` como chaves para identificar as taxas de conversão.
* **Função Dinâmica:** A função `conversor_moeda` foi reescrita para aceitar argumentos (`valor`, `id_origem`, `id_destino`), tornando-a independente de variáveis globais.
* **UX (Experiência do Usuário):** Adição de símbolos monetários ($, €, £) nos resultados.
* **Tratamento de Erros:** Melhoria no `try/except` para capturar entradas inválidas e chaves de dicionário inexistentes.

## 🛠️ Tecnologias Utilizadas
* Python 3
* Estruturas de Dados: Listas, Dicionários, Tuplas
* Controle de Fluxo: While, Try/Except
---
