# CI1030-Ciencia-de-Dados

- Este repositório tem como função abrigar as tarefas proposta pela matéria de Ciência de Dados para Segurança (CI1030) da Universiade Federal do Paraná (Período 2022/1)
- As tarefas estão divididas em diferentes diretórios, cada diretório contem um `README.md` descrevendo a tarefa
- Este `README.md` contém apenas os enunciados das tarefas


# Tarefa 01

- Faça uma captura de rede em sua máquina usando o ScaPy (aproximadamente 1 minuto, navegando na Web) e salve o arquivo como "trace.pcap"
- Crie um script que leia o arquivo capturado e:
- Conte quantos pacotes foram capturados no Total;
- Conte quantos pacotes possuem protocolo de camada de Rede "IP"
- Conte quantos pacotes possuem protocolo de camada de Transporte "TCP"
- Conte quantos pacotes possuem protocolo de camada de Transporte "UDP"
- Separe as sessões "TCP" e "UDP" em dicionários de listas (chave == sessão, valor recebe lista de payloads daquela sessão em formato legível)
- Imprima a quantidade de sessões TCP e UDP, bem como a quantidade de pacotes não-associados ao protocolo de rede IP.

__EXEMPLO DE SAÍDA:__

O arquivo "trace.pcap" possui:

1456 pacotes no total

1301 pacotes IP

965 pacotes TCP

336 pacotes UDP

12 sessões TCP

3 sessões UDP

155 pacotes não-IP


# Tarefa 02
- Criar um repositório no Github/Gitlab para a disciplina.
- Organizá-lo de acordo com as tarefas (em código e documentos).
- Iniciar a escrita do "manual" (README).
- Subir o código da Tarefa 1 no seu repositório.

# Tarefa 03

Exploração do seu dataset

Os objetivos da tarefa são:

1. Obter o dataset selecionado conforme aprovado pelo professor;

2. Descrevê-lo em seu repositório
- quantidade de amostras;
- classes das amostras - isto é, tipos de rótulos que categorizam as amostras e o que eles significam;
- dicionário de atributos - isto é, quantos, quais são e descrição dos atributos;

3. Apresentar o dataset: estude como fazer um scatterplot e aplique-o para seus dados. O scatterplot é um gráfico que rebate cada atributo pelo outro, gerando uma matriz N por N, onde N é o número de atributos.

4. Investigar o scatterplot para discutir dataset: suas amostras são distinguíveis? Existem características/atributos que parecem não distinguir entre as amostras? Quais? Há características/atributos que parecem ser adequados para distinguir entre as classes/rótulos das amostras? Quais?

# Tarefa 04

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