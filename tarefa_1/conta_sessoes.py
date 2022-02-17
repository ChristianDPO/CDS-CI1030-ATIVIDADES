#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Christian Debovi Paim Oliveira
#GRR20186713
"""
Script para contar seções com base em um arquivo de caputra de rede (.pcap)
"""
from scapy.all import rdpcap

OUTPUT_STR_FORMAT = """
O arquivo "trace.pcap" possui:

{total_pkt_count} pacotes no total

{ip_count} pacotes IP

{tcp_count} pacotes TCP

{udp_count} pacotes UDP

{tcp_sessions} sessões TCP

{udp_sessions} sessões UDP

{no_ip_count} pacotes não-IP
"""

def conta_sessoes():
    
    pcap_file = rdpcap('trace.pcap')
    print(pcap_file)

    total_pkt_count = 0
    ip_count = 0
    tcp_count = 0
    udp_count = 0
    tcp_sessions = 0
    udp_sessions = 0
    no_ip_count = 0

    tcp_sessions_dict = {}
    udp_sessions_dict = {}

    for pkt in pcap_file:
        total_pkt_count+=1
        
        if pkt.getlayer('IP'):
            ip_count+=1
        else:
            no_ip_count+=1

        tcp_result = pkt.getlayer('TCP')
        if tcp_result:
            tcp_count+=1

            #o summary ja contém o ip de origem, destino e os ports usados
            current_tcp_session = str(tcp_result.summary())

            if not current_tcp_session in tcp_sessions_dict:
                tcp_sessions+=1
                tcp_sessions_dict[current_tcp_session] = []
            tcp_sessions_dict[current_tcp_session].append(str(tcp_result.payload))

        udp_result = pkt.getlayer('UDP')
        if udp_result:
            udp_count+=1
            
            #o summary ja contém o o endereço de origem e destino
            current_udp_session = str(udp_result.summary())

            if not current_udp_session in udp_sessions_dict:
                udp_sessions+=1
                udp_sessions_dict[current_udp_session] = []
            udp_sessions_dict[current_udp_session].append(str(udp_result.payload))

    print(
        OUTPUT_STR_FORMAT.format(
            total_pkt_count=total_pkt_count,
            ip_count=ip_count,
            tcp_count=tcp_count,
            udp_count=udp_count,
            tcp_sessions=tcp_sessions,
            udp_sessions=udp_sessions,
            no_ip_count=no_ip_count
        )
    )


if __name__ == '__main__':
    conta_sessoes()

