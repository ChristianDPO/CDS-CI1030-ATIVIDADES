#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Christian Debovi Paim Oliveira
#GRR20186713
"""
Script para caputrar tráfego de rede em um arquivo '.pcap'
"""

from scapy.all import sniff, PcapWriter

#in seconds
CAPUTRE_TIME = 60

def captura_rede(capture_time=CAPUTRE_TIME):    

    pcapwriter = PcapWriter("trace.pcap", append=True, sync=True)
    sniff_result = sniff(timeout=capture_time)
    
    for pkt in sniff_result:
        print(pkt.summary())
        pcapwriter.write(pkt)



if __name__ == '__main__':
    captura_rede()