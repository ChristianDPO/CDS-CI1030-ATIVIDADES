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