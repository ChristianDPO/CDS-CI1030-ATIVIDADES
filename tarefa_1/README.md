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

# Resultados

## Scripts

`$captura_rede.py`
- Gera um arquivo `trace.pcap` com a captura do tráfego de rede por 1 min

`conta_sessoes.py`
- Conta o número de sessões gerando o formato de saída, por exemplo:


1456 pacotes no total

1301 pacotes IP

965 pacotes TCP

336 pacotes UDP

12 sessões TCP

3 sessões UDP

155 pacotes não-IP
