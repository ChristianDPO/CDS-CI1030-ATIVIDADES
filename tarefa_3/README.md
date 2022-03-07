# Dataset 01 - UrlHaus

- `WARING: as urls desse dataset são ativamente malicosas`
- Link: https://urlhaus.abuse.ch/api/#csv

## Descrição
- Este dataset é um arquivo CSV que contém um dump da database de urls do UrlHaus, contendo somente urls maliciosas ativas (que ativamente distribuem malware) ou que foram adicionadas na database nos últimos 90 dias. 
- Como o arquivo é atualizado de 5 em 5 minutos com novas urls, será usado o arquivo de dataset baixado em 06/03/2022, as 15:30 em ponto

## Informações do dataset

- __Amostrars__: 222.686
- O arquivo CSV tem os seguintes campos para cada amostra:
    - __id__: id da url
    - __dateadded__: contém data e horário (utc) que a url foi adicionada
    - __url__: a url em si (contém caracteres especiais)
    - __url_status__: se a url está `"online"` ou `"offline"`
    - __last_online__: ultima data e hora (sem minutos/segundos) que a url estava `"online"`, ou a string `"None"`
    - __threat__: todas as colunas são `"malware_download"`
    - __tags__: diversas tags associadas a url. Os grupos de tags distintos estão em `dataset_1/tags.txt`
    - __urlhaus_link__: link relacionado a url no side do UrlHaus
    - __reporter__: aparentemente a entidade/pessoa que adicionou a url a database


## Informações adicionais
- Comando para contar o número de amostras:
    - `cat dataset_1/csv.txt | cut -d "," -f1 | grep -v \# | wc -l`
- Comando para verificar valores distintos de uma coluna 'X' (considere que as urls tem carcteres especiais), valores pares são os das colunas (colunas impares são virgulas e espaços em branco)
    - `cat dataset_1/csv.txt | cut -d "\"" -f'X' | grep -v \# | sort | uniq -c`



# Dataset 02 - URL Reputation Dataset

- Links: 
    - https://archive.ics.uci.edu/ml/datasets/URL+Reputation
    - http://www.sysnet.ucsd.edu/projects/url/
    - Paper relacionado: https://cseweb.ucsd.edu//~jtma/papers/url-icml2009.pdf

## Descrição
- Este dataset contem dados anonimizados de classificação de urls como maliciosas ou não, basedos em carcaterísticas léxicas e host-based 
- Foram coletados dados de urls durante 120 dias, assim dividindo os dados/features extraidas em 120 arquivos


## Informações do dataset
- __Amostras__: 2396130 (numero de classificações de URL em todos os arquivos)
- Os atributos são anonimizados (ou seja, não é dita a url ou o que o valor da feature corresponde especificamente), mas correspondem a carcaterísticas léxicas e host-based da url, que são descritas em detalhes na seção 2.1 do [paper](https://cseweb.ucsd.edu//~jtma/papers/url-icml2009.pdf)
- As features fora extraidas utilizando técnicas de extração para textos (como a url em si, o dominio, o hostname, entre outros), aumentando o número de features existentes a cada dia com base nas urls adicionadas a classificação. As features (numero da coluna) que tem valores numericos reais são descritas num arquivo `FeatureTypes`
- Ao fazer o download do dataset em formato svm (disponível [neste link](http://www.sysnet.ucsd.edu/projects/url/)) o arquivo descompactado de `url_svmligh.tar.gz` contém os arquivos:
    - ___FeatureTypes__: Uma lista de indices de coluna que representam features de valor real (real-valued)
    - __DayX.svm__ (onde X é um inteiro de 0 a 120) --- os dados para o dia X em formato SVM-light . A label de +1 indica que é uma URL maliciosa e -1 corresponde a uma URL benigna.

