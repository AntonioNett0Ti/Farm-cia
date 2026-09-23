# 🗺️ Roteiro de Desenvolvimento (Roadmap) - Farmácia Vida+

Este documento registra o histórico de desenvolvimento do sistema de **Controle de Estoque de Medicamentos**, o estado atual da aplicação e os próximos passos planejados para futuras versões.

---

## 📍 Fase 1: MVP Procedural & Interface Base (Concluído)

> **Objetivo:** Implementar a lógica fundamental de controle de estoque usando o paradigma procedural puro e criar a interface gráfica nativa.

- [x] **Estruturação Procedural (Sem Classes)**
  - [x] Criação do vetor fixo de 10 posições para controle de quantidades (`estoque`).
  - [x] Mapeamento dos índices do vetor para os nomes dos medicamentos (`NOMBRES_MEDICAMENTOS`).
  - [x] Implementação do cálculo de saldo total acumulado.

- [x] **Interface Gráfica (Tkinter / TTK)**
  - [x] Layout organizado com `ttk.LabelFrame` e gerenciador de geometrias `grid`.
  - [x] Exibição do estado do estoque em tempo real com `ttk.Treeview`.
  - [x] Formulário de entrada de dados via `ttk.Combobox` e `ttk.Entry`.
  - [x] Aplicação de estilo visual nativo via `ttk.Style`.

- [x] **Regras de Negócio & Validações**
  - [x] Incremento de estoque para recebimento de novos medicamentos.
  - [x] Decremento unitário (-1) para registro de vendas.
  - [x] Trava contra saldo negativo quando a quantidade de um medicamento chega a `0`.
  - [x] Validação de entradas do usuário (prevenção de textos e números negativos).
  - [x] Tela de encerramento de expediente com resumo geral do estoque.

- [x] **Documentação & Didática**
  - [x] Comentários pedagógicos "por debaixo dos panos" em funções de alto nível (`sum()`, `enumerate()`, `len()`, `.isnumeric()`).
  - [x] Documentação das estruturas fundamentais de Böhm-Jacopini (Sequência, Seleção, Repetição).
  - [x] Criação da documentação base no `README.md`.

---

## 📍 Fase 2: Persistência de Dados & Histórico (Próxima Etapa)

> **Objetivo:** Garantir que as alterações do estoque não sejam perdidas ao fechar o programa e registrar todas as movimentações.

- [ ] **Persistência de Arquivos**
  - [ ] Implementar rotina para salvar o vetor de estoque em um arquivo texto (`.txt` ou `.csv`) ao encerrar.
  - [ ] Implementar leitura automática do arquivo de dados na inicialização da aplicação.
- [ ] **Histórico de Movimentações**
  - [ ] Criar log de entradas e saídas com data/hora.
  - [ ] Adicionar aba ou janela secundária para consulta das últimas transações.

---

## 📍 Fase 3: Alertas e Gestão Avançada (Planejado)

> **Objetivo:** Adicionar inteligência operacional para auxiliar o funcionário no controle da farmácia.

- [ ] **Sistema de Alertas**
  - [ ] Destacar em vermelho na tabela medicamentos com estoque crítico (menor ou igual a 2 unidades).
  - [ ] Notificação automática ao iniciar o sistema caso haja itens zerados.
- [ ] **Filtros e Buscas**
  - [ ] Campo de busca rápida de medicamentos pelo nome na tabela.
  - [ ] Ordenação da tabela por quantidade (da menor para a maior).

---

## 📍 Fase 4: Refatoração & Transição Modular (Futuro)

> **Objetivo:** Evoluir a arquitetura mantendo o foco acadêmico e comparativo.

- [ ] Separação das rotinas em módulos Python independentes (`interface.py`, `regra_negocio.py`, `dados.py`).
- [ ] Versão comparativa implementando o paradigma de **Orientação a Objetos (POO)** para fins de estudo.

---

## 💡 Como Contribuir ou Sugerir Melhorias

Caso queira sugerir novas etapas ou relatar um problema:
1. Abra uma **Issue** detalhando a funcionalidade desejada.
2. Siga o padrão do projeto mantendo o foco em clareza pedagógica e legibilidade do código.