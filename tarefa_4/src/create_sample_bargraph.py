#!/usr/bin/env python
"""
Módulo responsável por extrair o vetor de características do dataset escolhido
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



def do_main(csv_file, selected_att, class_column_name):
    
    # Reads CSV file with data
    csv_data = pandas.read_csv(csv_file)

    # Splits CSV file by chosen atributes
    
    csv_selected = csv_data[ selected_att ]
    
    #rename class_column_name to 'class'
    rename_dict = {}
    rename_dict[class_column_name] = 'class'
    csv_selected.rename(rename_dict)
    
    csv_selected = csv_selected.set_axis(selected_att, axis=1)

    #Create class name array and class count vectors

    class_names = csv_selected[class_column_name].unique()
    class_counts = csv_selected[class_column_name].value_counts()

    #Plot bar graph to show class sample distribution

    plt.bar(class_names, class_counts)
    plt.show()


if __name__ == '__main__':

    if len(sys.argv) < 2:
        exit("Usage: extract_features.py <csv_file>")
    
    do_main(
        csv_file=sys.argv[1], 
        selected_att=MANUALLY_SELECTED_ATT,
        class_column_name='URL_Type_obf_Type'
    )