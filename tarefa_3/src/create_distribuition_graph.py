#!/usr/bin/env python
"""
Script responsável para plotar um grafico de barras com a distribuição dos dados de um dataset
"""
import sys
import pandas
import matplotlib.pyplot as plt


def create_distribution_graph(csv_file, class_column_name, dropna = False, color='green'):
    """
    Plots a barh graph with the class distribution of a csv file dataset

    :param str csv_file: path to the csv file
    :param str class_column_name: the name of the csv column with the class labels
    """


    # Reads CSV file with data
    csv_data = pandas.read_csv(csv_file)
    
    if dropna:
        csv_data.dropna(inplace = True)

    #Create class name/label array and class count vectors
    # more info in https://pandas.pydata.org/docs/reference/api/pandas.Series.html
    class_counts = csv_data[class_column_name].value_counts()

    #Plot bar graph to show class sample distribution
    plt.ylabel('Classes')
    plt.xlabel('Number of samples') 
    plt.barh(class_counts.index, class_counts, color=color)

    #Shows the exact class sample count on top of the bar 
    for index, value in enumerate(class_counts):
        plt.text(value, index,str(value))

    plt.show()


def do_main(csv_file, class_column_name):

    create_distribution_graph(
        csv_file=csv_file,
        class_column_name=class_column_name,
    )


if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit("Usage: create_distribution_graph.py <csv_file> <class_column_name>")
    
    do_main(
        csv_file=sys.argv[1],
        class_column_name=sys.argv[2]
    )