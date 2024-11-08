**Status do Projeto:** Em Desenvolvimento 🚧  
________________________

# Outliers

Aplicação que identifica outliers em um conjunto de números gerado aleatoriamente pelo computador com base em configurações feitas pelo usuário.

**Definição:** Outliers são valores que desviam significativamente dos demais valores em um conjunto de dados. Eles podem ser detectados utilizando fórmulas estatísticas que estabelecem limites superior e inferior. Neste programa, os limites foram definidos pelo método do intervalo interquartil.

## Funcionalidades

- **Configuração de parâmetros:** O usuário escolhe o tamanho do conjunto e define o intervalo de valores em que os números aleatórios serão gerados.
- **Identificação de Outliers:** Aplica o método do intervalo interquartil para determinar os limites superior e inferior e identificar valores que estejam fora desses limites.

## Conceitos de programação

- **Variáveis:** Utilizadas para armazenar as configurações e os resultados.
- **Estruturas de controle:** Implementação de loops e condicionais para lidar com a geração e verificação dos valores.
- **Funções:** Organização do código em funções para garantir modularidade e facilitar a manutenção.

## Tecnologias Utilizadas

- **Python:** Linguagem principal para desenvolver a lógica do algoritmo.
- **Random:** Biblioteca nativa do Python utilizada para definir os números aleatórios, que compõem o vetor de dados.

## Como utilizar

1. O usuário deve escolher o número de elementos que deseja incluir no vetor.
2. O usuário deve escolher um intervalo de números, dos quais o algoritmo gerará os números aleatórios.
3. Com base nas escolhas do usuário, o computador define os números para análise, adicionando alguns outliers propositalmente, conforme as condições pré-definidas.
4. O algoritmo aplica método do intervalo interquartil para definir o limite superior e inferior do conjunto específico.
5. Por fim, o algoritmo cria uma lista com os números que estão dentro dos limites estabelecidos (excluindo os outliers) e exibe a quantidade total de outliers encontrados no conjunto original.


### Possíveis Melhorias Futuras
- Gerar informações adicionais, como média, mediana e moda dos valores.
- Gerar gráficos de dispersão para ajudar na visualização dos outliers.
- Permitir que o usuário adicione seus próprios valores dentro do programa.
- Permitir o uso de diferentes métodos de detecção de outliers.
