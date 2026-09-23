# ==============================================================================
# SISTEMA DE CONTROLE DE ESTOQUE - FARMÁCIA VIDA+
# Paradigma: Programação Estruturada/Procedural Pura (sem uso de classes)
# Finalidade: Demonstrativo Pedagógico das Estruturas de Böhm-Jacopini
# ==============================================================================

import tkinter as tk
from tkinter import messagebox, ttk

# ------------------------------------------------------------------------------
# 1. VARIÁVEIS E ESTRUTURAS DE DADOS GLOBAIS (ESTADO DO PROGRAMA)
# ------------------------------------------------------------------------------

# Vetor de 10 posições fixas com os nomes dos medicamentos (Mapeamento Índices -> Nomes)
NOMBRES_MEDICAMENTOS = [
    "Dipirona",
    "Paracetamol",
    "Ibuprofeno",
    "Amoxicilina",
    "Omeprazol",
    "Loratadina",
    "Dorflex",
    "Buscopan",
    "Vitamina C",
    "Azitromicina",
]

# Vetor de 10 posições representando as quantidades disponíveis no estoque
# Posição i do vetor equivale ao medicamento na posição i da lista de nomes
estoque = [10, 5, 2, 0, 15, 8, 20, 1, 12, 4]  # Valores iniciais para simulação

# Referências globais para elementos da Interface Gráfica
janela_principal = None
combo_medicamentos = None
campo_quantidade = None
tabela_estoque = None


# ------------------------------------------------------------------------------
# 2. FUNÇÕES PROCEDURAIS E REGRAS DE NEGÓCIO
# ------------------------------------------------------------------------------


def atualizar_exibicao_tabela():
    """Atualiza visualmente a lista/tabela de medicamentos e suas quantidades em tempo real.

    Estrutura de Repetição (Böhm-Jacopini): Percorre o vetor de estoque.
    """
    # Limpa as linhas atuais da tabela
    # O método get_children() retorna uma tupla com os IDs dos itens da tabela
    # Usa um loop para remover individualmente cada linha
    for item in tabela_estoque.get_children():
        tabela_estoque.delete(item)

    # REPETIÇÃO: Iteração para povoar a tabela com os dados atualizados dos vetores
    # NOTA PEDAGÓGICA SOBRE ATALHO NATIVO:
    # A função built-in 'enumerate()' gera pares (índice, valor) a cada iteração.
    # "Por debaixo dos panos": Substitui o controle manual de uma variável de
    # contagem (ex: i = 0; while i < len(estoque): i += 1).
    for indice, quantidade in enumerate(estoque):
        nome = NOMBRES_MEDICAMENTOS[indice]
        status = "Disponível" if quantidade > 0 else "SEM ESTOQUE"

        # SELEÇÃO: Destaca visualmente os medicamentos zerados
        tabela_estoque.insert(
            "", "end", values=(indice, nome, quantidade, status)
        )


def registrar_entrada():
    """Adiciona a quantidade informada pelo usuário ao estoque do medicamento selecionado.

    Fase de Sequência -> Seleção -> Atualização -> Exibição.
    """
    # 1. SEQUÊNCIA: Obtenção dos dados digitados/selecionados
    posicao_selecionada = combo_medicamentos.current()
    qtd_texto = campo_quantidade.get().strip()

    # 2. SELEÇÃO (Validação de Entrada)
    if posicao_selecionada == -1:
        messagebox.showwarning(
            "Aviso", "Por favor, selecione um medicamento da lista."
        )
        return

    # NOTA PEDAGÓGICA SOBRE ATALHO NATIVO:
    # O método de string '.isnumeric()' checa se todos os caracteres da string são dígitos.
    # "Por debaixo dos panos": Substitui uma verificação caractere a caractere checando
    # os códigos ASCII (ex: '0' <= char <= '9') e o tratamento manual de exceções de conversão.
    if not qtd_texto.isnumeric() or int(qtd_texto) <= 0:
        messagebox.showerror(
            "Erro de Validação",
            "A quantidade de entrada deve ser um número inteiro positivo!",
        )
        return

    quantidade_adicionar = int(qtd_texto)

    # 3. ATUALIZAÇÃO DO ESTOQUE (Incremento Procedural)
    # Soma o valor digitado diretamente no vetor na posição correspondente
    estoque[posicao_selecionada] += quantidade_adicionar

    # Feedback ao usuário e atualização da interface
    nome_med = NOMBRES_MEDICAMENTOS[posicao_selecionada]
    messagebox.showinfo(
        "Sucesso",
        f"Registrada a entrada de {quantidade_adicionar} unidade(s) de {nome_med}.",
    )

    campo_quantidade.delete(0, tk.END)
    atualizar_exibicao_tabela()


