#!/usr/bin/env python
"""
Script responsável para plotar um grafico de barras com a distribuição dos dados de um dataset

Este script foi feito para funcionar com os arquivos CSV do dataset:
https://www.unb.ca/cic/datasets/url-2016.html#:~:text=Benign%20URLs%3A%20Over%2035%2C300%20benign,duplicate%20and%20 domain%20only%20URLs
"""
import sys
import pandas
import matplotlib.pyplot as plt


MANUALLY_SELECTED_ATT = [
    'domain_token_count',
    'NumberofDotsinURL',
    'Arguments_LongestWordLength',
    'NumberRate_Domain',
    'NumberRate_FileName',
    'NumberRate_AfterPath',
    'Entropy_Domain',
    'URL_Type_obf_Type'
]



def create_distribution_graph(csv_file, class_column_name):
    
    # Reads CSV file with data
    csv_data = pandas.read_csv(csv_file)

    #Create class name array and class count vectors
    class_names = csv_data[class_column_name].unique()
    class_counts = csv_data[class_column_name].value_counts()

    #Plot bar graph to show class sample distribution
    plt.xlabel('Classes')
    plt.ylabel('Number of samples') 
    plt.barh(class_names, class_counts, color='green')

    #Shows the exat class sample count on top of the bar 
    for index, value in enumerate(class_counts):
        plt.text(value, index,str(value))

    plt.show()


def do_main(csv_file):

    create_distribution_graph(
        csv_file=csv_file,
        class_column_name='URL_Type_obf_Type',
    )



if __name__ == '__main__':

    if len(sys.argv) < 2:
        exit("Usage: create_distribution_graph.py <csv_file>")
    
    do_main(
        csv_file=sys.argv[1]
    )