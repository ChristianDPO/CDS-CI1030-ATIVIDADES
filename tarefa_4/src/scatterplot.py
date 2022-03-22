#!/usr/bin/env python
from pandas.plotting import scatter_matrix

import sys
import pandas
import matplotlib.pyplot as plt
from sklearn import preprocessing

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
    dataset = pandas.read_csv(csv_file, index_col=0)

    # Splits CSV file by chosen atributes
    ds_sel = dataset[ selected_att ]

    # Chooses N examples for each class for plotting
    df1 = ds_sel.loc[ds_sel[class_column_name] == 'benign'].sample(n=50)
    df2 = ds_sel.loc[ds_sel[class_column_name] == 'spam'].sample(n=50)
    df3 = ds_sel.loc[ds_sel[class_column_name] == 'phishing'].sample(n=50)
    df5 = ds_sel.loc[ds_sel[class_column_name] == 'malware'].sample(n=50)
    df4 = ds_sel.loc[ds_sel[class_column_name] == 'Defacement'].sample(n=50)
    df = pandas.concat([df1, df2, df3, df4, df5])
    df = df.set_axis(selected_att, axis=1)

    # df.loc[df[class_column_name] == "spam", class_column_name] = 'malicious'
    # df.loc[df[class_column_name] == "phishing", class_column_name] = 'malicious'
    # df.loc[df[class_column_name] == "malware", class_column_name] = 'malicious'
    # df.loc[df[class_column_name] == "Defacement", class_column_name] = 'malicious'
   
    #Creates an array with a code for each class for each example
    class_colors = df[class_column_name].astype("category").cat.codes
    #plt.scatter(df['domain_token_count'], df['Entropy_Domain'], c=appcolor, s=10, cmap='viridis')   

    #df = a pandas dataset
    #c = the color codes for each class
    pandas.plotting.scatter_matrix(
        df, 
        c=class_colors, 
        figsize=(30,30), 
        hist_kwds={'bins': 10}, 
        s=100, 
        marker='.', 
        alpha=.7
    )

    plt.show()


if __name__ == '__main__':

    if len(sys.argv) < 2:
        exit("Usage: extract_features.py <csv_file>")
    
    do_main(
        csv_file=sys.argv[1], 
        selected_att=MANUALLY_SELECTED_ATT,
        class_column_name='URL_Type_obf_Type'
    )

