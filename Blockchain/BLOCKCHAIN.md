# Blockchain

## O que é uma blockchain
Estrutura para armazenamento de dados que consiste em vários blocos conectados entre si. Um esquema criptográfico garante a inviolabilidade da cadeia.

## O que são e o que fazem as funções hash na blockchain?
As funções hash transformam um texto de entrada, de qualquer tamanho, em um texto de saída aparentemente aleatório, com tamanho fixo.

### Características fundamentais das funções hash criptográficas:
- Fácil de computar;
- Unidirecional;
- Livre de colisão;
- Puzzle friendly.

## Como as funções hash garantem a integridade da blockchain?
Cada bloco da blockchain é identificado pelo hash de seu conteúdo e também armazena o hash do bloco anterior. Se um bloco for alterado, seu hash será alterado também, quebrando a cadeia de blocos.

## Para que servem as assinaturas digitais?
Servem para autenticar documentos virtualmente.

### Propriedades requeridas em uma assinatura digital:
- Impossível de falsificar;
- Fácil de verificar;
- Atrelada ao documento.

## Qual a função da chave secreta?
Permite a geração de assinaturas digitais, em conjunto com o documento a ser assinado.

## Qual a função da chave pública?
Serve para autenticar assinaturas digitais.

> Se alguém descobrir seu par de chaves pública/secreta, esta pessoa poderá assinar qualquer documento como se fosse você. Sendo um conjunto de funções criptográficas, o sistema de assinaturas digitais é incapaz de fazer distinção entre pessoas, apenas verificar a compatibilidade das chaves utilizadas. Proteger sua chave secreta é fundamental para a segurança no Bitcoin.

## Como a blockchain garante consenso na rede Bitcoin?
As transações de Bitcoin só se tornam efetivas quando são inseridas na blockchain, e a mineração garante que todos os nós mantenham a mesma blockchain armazenada.

# Bitcoin

## Em qual contexto histórico surgiu o Bitcoin?
Surgiu com a crise econômica de 2008, marcada por planos bilionários de resgate a bancos, muitas vezes sem contrapartida para a população afetada.

## As principais funções que o Bitcoin agrega são:
- Reserva de valor;
- Moeda de troca;
- Meio de pagamento.

**Não é possível realizar vendas a prazo com Bitcoin.**

### Características fundamentais do Bitcoin:
- Descentralizado;
- Segurança por criptografia;
- Registro em blockchain;
- Engenharia de incentivo.

## Diferenças entre o sistema bancário tradicional e o Bitcoin:
- **Bitcoin**: é baseado em consenso, descentralizado, algoritmos e controle individual do dinheiro.
- **Sistema Bancário Tradicional**: operações centralizadas, arbitrárias e baseadas em um controle institucional do dinheiro dos clientes.

## O que acontece se o consenso não for atingido para o Bitcoin?
Quando a comunidade não consegue alcançar um consenso, ocorrem os chamados "hard forks" (bifurcações). Nesses casos, cada participante passa a operar de acordo com a versão que apoia, resultando na criação de duas versões distintas do Bitcoin, como o **Bitcoin Cash** e **Bitcoin Gold**. Essas criptomoedas compartilham o histórico anterior ao "fork", e os detentores de Bitcoin antes da bifurcação possuem saldos equivalentes nas novas moedas. Após o "fork", cada moeda segue seu próprio caminho, independentemente do Bitcoin original.

Até meados de 2019, o Bitcoin passou por três "hard forks".

### Características da rede Bitcoin:
- Distribuída;
- Sem hierarquia;
- Segue um protocolo de consenso.

## O que é um nó da rede Bitcoin?
É qualquer computador conectado à rede Bitcoin.

## O que diferencia um full node de um lite node?
O full node armazena toda a blockchain e é capaz de operar independentemente.

## O que acontece se um nó da rede começa a transmitir informações falsas?
Nada acontece, pois a rede Bitcoin é altamente resistente a agentes maliciosos. Todas as informações são verificadas antes de serem incorporadas à blockchain, tornando-as imutáveis. Para inserir informações falsas, um hacker precisaria controlar, no mínimo, 51% de todo o poder computacional da rede, algo extremamente improvável no caso do Bitcoin.

