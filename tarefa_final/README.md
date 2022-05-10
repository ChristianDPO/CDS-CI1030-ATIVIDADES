## Tarefa Final

## Seleção de atributos
- Das features geradas da tarefa anterior, foram removidas: `['Entropy_Domain', 'avgpathtokenlenght', CharacterContinuityRate]` por não terem uma especificação clara de como foram calculadas

## Diretórios

- `results`: Contém os resultados dos experimenots (imagens, apresentação)

- `data/`: Contém listas de urls maliciosas usadas para testar os modelos:
    - `list_1.csv`: Algumas urls maliciosas extraidas do CSV do repositório da [URLhaus](https://urlhaus.abuse.ch/api/#csv). Foram priorizadas urls com parametros para realizar melhorar a extração.
        - Samples: 64
    - `list_2.csv`: Lista de urls blacklistadas de um dado banco, enviada por email em 28-04-2022 18:00
        - Samples: 56
    - `list_3.csv`: Lista de urls benignas. Samples retirados do csv [deste dataset](https://data.mendeley.com/datasets/gdx3pkwp47/2)
        - Samples: 50


## Notebooks

- `tarefa_final/src/DatasetDescribe.ipynb`: Faz a descrição dos valores do dataset e do dataset após uma seleção de atributos.
- `tarefa_final/src/DatasetSpliting.ipynb`: Faz splitting do dataset em 80% e 20% de maneira balanceada nas classes.
Também gera o dataset com duas classes: 'positiva' (benign) e 'negativa' (malicious)
- `tarefa_final/src/DatasetTraining.ipynb`: Treina modelos usando 80% do dataset, plota gráficos com matrizes de confusão, ROC curves e mostra métricas, além de salvar os modelos treinados em um dado diretório.
- `tarefa_final/src/DatasetTesting.ipynb`: Utiliza os modelos treinados para classificar as 20% das amostras e amostras da vida real (listas de urls em `data/`)