def registrar_saida_unitaria():
    """Decrementa em 1 a quantidade disponível do medicamento selecionado.

    Garante que a quantidade não fique menor que zero (Regra de Negócio).
    """
    # 1. SEQUÊNCIA: Identificação do item selecionado
    posicao_selecionada = combo_medicamentos.current()

    # 2. SELEÇÃO: Validação de escolha
    if posicao_selecionada == -1:
        messagebox.showwarning(
            "Aviso", "Por favor, selecione um medicamento para a venda."
        )
        return

    # 3. SELEÇÃO (Regra de Negócio: Estoque Insuficiente / Quantidade Não Negativa)
    quantidade_atual = estoque[posicao_selecionada]
    nome_med = NOMBRES_MEDICAMENTOS[posicao_selecionada]

    if quantidade_atual <= 0:
        messagebox.showerror(
            "Estoque Esgotado",
            f"O medicamento {nome_med} está SEM ESTOQUE!\nNão é possível registrar a saída.",
        )
        return

    # 4. ATUALIZAÇÃO DO ESTOQUE (Decremento Unutário)
    estoque[posicao_selecionada] -= 1

    # Feedback e sincronização visual
    messagebox.showinfo(
        "Venda Realizada", f"Saída de 1 unidade de {nome_med} registrada!"
    )
    atualizar_exibicao_tabela()


def encerrar_sistema():
    """Calcula o resumo do estoque utilizando funções de acumulação e encerra a aplicação.

    Apresenta a quantidade por medicamento e o total geral armazenado.
    """
    # NOTA PEDAGÓGICA SOBRE ATALHO NATIVO:
    # A função built-in 'sum()' calcula a soma total de todos os elementos da lista.
    # "Por debaixo dos panos": Substitui um algoritmo manual de acumulação:
    #   total = 0
    #   for qtd in estoque:
    #       total += qtd
    total_unidades = sum(estoque)

    # REPETIÇÃO: Construção da mensagem textual linha a linha
    resumo_texto = "=== RESUMO FINAL DO ESTOQUE ===\n\n"

    # NOTA PEDAGÓGICA SOBRE ATALHO NATIVO:
    # A função built-in 'len()' retorna a quantidade de itens na coleção.
    # "Por debaixo dos panos": Acessa diretamente a propriedade de tamanho guardada na
    # estrutura da lista em C, evitando a contagem manual elemento a elemento via loop.
    tamanho_vetor = len(estoque)

    for i in range(tamanho_vetor):
        resumo_texto += f"• {NOMBRES_MEDICAMENTOS[i]}: {estoque[i]} unidade(s)\n"

    resumo_texto += f"\n----------------------------------"
    resumo_texto += f"\nTOTAL DE UNIDADES EM ESTOQUE: {total_unidades}"

    # Exibição do relatório final
    messagebox.showinfo("Encerramento do Expediente", resumo_texto)

    # Destruição da janela e finalização do programa
    janela_principal.destroy()


# ------------------------------------------------------------------------------
# 3. CONSTRUÇÃO PROCEDURAL DA INTERFACE GRÁFICA (TKINTER / TTK)
# ------------------------------------------------------------------------------


