# Tarefa Final

Tarefa Final
INSTRUÇÕES:

Do dataset total escolhido, REMOVA 20% das amostras (com balanceamento entre as classes) e as GUARDE em um outro diretório para uso futuro.

As amostras remanescentes (80%) serão referidas daqui por diante como "DATASET".

1. Utilizar o DATASET para treinar modelos baseados em KNN (1, 3 e 5 vizinhos), RandomForest (50 e 100 árvores) e MLP ou SVM (1000 e 5000 épocas, ou erro menor que 0.01);

- Escolha uma meta para o ajuste de limiar, justifique-a conforme a solução que você quer criar e rode o GridSearch de forma a gerar os modelos ótimos para sua meta;
- Defina uma classe positiva, mesmo em um problema multiclasse e binarize seu problema;
- Se seu dataset for muito desbalanceado, faça reamostragem (resample) considerando 1 para 5, isto é, cinco amostras da classe maior para cada amostra da classe menor. Faça 3 (três) conjuntos de dados reamostrados, para melhorar a chance de variedade na classe mais populada. Você também pode tentar criar um classificador de uma classe (ver: one-class classifiers).
2. Com base nos melhores parâmetros gerados para cada algoritmo:

- Treine modelos usando separação do DATASET em 50/50 e 80/20;
- Grave os modelos gerados para uso posterior;
- Registre o tempo de TREINAMENTO dos modelos (lembre-se de definir um estado que permita a replicação do experimento e de salvar seu modelo para uso posterior em uma solução a ser demonstrada);
- Gere as curvas ROC ou P/R e matrizes de confusão para o relatório usando k-folding com k = 5 (produzir um gráfico com 5 curvas por algoritmo);
- Compare os resultados dos testes iniciais com os resultados obtidos pelo artigo original do qual seu dataset é proveniente.
3. Na definição do experimento, lembre-se de colocar a especificação da máquina utilizada (processador, memória, sistema operacional) e dos parâmetros usados em cada algoritmo

4. Testes:

- Se seu problema era inicialmente multiclasses, use um algoritmo de agrupamento no resultado da classe positiva com N clusters (N == quantidade de classes que compõem a classe positiva) e gere a matriz de confusão do agrupamento, a fim de verificarmos se é possível "especializar" a detecção realizada...
- Busque por amostras do mundo real para demonstração posterior;
- Ajeite os 20% de amostras removidas de forma que elas não tenham mais rótulo, mas que você possa mapea-las individualmente para o rótulo correto após usá-las como entrada para sua solução;
5. Faça uma apresentação da sua solução contendo experimentos, gráficos, tabelas comparativas e uma demonstração prática utilizando os modelos gerados com os 20% de amostras removidas e com as amostras que você encontrou do mundo real.

6. Atualize seu GitHub com os códigos, vetores e documentação nova

# Resultados

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