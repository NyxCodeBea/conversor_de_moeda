# 💱 Conversor de Moedas

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

### Versão 1.2: Conversão Bidirecional (Ida e Volta)
Esta atualização focou na flexibilidade matemática e na integridade dos dados, permitindo conversões de e para a moeda nacional.
* **Fluxo Bidirecional:** Implementação da lógica para converter **Real Brasileiro → Moeda Estrangeira**, além do fluxo original.
* **Lógica Matemática Inversa:** Aplicação automática de **divisão** quando a origem é Real, e **multiplicação** quando a origem é estrangeira.
* **Otimização de Dicionários:** Reutilização das taxas existentes invertendo a busca das chaves `[origem, destino]` para `[destino, origem]` quando necessário, evitando a duplicação de dados manuais.
* **Expansão de Dados:** Inclusão completa do "Real Brasileiro" (ID 6) e seu símbolo (R$) em todas as estruturas de dados para evitar erros de chave (`KeyError`).

## 🛠️ Tecnologias Utilizadas
* Python 3
* Estruturas de Dados: Listas, Dicionários, Tuplas
* Controle de Fluxo: While, Try/Except
---
