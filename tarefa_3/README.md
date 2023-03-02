# Tarefa 03

Exploração do seu dataset

- Os objetivos da tarefa são:

1. Obter o dataset selecionado conforme aprovado pelo professor;

2. Descrevê-lo em seu repositório
- quantidade de amostras;
- classes das amostras - isto é, tipos de rótulos que categorizam as amostras e o que eles significam;
- dicionário de atributos - isto é, quantos, quais são e descrição dos atributos;

3. Apresentar o dataset: estude como fazer um scatterplot e aplique-o para seus dados. O scatterplot é um gráfico que rebate cada atributo pelo outro, gerando uma matriz N por N, onde N é o número de atributos.

4. Investigar o scatterplot para discutir dataset: suas amostras são distinguíveis? Existem características/atributos que parecem não distinguir entre as amostras? Quais? Há características/atributos que parecem ser adequados para distinguir entre as classes/rótulos das amostras? Quais?

Vetor de características e Distribuição do conjunto de dados

- Após a exploração e seleção inicial de quais atributos serão usados como características, faça:

1. Crie um vetor de características com seus dados;

2. Utilize os rótulos das amostras como classes (é um problema binário ou multiclasse?);

3. Inclua os rótulos como última posição do vetor de características, um por amostra, indexando como "classe";

4. Apresente graficamente a distribuição dos seus dados por classe em um gráfico de barras (quantas amostras por classe).

O que fazer?

- Disponibilize o código utilizado para resolver os itens acima no seu repositório. 

- Responda as perguntas na documentação do repositório, em seção específica para Exploração dos Dados.

- Coloque também a figura gerada na documentação do seu repositório. 

__ENTREGAR__: 1 Documento em PDF que atenda aos itens 1 a 4, mostrando as colunas (cabeçalho) do vetor de características, a figura de distribuição das classes e o código como apêndice (formato relatório técnico). 

---
# Dataset - URL dataset (ISCX-URL2016)

- O dataset se encontra no diretório raiz do repositório: `CI1030-Ciencia-de-Dados/dataset/ISCXURL2016.zip`
- Os arquivos em `CI1030-Ciencia-de-Dados/dataset/splitted` são partições do dataset em 80% e 20%, leia mais na `tarefa_final/`

## Descrição

- Contém arquivos texto com urls divididas nas seguintes categorias:
    - Bening URLs: coletadas da lista Alexa top sites, usado um web crawler para extrair as urls dos domínios. Utilizado o VirusTotal para verificar-las como benignas
    
    - Spam URLs: Urls spam coletadas do dataset público WEBSPAM-UK2007.

    - Phishing URLs: obtidas do OpenPhish, um repositório ativo de sites phishing.

    - Malware URLs: urls relacionadas a malware obtidas do projeto DNS-BH, que mantém uma lista de sites com malware.

    - Defacement URLs: Da lista Alexa de sites confiáveis, foram extraidas de suas páginas urls ocultas ou forjadas que contém paginas webs maliciosas

- Contém arquivos CSV com informações léxicas das urls (como numero de tokens/palavras do domínio da url, tamanho da url, etc) 


## Informações
- O dataset contém 5 arquivos para cada categoria de url, que são arquivos csv de uma unica coluna.
- Cada arquivo tem o seguinte número de urls (contado o número de linhas)

    - __Benign_list_big_final.csv__: 35378
    - __DefacementSitesURLFiltered.csv__: 96457
    - __phishing_dataset.csv__: 9965
    - __Malware_dataset.csv__: 11566
    - __spam_dataset.csv__: 12000
    - __Total__: 165366

- O número de dados das urls de cada classe nos arquivos csv não é o mesmo que o total de urls de cada classe, pois foram selecioanadaas uma quantidade menor aleatória de urls para a extração de atributos. Abaixo temos o número de exemplos de cada classe extraidos do arquivo `All.csv`:
    - __Benignas__: 7781
    - __Defacement__: 7930
    - __Phishing__: 7586
    - __Malware__: 6712
    - __Spam__: 6698
    - __Total__: 36707

