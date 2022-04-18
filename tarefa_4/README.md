## Tarefa 04 - Apresentação

- O resultado do gráfico do kmeans se encontra em `tarefa_4/results/kmeans_graph.png`
- A apresentação de slides com o resultados do dataset se encontra em `tarefa_4/results/CI1030-cdpo18.pdf`


## Scripts

`$kmeans_cluster_graph.py `
- __Descrição__: Cria um grafico de clusters usando kmeans, plotando em duas dimensões utilizando Principal component analysis (PCA)
- __Execução__: `python3 kmeans_cluster_graph.py <csv_file> <class_column_name>`
    - `<csv_file>`: Path para o arquivo CSV do dataset para plotar o gráfico
    - `<class_column_name>`: nome da coluna do CSV que contém as labels das classes de cada exemplo
- __Exemplo__:
    - `python3 kmeans_cluster_graph.py ../../dataset/FinalDataset/All_Infogain.csv class`

## Notebooks

- `tarefa_4/src/Clustering.ipynb`: Faz o clustering com Kmeans para verificar a separação das classes
- `tarefa_4/src/Classification.ipynb`: faz a classificação usando o vetor de características escolhido