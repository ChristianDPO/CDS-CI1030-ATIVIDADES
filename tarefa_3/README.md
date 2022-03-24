# Dataset - URL dataset (ISCX-URL2016)

## Fontes
- Info do dataset: https://www.unb.ca/cic/datasets/url-2016.html
- Paper que utiliza o dataset: [Detecting Malicious URLs Using Lexical Analysis](https://www.researchgate.net/publication/308365207_Detecting_Malicious_URLs_Using_Lexical_Analysis)


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
- Cada campo dos arquivos CSV é descrito, em detalhes, na seção 3.1 do [paper](https://www.researchgate.net/publication/308365207_Detecting_Malicious_URLs_Using_Lexical_Analysis)
