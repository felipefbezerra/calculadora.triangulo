# Calculadora de Área de Triângulo

Este projeto é uma aplicação em Python que utiliza a biblioteca Tkinter para criar uma interface gráfica simples, onde o usuário pode calcular a área de um triângulo a partir da base e altura fornecidas.

## Funcionalidades

- Entrada de valores para a base e altura de um triângulo.
- Cálculo automático da área do triângulo com base nos valores fornecidos.
- Exibição do resultado diretamente na interface gráfica.

## Estrutura do Código

- **Função `calcular_area(base, altura)`**: Recebe os valores da base e altura do triângulo e retorna a área calculada.
- **Função `calcular_e_mostrar()`**: Coleta os valores inseridos pelo usuário, chama a função de cálculo da área, e exibe o resultado na interface.

## Interface Gráfica

A interface gráfica é composta por:

- **Labels**: Para identificar os campos de entrada de base e altura do triângulo.
- **Entries**: Campos de entrada para o usuário inserir os valores da base e altura.
- **Button**: Botão para calcular a área do triângulo.
- **Label de Resultado**: Campo onde o resultado da área calculada é exibido.

## Uso

1. Execute o código.
2. Insira o valor da base do triângulo no primeiro campo.
3. Insira o valor da altura do triângulo no segundo campo.
4. Clique no botão "Calcular" para obter a área do triângulo.
5. O resultado será exibido logo abaixo do botão de cálculo.

## Dependências

- **Python 3.x**
- **Tkinter**: A biblioteca Tkinter é necessária para a interface gráfica. Ela já vem pré-instalada com a maioria das distribuições Python.

## Exemplo de Execução

1. Ao iniciar o programa, uma janela será exibida com campos para inserir a base e a altura do triângulo.
2. Após inserir os valores, clique no botão "Calcular".
3. A área do triângulo será calculada e exibida na tela.

## Considerações

- Os valores da base e altura devem ser números reais (decimais são permitidos).
- Certifique-se de que os valores inseridos sejam válidos para evitar erros no cálculo.

## Como Executar

Para executar o programa, basta rodar o arquivo Python em um ambiente que suporte Tkinter.

```bash
python parcial.py ou parcial_janela.py
