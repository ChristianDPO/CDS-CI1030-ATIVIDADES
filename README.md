# CI1030-Ciencia-de-Dados

- Este repositório tem como função abrigar as tarefas proposta pela matéria de Ciência de Dados para Segurança (CI1030) da Universiade Federal do Paraná (2021/2o Semestre (ERE5) - feito em 2022)
- Este `README.md` contém apenas os enunciados das tarefas. As tarefas estão divididas em diferentes diretórios, cada diretório contem um `README.md` descrevendo a tarefa

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


# Tarefa Final

Tarefa Final
INSTRUÇÕES:

Do dataset total escolhido, REMOVA 20% das amostras (com balanceamento entre as classes) e as GUARDE em um outro diretório para uso futuro.

As amostras remanescentes (80%) serão referidas daqui por diante como "DATASET".

1. Utilizar o DATASET para treinar modelos baseados em KNN (1, 3 e 5 vizinhos), RandomForest (50 e 100 árvores) e MLP ou SVM (1000 e 5000 épocas, ou erro menor que 0.01)

2. Registre o tempo de TREINAMENTO dos modelos (lembre-se de definir um estado que permita a replicação do experimento e de salvar seu modelo para uso posterior em uma solução a ser demonstrada)

3. Na definição do experimento, lembre-se de colocar a especificação da máquina utilizada (processador, memória, sistema operacional) e dos parâmetros usados em cada algoritmo

4. Treine usando separação do DATASET em 50/50 e 80/20, depois use k-folding com k = 5. Compare os resultados dos testes iniciais com os resultados obtidos pelo artigo original do qual seu dataset é proveniente. Gere as

5. Curvas ROC ou P/R e matrizes de confusão para o relatório

6. Defina uma classe positiva, mesmo em um problema multiclasse

7. Escolha uma meta para o ajuste de limiar, justifique-a conforme a solução que você quer criar e rode o GridSearch de forma a gerar os modelos ótimos para sua meta

8. Busque por amostras do mundo real para demonstração posterior;

9. Ajeite os 20% de amostras removidas de forma que elas não tenham mais rótulo, mas que você possa mapea-las individualmente para o rótulo correto após usá-las como entrada para sua solução

10. Faça uma apresentação da sua solução contendo experimentos, gráficos, tabelas comparativas e uma demonstração prática utilizando os modelos gerados com os 20% de amostras removidas e com as amostras que você encontrou do mundo real.

11. Atualize seu GitHub com os códigos, vetores e documentação nova

CADA ALUNO TERÁ UM SLOT DE 30 MINUTOS NO DIA DA APRESENTAÇÃO (a ser definido).