def construir_interface():
    """Função responsável por instanciar a janela, configurar o tema ttk e

    organizar todos os componentes no gerenciador de geometrias (Grid).
    """
    global janela_principal, combo_medicamentos, campo_quantidade, tabela_estoque

    # Janela Principal
    janela_principal = tk.Tk()
    janela_principal.title("Farmácia Vida+ | Controle de Estoque")
    janela_principal.geometry("620x520")
    janela_principal.resizable(False, False)

    # Aplicação de Estilo Nativo (ttk.Style)
    estilo = ttk.Style()
    # Tenta utilizar o tema nativo 'vista' ou 'clam' dependendo do sistema operacional
    # NOTA PEDAGÓGICA SOBRE ATALHO NATIVO:
    # O operador 'in' busca a existência de um elemento na sequência retornada por theme_names().
    # "Por debaixo dos panos": Realiza uma busca linear O(n) iterando sobre os temas do Tkinter.
    if "vista" in estilo.theme_names():
        estilo.theme_use("vista")
    else:
        estilo.theme_use("clam")

    # Frame Superior: Painel de Operações
    frame_operacoes = ttk.LabelFrame(
        janela_principal, text=" Registros e Movimentações ", padding=10
    )
    frame_operacoes.pack(fill="x", padx=15, pady=10)

    # Componentes de Entrada
    lbl_med = ttk.Label(frame_operacoes, text="Medicamento:")
    lbl_med.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    combo_medicamentos = ttk.Combobox(
        frame_operacoes, values=NOMBRES_MEDICAMENTOS, state="readonly", width=25
    )
    combo_medicamentos.grid(row=0, column=1, padx=5, pady=5)

    lbl_qtd = ttk.Label(frame_operacoes, text="Qtd. Entrada:")
    lbl_qtd.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    campo_quantidade = ttk.Entry(frame_operacoes, width=28)
    campo_quantidade.grid(row=1, column=1, padx=5, pady=5)

    # Botões de Ação
    btn_entrada = ttk.Button(
        frame_operacoes, text="➕ Adicionar Estoque", command=registrar_entrada
    )
    btn_entrada.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

    btn_saida = ttk.Button(
        frame_operacoes,
        text="🛒 Registrar Venda (-1)",
        command=registrar_saida_unitaria,
    )
    btn_saida.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

    # Frame Central: Exibição do Estoque (Treeview / Tabela)
    frame_tabela = ttk.LabelFrame(
        janela_principal, text=" Estado Atual do Estoque ", padding=10
    )
    frame_tabela.pack(fill="both", expand=True, padx=15, pady=5)

    # Configuração da Treeview (Exibição dos 10 elementos do vetor)
    colunas = ("pos", "nome", "qtd", "status")
    tabela_estoque = ttk.Treeview(
        frame_tabela, columns=colunas, show="headings", height=10
    )

    tabela_estoque.heading("pos", text="Posição")
    tabela_estoque.heading("nome", text="Medicamento")
    tabela_estoque.heading("qtd", text="Qtd Disponível")
    tabela_estoque.heading("status", text="Status")

    tabela_estoque.column("pos", width=60, anchor="center")
    tabela_estoque.column("nome", width=200, anchor="w")
    tabela_estoque.column("qtd", width=110, anchor="center")
    tabela_estoque.column("status", width=120, anchor="center")

    tabela_estoque.pack(fill="both", expand=True)

    # Frame Inferior: Encerramento
    frame_rodape = ttk.Frame(janela_principal, padding=10)
    frame_rodape.pack(fill="x", padx=15, pady=5)

    btn_encerrar = ttk.Button(
        frame_rodape, text="🛑 Encerrar Expediente", command=encerrar_sistema
    )
    btn_encerrar.pack(side="right")

    # Carga Inicial de Dados (DADO que o sistema seja iniciado... ENTÃO o estoque será carregado)
    atualizar_exibicao_tabela()

    # Inicia o Loop Principal da Interface Gráfica
    janela_principal.mainloop()


# ------------------------------------------------------------------------------
# 4. PONTO DE ENTRADA DO PROGRAMA (SEQUÊNCIA PRINCIPAL)
# ------------------------------------------------------------------------------
# Inicia a execução chamando a construção da interface
construir_interface()