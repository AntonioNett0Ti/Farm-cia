# 💊 Controle de Estoque - Farmácia Vida+

> Sistema desktop para controle procedural de estoque de medicamentos com interface gráfica em Python (Tkinter/TTK).

---

## 📌 Sobre o Projeto

Este projeto consiste em uma aplicação de controle de estoque desenvolvida para a **Farmácia Vida+**. Seu objetivo principal é permitir o acompanhamento em tempo real, a entrada de novas remessas e a realização de vendas de medicamentos de forma simples e intuitiva.

Além de atender às regras de negócio de um ambiente farmacêutico, o código foi projetado com foco **pedagógico**, servindo como modelo acadêmico para o ensino de **Lógica de Programação Estruturada/Procedural**.

---

## 🎯 Objetivos Pedagógicos & Paradigma

O projeto foi construído sob **restrições pedagógicas rigorosas**:

1. **Paradigma Procedural Puro**:
   * Não utiliza Orientação a Objetos (`class`).
   * Utiliza apenas variáveis de escopo local/global, vetores (listas) e funções procedurais.
2. **Estruturas de Controle de Böhm-Jacopini**:
   * O fluxo do código evidencia com clareza os três pilares do paradigma estruturado: **Sequência**, **Seleção** (`if`/`else`) e **Repetição** (`for`/`while`).
3. **Análise de Métodos Embutidos ("Por Debaixo dos Panos")**:
   * Cada função de alto nível ou atalho nativo da linguagem (como `sum()`, `enumerate()`, `len()`, `.isnumeric()`) possui comentários detalhando qual algoritmo tradicional de iteração/acumulação ela substitui.

---

## 🛠️ Regras de Negócio e Mapeamento de Dados

O estoque é representado por um **vetor fixo de 10 posições** (índices 0 a 9). Cada posição armazena a quantidade inteira disponível de um medicamento específico:

| Posição (Índice) | Medicamento |
| :---: | :--- |
| **0** | Dipirona |
| **1** | Paracetamol |
| **2** | Ibuprofeno |
| **3** | Amoxicilina |
| **4** | Omeprazol |
| **5** | Loratadina |
| **6** | Dorflex |
| **7** | Buscopan |
| **8** | Vitamina C |
| **9** | Azitromicina |

### Funcionalidades
* **Visualização em Tempo Real**: Tabela atualizada a cada movimentação via `ttk.Treeview`.
* **Entrada de Estoque**: Incremento da quantidade do medicamento selecionado via formulário validado.
* **Saída por Venda**: Decremento unitário (-1) da quantidade do medicamento.
* **Proteção contra Saldo Negativo**: O sistema impede a venda caso o estoque de um medicamento esteja igual a `0`.
* **Encerramento de Expediente**: Exibição de um resumo detalhado com o saldo de cada item e o total geral estocado acumulado (via `sum()`).

---

## 🖥️ Pré-requisitos

Não é necessária a instalação de nenhuma biblioteca externa! O projeto utiliza apenas a biblioteca padrão do Python.

* **Python 3.8** ou superior instalado.
* **VS Code** com a extensão **Python** oficial instalada.

---

## 🚀 Como Executar no VS Code

1. Abra a pasta do projeto no VS Code (`File -> Open Folder...`).
2. Abra o arquivo `main.py`.
3. Pressione a tecla **`F5`** (ou clique no botão **Run** no canto superior direito) para iniciar a aplicação.

---

## 📂 Estrutura do Projeto no VS Code

```text
├── .vscode/          # Configurações do ambiente de desenvolvimento (opcional)
├── main.py           # Código-fonte principal da aplicação
└── README.md         # Documentação e instruções do projeto