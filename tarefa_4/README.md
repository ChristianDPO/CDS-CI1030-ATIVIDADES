# Vetor de características e Distribuição do conjunto de dados

- Mais informações sobre o dataset encontradas no README.md do diretório `tarefa_3`
- Os resultados dos esperimentos dessa tarefa foram adicionados ao diretório `results/`


## Scripts
`$create_distribuition_graph.py `
- __Descrição__: Cria um grafico de barras que mostra a distribuição de amostras por classe (quantidade de exemplos para cada classe)
- __Execução__: `python3 create_distribuition_graph.py <csv_file> <class_column_name>`
    - `<csv_file>`: Path para o arquivo CSV do dataset para plotar o gráfico
    - `<class_column_name>`: nome da coluna do CSV que contém as labels das classes de cada exemplo
- __Exemplo__:
    - `python3 create_distribuition_graph.py ../../tarefa_3/dataset/FinalDataset/All.csv URL_Type_obf_Type`

`$scattermatrix.py `
- __Descrição__: Gera uma scatter_matrix para o dataset escolhido
- __Execução__: `python3 scattermatrix.py <csv_file>`
    - `<csv_file>`: Path para o arquivo CSV do dataset para plotar a scatter_matrix
- __Exemplo__:
    - `python3 scattermatrix.py ../../tarefa_3/dataset/FinalDataset/All.csv`


## Fontes/Guia de conteúdos

- https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
- https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.scatter.html
- https://matplotlib.org/3.5.1/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py
- https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html





