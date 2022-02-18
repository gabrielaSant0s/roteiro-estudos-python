# Roteiro de estudos Python (2022)

Este roteiro de estudos contém um cronograma para usar o [O tutorial de Python](https://docs.python.org/pt-br/3/tutorial/index.html) para aprender e fortalecer os fundamentos da linguagem ao longo de 5 dias. Para cada dia há uma recomendação de capítulos para leitura e exercícios para praticar o conteúdo dos capítulos.

## Como usar este repositório

Os exercícios recomendados estão na pasta `exercicios`, separados por dia. As pastas dos dias tem 2 ou 3 exercícios recomendados para aquele dia. Cada pasta de exercício tem um `README.md` em inglês explicando o que deve ser implementado, um arquivo principal para escrever sua solução e um arquivo com testes, para validar a solução.

Para testar as soluções que você escrever,:

1. Instale o [Poetry](https://python-poetry.org/docs/#installation)
2. Execute `poetry install` para instalar as dependências
3. Execute `poetry shell` para ativar o ambiente virtual (mais detalhes sobre isso no dia 5)
4. Execute `pytest` para rodar os testes

O comando `pytest` vai rodar os testes de todos os exercícios, para testar apenas um deles (o que você estiver implementado, por exemplo) especifique o caminho da pasta com o exercício.

O comando abaixo valida a solução do _Ghost Gobble Arcade Game_, que é um exercício do dia 1:
```
pytest exercicios/dia1/ghost-gobble-arcade-game/
```

## Dia 1

Ler os seguintes capítulos:

- [1. Abrindo seu apetite](https://docs.python.org/pt-br/3/tutorial/appetite.html)
- [2. Utilizando o interpretador Python](https://docs.python.org/pt-br/3/tutorial/interpreter.html)
- [3. Uma introdução informal ao Python](https://docs.python.org/pt-br/3/tutorial/introduction.html)
- [4. Mais ferramentas de controle de fluxo](https://docs.python.org/pt-br/3/tutorial/controlflow.html)

E praticar os seguintes exercícios:

- [Ghost Gobble Arcade Game](exercicios/dia1/ghost-gobble-arcade-game/README.md)
- [Little Sister's Vocabulary ](exercicios/dia1/little-sisters-vocab/README.md)
- [Black Jack](exercicios/dia1/black-jack/README.md)

## Dia 2

Ler os seguintes capítulos:

- [5. Estruturas de dados](https://docs.python.org/pt-br/3/tutorial/datastructures.html)
- [6. Módulos](https://docs.python.org/pt-br/3/tutorial/modules.html)

E praticar os seguintes exercícios:

- [Chaitana's Colossal Coaster](exercicios/dia2/chaitanas-colossal-coaster/README.md)
- [Inventory Management](exercicios/dia2/inventory-management/README.md)
- [Caret Waiter](exercicios/dia2/cater-waiter/README.md)

## Dia 3

Ler os seguintes capítulos:

- [7. Entrada e Saída](https://docs.python.org/pt-br/3/tutorial/inputoutput.html)
- [8. Erros e exceções](https://docs.python.org/pt-br/3/tutorial/errors.html)
- [10. Um breve passeio pela biblioteca padrão](https://docs.python.org/pt-br/3/tutorial/stdlib.html)

E praticar os seguintes exercícios:

- [Hamming](exercicios/dia3/hamming/README.md)
- [Wordy](exercicios/dia3/wordy/README.md)
- [Gigasecond](exercicios/dia3/gigasecond/README.md)

## Dia 4

Ler o seguinte capítulo:

- [9. Classes](https://docs.python.org/pt-br/3/tutorial/classes.html)

E praticar os seguintes exercícios:

- [Phone Number](exercicios/dia4/phone-number/README.md)
- [Bank Account](exercicios/dia4/bank-account/README.md)
- [Queen Attack](exercicios/dia4/queen-attack/README.md)

## Dia 5

Ler os seguintes capítulos:

- [11. Um breve passeio pela biblioteca padrão — parte II](https://docs.python.org/pt-br/3/tutorial/stdlib2.html)
- [15. Aritmética de ponto flutuante: problemas e limitações](https://docs.python.org/pt-br/3/tutorial/floatingpoint.html)
- [12. Ambientes virtuais e pacotes](https://docs.python.org/pt-br/3/tutorial/venv.html)
- [13. E agora?](https://docs.python.org/pt-br/3/tutorial/whatnow.html)

E praticar o seguinte exercício:

[Making the Grade](exercicios/dia5/making-the-grade/README.md)

Se você terminou o exercício acima e não conseguiu concluir o exercício de algum dos dias anteriores, ou acredita que consegue melhorar algum deles, volte para esses exercícios. Se estiver tudo ok, pode fazer também o seguinte exercício:

[Word Search](exercicios/dia5/word-search/README.md)

## Referências

Os exercícios foram extraídos da plataforma [exercism](https://exercism.org/) com poucas modificações.