- Os arquivos `Spam.csv`, `Malware.csv`, `Phishing.csv` e `Daefacement.csv` contém uma separação
dos exemplos do arquivo `All.csv` de somente os exemplos benignos juntamente com os exemplos da classe do nome do arquivo. Essa separação foi feita, julgando pelo paper, para ver o resultado de uma classificação de duas classes (acurácia da verificação entre benigno e spam, por exemplo)
- O arquivo `All.csv` aparentemente foi usado para a classificação multi-classe das urls
- O arquivo `All_Infogain.csv` contém o dataset de `All.csv`, com os 12 primeiros atributos selecionados no algortimo do Infogain + Ranker do Weka, também removendo todos os samples com valores NaN nas colunas. A coluna 13 é a classe do sample
    - Cada campo dos arquivos CSV é descrito, em detalhes, na seção 3.1 do [paper](https://www.researchgate.net/publication/308365207_Detecting_Malicious_URLs_Using_Lexical_Analysis)


## Seleção de atributos

- Foram feitas tentativas de scatterplot de NxN gráficos (scatter_matrix) para verificar a presença de agrupamentos/clustering das classes. Não foi notável nenhum agrupmento dos atributos. 
- Os atributos escolhidos para o vetor de características escolhidos são baseados no [paper](https://www.researchgate.net/publication/308365207_Detecting_Malicious_URLs_Using_Lexical_Analysis)
do dataset, sendo escolhidos através do algoritimo de Ganho de Informação (Infogain) e Ranker do Weka nos atributos
- Selecionados 12 atributos de 79. Os atributos são real-valued, então foram usados os próprios atributos para compor o vetor de caracteŕisticas, também com a label da classe.
- Foi replicado o experimento no paper, o dataset foi carregado no Weka, foram selecionados os atributos mais significativos usando os algortimos InfoGain + Ranker e, após isso, foi realizado um DropNaN
- Ao comparar o resultado da réplica do experimento com o arquivo já existente do dataset `All_Infogain.csv`, não houve diferenças (ou seja, `All_Infogain.csv` é o arquivo `All.csv` com a seleção de atributos + DropNaN)


## Resultados

- `tarefa_3/results/Infogain_Features_Scatterplot.png`: tentativa de scatterplot com NxN com os atributos escolhidos no Infogain
- `tarefa_3/results/feature_array_example.txt`: exemplifica como será representado o vetor de características
- `tarefa_3/results/Dataset_Distribution_Graph.png`: gráfico que mostra a distribuição dos dados no dataset
- `tarefa_3/results/Dataset_Distribution_Graph_Infogain_Dropna.png`: gráfico que mostra a distribuição dos dados usando os atributos selecionados sem valores 'NaN' nas colunas (Infogain)
- `tarefa_3/results/relatorio-ciencia-de-dados-cdpo18.pdf`: Relatório completo da atividade sobre os resultados

## Scripts

`$create_distribuition_graph.py `
- __Descrição__: Cria um grafico de barras que mostra a distribuição de amostras por classe (quantidade de exemplos para cada classe)
- __Execução__: `python3 create_distribuition_graph.py <csv_file> <class_column_name>`
    - `<csv_file>`: Path para o arquivo CSV do dataset para plotar o gráfico
    - `<class_column_name>`: nome da coluna do CSV que contém as labels das classes de cada exemplo
- __Exemplo__:
    - `python3 create_distribuition_graph.py ../../dataset/FinalDataset/All.csv URL_Type_obf_Type`

`$scattermatrix.py `
- __Descrição__: Gera uma scatter_matrix para o dataset escolhido
- __Execução__: `python3 scattermatrix.py <csv_file>`
    - `<csv_file>`: Path para o arquivo CSV do dataset para plotar a scatter_matrix
- __Exemplo__:
    - `python3 scattermatrix.py ../../dataset/FinalDataset/All.csv`


## Fontes
- Info do dataset: https://www.unb.ca/cic/datasets/url-2016.html
- Paper que utiliza o dataset: [Detecting Malicious URLs Using Lexical Analysis](https://www.researchgate.net/publication/308365207_Detecting_Malicious_URLs_Using_Lexical_Analysis)


## Guia de conteúdos

- https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
- https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.scatter.html
- https://matplotlib.org/3.5.1/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py
- https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html
