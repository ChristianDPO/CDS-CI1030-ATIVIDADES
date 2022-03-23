# Vetor de características e Distribuição do conjunto de dados

- Os resultados dos esperimentos dessa tarefa foram adicionados ao diretório `results/`

## Scripts
`$create_distribuition_graph.py `
- __Descrição__: Cria um grafico de barras que mostra a distribuição de amostras por classe (quantidade de exemplos para cada classe)
- __Execução__: `python3 create_distribuition_graph.py <csv_file> <class_column_name>`
    - `<csv_file>`: Path para o arquivo CSV do dataset para plotar o gráfico
    - `<class_column_name>`: nome da coluna do CSV que contém as labels das classes de cada exemplo
- __Exemplo__:
    - `python3 create_distribuition_graph.py ../../tarefa_3/dataset/FinalDataset/All.csv URL_Type_obf_Type`


## Fontes/Guia de conteúdos

- https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
- https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.scatter.html
- https://matplotlib.org/3.5.1/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py
- https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html





