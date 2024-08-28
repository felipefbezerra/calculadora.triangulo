# Calculadora de Média de Alunos

Este projeto é uma aplicação simples em Python utilizando a biblioteca Tkinter para criar uma interface gráfica que permite calcular a média de notas de alunos.

## Funcionalidades

- O usuário informa a quantidade de alunos (entre 2 e 7).
- Para cada aluno, o usuário insere o nome e duas notas.
- O programa calcula a média das notas de cada aluno e exibe um relatório com o nome do aluno e sua média.

## Estrutura do Código

- **Função `calcular_media(notas)`**: Recebe uma lista de duas notas e retorna a média delas.
- **Classe `Aplicacao`**: Gerencia a interface gráfica e a lógica da aplicação.
  - **`__init__(self, root)`**: Inicializa a interface, cria os widgets e define variáveis.
  - **Método `iniciar(self)`**: Valida a quantidade de alunos inserida, cria entradas para nome e notas, e prepara a interface para a próxima etapa.
  - **Método `calcular_medias(self)`**: Calcula a média das notas para cada aluno, valida as entradas e exibe um relatório com as médias calculadas.

## Uso

1. Execute o código.
2. Informe a quantidade de alunos (mínimo de 2 e máximo de 7).
3. Preencha o nome e as notas para cada aluno.
4. Clique em "Calcular Médias" para ver o relatório com as médias de cada aluno.

## Dependências

- **Python 3.x**
- **Tkinter**: A biblioteca Tkinter vem pré-instalada com a maioria das distribuições Python. Nenhuma instalação adicional é necessária.

## Exemplo de Execução

1. Ao iniciar o programa, uma janela solicitará a quantidade de alunos.
2. Após inserir a quantidade, campos para o nome e notas dos alunos serão exibidos.
3. Ao finalizar a inserção dos dados, clique no botão "Calcular Médias" e o relatório será gerado com o nome dos alunos e suas respectivas médias.

## Considerações

- As notas devem ser valores numéricos entre 0.0 e 10.0.
- Certifique-se de inserir corretamente os dados, pois o programa exibirá mensagens de erro em caso de entradas inválidas.

## Como Executar

Para executar o programa, basta rodar o arquivo Python em um ambiente que suporte Tkinter.

```bash
python final.py ou final_janela.py
