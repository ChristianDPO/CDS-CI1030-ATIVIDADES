# Dataset - URL dataset (ISCX-URL2016)

## Fontes
- Info do dataset: https://www.unb.ca/cic/datasets/url-2016.html#:~:text=Benign%20URLs%3A%20Over%2035%2C300%20benign,duplicate%20and%20domain%20only%20URLs.
- Paper que utiliza o dataset: ["Detecting Malicious URLs Using Lexical Analysis"](https://www.researchgate.net/publication/308365207_Detecting_Malicious_URLs_Using_Lexical_Analysis)


## Descrição

- Contém arquivos texto com urls divididas nas seguintes categorias:
    - Bening URLs: coletadas da lista Alexa top sites, usado um web crawler para extrair as urls dos domínios. Utilizado o VirusTotal para verificar-las como benignas
    
    - Spam URLs: Urls spam coletadas do dataset público WEBSPAM-UK2007.

    - Phishing URLs: obtidas do OpenPhish, um repositório ativo de sites phishing.

    - Malware URLs: urls relacionadas a malware obtidas do projeto DNS-BH, que mantém uma lista de sites com malware.

    - Defacement URLs: Da lista Alexa de sites confiáveis, foram extraidas de suas páginas urls ocultas ou forjadas que contém paginas webs maliciosas

- Contém arquivos CSV com informações léxicas (como numero de tokens/palavras do domínio da url, tamanho da url, etc) das urls


## Informa