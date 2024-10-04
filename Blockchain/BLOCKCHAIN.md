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
