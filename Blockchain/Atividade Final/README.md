Atividade Final: Construção de uma Blockchain Básica
Objetivos
Com esta atividade, vocês vão:
1. Simular uma rede onde diferentes “nós” trocam informações sobre blocos e transações.
2. Aprender a resolver conflitos (forks) e garantir que todos os nós concordem com a mesma cadeia.
3. Implementar um sistema que controla os saldos dos endereços e garante que só transações válidas sejam processadas.
4. Adicionar taxas de transação e recompensas para mineradores
O que vocês vão implementar
1. Propagação de Blocos e Transações
Imagine que cada nó na rede tem sua própria cópia da blockchain. Quando um novo bloco ou transação é criado, ele precisa ser compartilhado com os outros nós. Essa comunicação é essencial para manter a blockchain sincronizada.
• Tarefa: Criar uma função que simula essa troca de informações entre os nós.
2. Resolução de Conflitos (Forks)
Em uma rede real, às vezes surgem dois blocos “competindo” para serem o próximo na cadeia. Isso gera um fork. Para resolver esse conflito, usamos uma regra simples: a cadeia mais longa vence.
• Tarefa: Quando um nó detecta um fork, ele deve:
1. Comparar as cadeias recebidas.
2. Adotar a cadeia mais longa como válida.
3. Estado Global e Controle de Saldos
Agora é hora de dar mais significado aos endereços que vocês criaram. Cada endereço terá um saldo, e as transações devem obedecer a essa regra básica: ninguém pode gastar mais do que possui.
• Tarefa:
1. Adicionar um sistema para rastrear os saldos de cada endereço.
2. Atualizar os saldos sempre que um bloco for minerado e incluído na cadeia.
4. Taxas de Transação e Recompensas
Para tornar a mineração mais interessante, vamos adicionar taxas às transações. Essas taxas serão somadas à recompensa que o minerador já recebe por cada bloco minerado.
• Tarefa:
1. Adicionar um campo taxa às transações.
2. Modificar a lógica de mineração para somar todas as taxas das transações do bloco à recompensa do minerador.
• Dica: Pense nas taxas como um incentivo extra para os mineradores escolherem transações específicas.