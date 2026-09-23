# 🧠 MEMORY.md — Memória de Trabalho do Agente de IA

> **ATENÇÃO PARA AGENTES DE IA / LLMs:**
> Este arquivo contém a memória persistente de arquitetura, decisões técnicas, convenções de código e restrições pedagógicas deste repositório.
> **LEIA ESTE ARQUIVO ANTES DE PROPOR OU EXECUTAR QUALQUER MODIFICAÇÃO NO CÓDIGO.**

---

## 📌 Contexto Geral do Projeto

* **Nome do Projeto:** Controle de Estoque — Farmácia Vida+
* **Propósito Primário:** Demonstração acadêmica e ensino de Lógica de Programação Estruturada/Procedural.
* **Linguagem:** Python 3.8+ (Apenas biblioteca padrão: `tkinter`, `tkinter.ttk`, `tkinter.messagebox`).
* **Interface Gráfica:** GUI nativa via `ttk.Style` utilizando layout responsivo em `grid`/`pack`.

---

## 🚨 REGRAS ABSOLUTAS E RESTRIÇÕES ARQUITETÔNICAS (CRÍTICO)

Qualquer alteração feita por um agente de IA **DEVE SEGUIR RIGOROSAMENTE** as seguintes diretrizes:

### 1. Proibição Estrita de Orientação a Objetos (POO)
* 🛑 **NUNCA use a palavra-chave `class`.**
* 🛑 **NUNCA crie instâncias de objetos personalizados.**
* Toda a lógica DEVE ser implementada utilizando **paradigma procedural puro**, funções globais/locais e manipulação de estado via estruturas de dados nativas (`list`, `tuple`, `dict`).

### 2. Contrato Didático — Comentários "Por Debaixo dos Panos"
* Sempre que utilizar **funções nativas de alto nível**, **atalhos** ou **métodos utilitários** (ex: `sum()`, `len()`, `enumerate()`, `isnumeric()`, operador `in`), você **É OBRIGADO** a incluir um comentário explicativo no código.
* O comentário deve explicar explicitamente o que a função faz no nível do processador e qual estrutura/algoritmo tradicional (loop de acumulação, busca linear, verificação de tabela ASCII) ela substitui.

### 3. Evidência das Estruturas de Böhm-Jacopini
* O código deve manter claros os blocos de:
  1. **Sequência:** Fluxos lineares de atribuição e leitura.
  2. **Seleção:** Estruturas condicionais (`if`, `elif`, `else`) para validação e lógica de negócio.
  3. **Repetição:** Laços de iteração (`for`, `while`) para percorrer vetores e atualizar a interface.

---

## 🏗️ Estrutura de Dados e Estado Global

### Mapeamento do Estoque
* **Modelo:** Vetor (lista Python) fixo de **10 posições de números inteiros positivos**.
* **Variável do Estoque:** `estoque = [10, 5, 2, 0, 15, 8, 20, 1, 12, 4]`
* **Vetor de Mapeamento (Nomes):** `NOMBRES_MEDICAMENTOS` (Lista de 10 strings com os nomes fixos dos remédios).
* **Relação de Índice Fixo:**
  * `0`: Dipirona
  * `1`: Paracetamol
  * `2`: Ibuprofeno
  * `3`: Amoxicilina
  * `4`: Omeprazol
  * `5`: Loratadina
  * `6`: Dorflex
  * `7`: Buscopan
  * `8`: Vitamina C
  * `9`: Azitromicina

---

## ⚙️ Regras de Negócio Implementadas

1. **Consulta/Exibição em Tempo Real:** A tabela (`ttk.Treeview`) reflete instantaneamente o conteúdo do vetor `estoque`.
2. **Entrada de Medicamentos:**
   * O usuário seleciona o medicamento no `Combobox` e digita um valor no `Entry`.
   * **Validação:** Apenas valores numéricos inteiros maiores que zero são aceitos (validado via `.isnumeric()`).
   * Adiciona o valor à posição correspondente no vetor (`estoque[i] += qtd`).
3. **Saída de Medicamentos (Venda):**
   * Decrementa em 1 unidade a posição correspondente do vetor (`estoque[i] -= 1`).
   * **Trava de Saldo Negativo:** Se `estoque[i] <= 0`, impede a operação e exibe um `messagebox.showerror`.
4. **Encerramento:**
   * Utiliza a função `sum(estoque)` para calcular o total armazenado.
   * Exibe um `messagebox.showinfo` detalhando a quantidade de cada item e a soma geral antes de fechar a janela com `.destroy()`.

---

## 📝 Diretrizes para Futuras Atualizações (Para o Agente de IA)

Ao receber solicitações para adicionar novas funcionalidades (ex: as fases descritas no `ROADMAP.md`):

* **Manter Arquivo Único ou Módulos Procedurais:** Mantenha o código no padrão procedural. Se for criar novos arquivos `.py`, crie-os como módulos de funções procedurais, sem criar classes.
* **Persistência de Dados (Próxima Fase):** Ao implementar leitura/escrita em arquivo (`.txt` ou `.csv`), utilize as funções nativas de manipulação de arquivo (`open()`, `read()`, `write()`) acompanhadas de comentários didáticos sobre o gerenciamento de buffers e ponteiros de arquivo.
* **Preservar Nomes de Componentes:** Mantenha as referências globais da interface (`janela_principal`, `combo_medicamentos`, `campo_quantidade`, `tabela_estoque`) coerentes com o arquivo `main.py` original.