# Tarefa 04

Cada aluno deverá apresentar o estado atual do seu projeto, mostrando e discutindo:

- O dataset como um todo
    - atributos, características, classes, amostras
    - distribuição de classes
- Processamento dos dados
    - Como foi feita a extração de características
    - Foi feito seleção?
- Exploração e visualização de dados
    - Mostrar o diagrama de dispersão (scatterplot)
    - Mostrar visualmente o agrupamento de seu dataset com algum algoritmo de clustering
        - Sugestão: K-Means (mas pode usar outro, como DBScan)
        - Usar como número de cluster o número de classes do seu problema (se for binário, K=2)

__ENTREGAR__: Apresentar slides, 10 minutos cada aluno/apresentação (vale nota parcial).

Outras tarefas para a verificação:
    
- Verificar o gráfico do Kmeans e o gráfico das amostras. Qual a proporção de amostras em cada cluster? Os clusters separam bem as amostras?
- Fazer a classificação do dataset com a proporção 80/20 de treino/teste com alguns classificadores de sua escolha. Houveram bons resultados? Qual dos escolhidos tiveram bons resultados e por quê?

# Resultados

- `tarefa_4/results/kmeans_graph.png`: Gráfico do kmeans do script `kmeans_cluster_graph.py`
- `tarefa_4/results/CI1030-cdpo18.pdf`: Apresentação em PDF sobre um overview e seleção de atributos do dataset


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