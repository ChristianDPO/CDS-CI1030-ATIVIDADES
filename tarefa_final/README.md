## Tarefa Final

## Informações

- `data/`: Contém listas de urls maliciosas usadas para testar os modelos:
    - `list_1.txt`: Algumas urls extraidas do CSV do repositório da [URLhaus](https://urlhaus.abuse.ch/api/#csv). Foram priorizadas urls com parametros para realizar melhorar a extração.
    - `list_2.txt`: Lista de urls blacklistadas de um dado banco, enviada por email em 28-04-2022 18:00


## Notebooks

- `tarefa_final/src/DatasetSpliting.ipynb`: Faz splitting do dataset em 80% e 20% de maneira balanceada nas classes.
Também gera o dataset com duas classes: 'positiva' (benign) e 'negativa' (malicious)