Por outro lado, em criptomoedas com menor número de mineradores, esse risco é mais significativo. Outra possibilidade de ataque envolve o roubo da chave privada de um usuário, permitindo ao invasor controlar seus Bitcoins. Nesse caso, a vulnerabilidade não estaria na rede Bitcoin em si, já que as informações transmitidas seriam tecnicamente corretas.

# CentralCoin

O CentralCoin é praticamente idêntico ao Bitcoin, exceto pelo fato de que na CentralCoin existe uma autoridade central que verifica as transações e mantém a blockchain, enquanto o Bitcoin faz isso em uma rede descentralizada.

## Quais informações ficam armazenadas na blockchain da CentralCoin?
Transações de criação e de transferência de moedas CentralCoin.

## Como funciona a transação de transferência de moedas?
O usuário deve indicar quais moedas estará utilizando (destruindo), quem são os destinatários das novas moedas criadas e adicionar sua assinatura digital.

O banco central verifica em cada transferência:
- A autenticidade da assinatura digital;
- Se a soma das moedas consumidas é maior que as moedas criadas;
- Se o usuário tem a posse das moedas utilizadas.

## Como o banco sabe o meu saldo na CentralCoin?
Na CentralCoin (e no Bitcoin), o conceito de "saldo" é distinto dos sistemas tradicionais. O banco central não mantém um registro centralizado. O saldo de um indivíduo corresponde à soma do valor de todas as moedas associadas à sua chave pública, que ainda não foram gastas. O banco da CentralCoin verifica essas informações na blockchain para determinar o saldo vinculado a uma chave pública específica.

# Mineração de Dados

## Para que serve a mineração?
A mineração impede o gasto duplo no sistema bitcoin.

## O que é gasto duplo?
É, literalmente, gastar a mesma moeda bitcoin duas vezes.

## O que acontece se há uma bifurcação na blockchain?
Enquanto os dois ramos tiverem o mesmo tamanho, os mineradores vão trabalhar em ambos até que um minerador consiga estender um desses ramos, que passará a ser o mais longo, e portanto todos os mineradores passam a trabalhar nesse ramo. O outro bloco bifurcaddo é esquecido.

## Como um hacker pode explorar uma bifurcação na cadeia para enriquecer?
- **Aproveitamento de Tokens:** Detentores da criptomoeda original recebem tokens equivalentes na nova moeda, permitindo lucros ao vender os novos tokens rapidamente.

- **Ataques de 51%:** Um hacker que controla 51% do poder de hash pode minerar blocos, reverter transações (double spending) e estabelecer regras que favoreçam seus interesses financeiros.

- **Manipulação de Mercado:** O hacker pode manipular o preço da nova criptomoeda através de práticas de "pump and dump", comprando grandes quantidades para elevar o preço e vendendo para lucrar.

- **Exploits e Vulnerabilidades:** A exploração de vulnerabilidades na nova criptomoeda ou contratos inteligentes pode permitir que hackers roubem tokens ou manipulem operações.

- **Falsificação de Transações:** Durante a bifurcação, um hacker pode realizar transações fraudulentas que não sejam detectadas imediatamente, aproveitando-se de falhas na rede.

- **Aproveitamento da Confusão dos Usuários:** Hackers podem explorar a falta de conhecimento dos usuários sobre o processo de bifurcação, obtendo acesso a fundos expostos ou não reivindicados.

## O que acontece se o hacker conseguir 51% do hash power?
Ele será capaz de gastar a mesma moeda quantas vezes quiser. Ou seja, ele terá Bitcoins infinitos. Na prática, as pessoas vão perceber rapidamente que isso ocorreu e o valor do Bitcoin irá despencar. Dessa forma, é provável que os gastos para fazer esse tipo de ataque não sejam compensados pelos possíveis ganhos.

## O que é um nonce e qual a função dele?
É um valor numérico sem significado que é adicionado a cada bloco da blockchain. Os mineradores alteram o valor do nonce tentando cumprir com o requisito do proof of work.

## O que dá ao minerador o direito de adicionar o próximo bloco da cadeia?
Conseguir criar um bloco cujo hash tenha um determinado número de zeros.

## De onde surgiram os Bitcoins em circulação?
Todos os bitcoins em circulação surgiram da mineração. A cada quatro anos, o número de bitcoins criados a cada novo bloco é reduzido pela metade.

