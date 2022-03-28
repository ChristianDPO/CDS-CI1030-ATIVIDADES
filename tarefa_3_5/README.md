# Vetor de características e Distribuição do conjunto de dados

- Mais informações sobre o dataset encontradas no README.md do diretório `tarefa_3`

## Atributos
- Os atributos escolhidos para o vetor de características escolhidos são baseados no [paper](https://www.researchgate.net/publication/308365207_Detecting_Malicious_URLs_Using_Lexical_Analysis)
do dataset, sendo escolhidos através do algoritimo de Ganho de Informação (Infogain) e Ranker do Weka nos atributos
- Foram feitas tentativas de scatterplot de NxN gráficos (scatter_matrix) para verificar a presença de agrupamentos/clustering das classes. 
- Não foi notável nenhum agrupmento dos atributos (pelo menos no plano de duas dimensões), mesmo os escolhidos pelo paper (figura da scattermatrix com esses atributos em `results/`)
- O arquivo `results/feature_array_example.txt` exemplifica como será representado o vetor de características usando os atributos real-valued
O gráfico `results/Dataset_Distribution_Graph.png` mostra a a distribuição dos dados no dataset
- O gráfico `results/Dataset_Distribution_Graph_Infogain_Dropna.png` mostra a a distribuição dos dados usando os atributos selecionados sem valores 'NaN'
nas colunas 
- Mais informações sobre os atributos escolhidos em `tarefa_4/results/relatorio-ciencia-de-dados-cdpo18.pdf`

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





