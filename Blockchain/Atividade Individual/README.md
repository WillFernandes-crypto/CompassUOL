> # Atividade Individual
> Desenvolver uma "rede blockchain" com funcionalidades básicas.
> 
> O sistema deve permitir:
> 
> - A criação de transações;
> - A inclusão delas em blocos;
> - A inserção desses blocos na rede;
> - A validação da autenticidade.
> 
> O resultado dessas operações deve ser exportado por meio de logs no console.
> 
> Além disso, o projeto deve garantir a integridade e validação da rede como um todo. A avaliação será estritamente técnica. 
> 
> Não se esqueçam de incluir uma documentação detalhada que explique como executar o projeto.
>
> Observações:
> - Criar uma lista encadeada de hashes;

# Ferramentas Utilizadas

## Pré-requisitos
Python

## Configuração Inicial


## Executando a aplicação


## Funcionalidades


---
---
---
# Recaptulando Blockchains

## O que é um hash?
Funciona como uma "impressão digital" de um determinado dado, de uma quantidade de caracteres ou bytes.

_A partir do hash não é possível gerar o código original._

## O que é um bloco
É uma quantidade de dados agrupado, com tamanho limitado de 1MB no protocolo de bitcoins.

| Bloco |

| Número do bloco (altura do bloco no protocolo bitcoin) |

| Nounce |

| Dados |

_Um bloco é considerado minerado toda vez que o minerador encontrar um nounce que faz com que o hash comece com uma certa quantidade de zeros_

## O que é um blockckain
São vários blocos encadeados.

_Na blockchain, o bloco atual possui um novo campo prev, que aponta para o hash do bloco anterior._