## O que são mining pools?
São esquemas cooperativos entre minerados, em que todos trabalham tentando montar blocos, e os bitcoins auferidos são distribuídos entre todos os participantes de acordo com o trabalho computacional de cada um.

## Qual é a consequência da redução de mineradores para a velocidade de criação de novos blocos?
Nenhuma. Um novo bloco é criado, em média, a cada dez minutos. Se o número de mineradores é menor, fica mais fácil obter uma solução para o proof of work. Assim, a taxa de criação de blocos é mantida aproximadamente constante.

# Ethereum

## O que é o Ethereum?
Ethereum é uma plataforma descentralizada que permite a criação e execução de contratos inteligentes (smart contracts) e aplicativos descentralizados (DApps), utilizando a blockchain para garantir a segurança e a imutabilidade das transações. Pode ser descrito como uma blockchain programável e qualquer algoritmo pode ser executado na rede Ethereum (Turing Completo).

## Quais são as características básicas do Ethereum?
- **Descentralização**: Não possui uma autoridade central controlando a rede.
- **Contratos Inteligentes**: Permite a automação de processos através de códigos que são executados quando determinadas condições são atendidas.
- **Token Ether (ETH)**: A moeda nativa utilizada para pagar taxas de transação e serviços na rede.

## O que é a Fundação Ethereum?
A Fundação Ethereum é uma organização sem fins lucrativos que apoia o desenvolvimento e a pesquisa da plataforma Ethereum, promovendo a tecnologia de blockchain e contratos inteligentes.

## Quais são os objetivos da Fundação Ethereum?
- **Desenvolvimento da Plataforma**: Facilitar o avanço da infraestrutura do Ethereum e de suas ferramentas.
- **Educação**: Promover a conscientização e a compreensão sobre a tecnologia blockchain e o Ethereum.
- **Financiamento**: Apoiar projetos e iniciativas que contribuam para a evolução do ecossistema Ethereum.

## Como a Fundação Ethereum opera?
A Fundação Ethereum financia e apoia desenvolvedores, pesquisadores e iniciativas que trabalham em melhorias da plataforma, além de colaborar com outros projetos e comunidades dentro do espaço de criptomoedas.

> A Fundação Ethereum desempenha um papel crucial na governança e no desenvolvimento sustentável do ecossistema Ethereum, garantindo que a plataforma continue a evoluir e atender às necessidades da comunidade.

## O que são Accounts e States no Ethereum?
- **Accounts**: Existem dois tipos de contas no Ethereum: contas de usuário (externas) e contas de contrato. As contas de usuário são controladas por chaves privadas, enquanto as contas de contrato são controladas pelo código do contrato inteligente.
- **States**: O estado da Ethereum refere-se à informação que é armazenada em toda a rede, incluindo o saldo das contas, o código e o armazenamento dos contratos inteligentes.

## O que é a Ethereum Virtual Machine (EVM)?
A Ethereum Virtual Machine é o ambiente de execução que permite a execução de contratos inteligentes na rede Ethereum. É uma máquina virtual descentralizada que executa código e garante que todos os nós da rede executem o mesmo programa de forma consistente.

## O que é o GAS?
GAS é a unidade de medida que representa a quantidade de trabalho computacional necessário para executar operações na rede Ethereum. Os usuários pagam taxas em ETH para cobrir o custo do GAS ao enviar transações ou executar contratos inteligentes.

## O que são Smart Contracts?
Smart contracts são contratos autoexecutáveis cujas condições são escritas em código. Eles permitem transações automáticas e seguras, sem a necessidade de intermediários. Os contratos inteligentes são imutáveis uma vez implantados na blockchain, garantindo sua execução conforme programado.

## O que são DApps (Aplicativos Descentralizados)?
DApps são aplicativos que funcionam em uma rede blockchain descentralizada, utilizando contratos inteligentes para operar. Eles oferecem maior segurança, transparência e resistência à censura, pois não são controlados por uma única entidade.

> O Ethereum revolucionou a forma como interagimos com a tecnologia blockchain, possibilitando a criação de uma variedade de aplicações que vão além das criptomoedas, incluindo finanças descentralizadas (DeFi), jogos, e muito mais.
