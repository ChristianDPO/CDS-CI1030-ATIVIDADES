#!/usr/bin/env python
from pandas.plotting import scatter_matrix

import sys
import pandas
import matplotlib.pyplot as plt
from sklearn import preprocessing

MANUALLY_SELECTED_ATT = [
    'Entropy_Domain', 
    'argPathRatio', 
    'ArgUrlRatio',
    'argDomanRatio', 
    'pathurlRatio',
    'CharacterContinuityRate', 
    'NumberRate_FileName', 
    'domainUrlRatio', 
    'NumberRate_URL', 
    'pathDomainRatio', 
    'NumberRate_AfterPath', 
    'avgpathtokenlen',
    'URL_Type_obf_Type'
]

DATASET_CLASS_COLUMN_NAME = 'URL_Type_obf_Type'


def scattermatrix(csv_file, class_column_name, n_samples, selected_att=None):
    """
    Creates an scattermatrix for the ISCXURL2016 url dataset

    :param str csv_file: path to the csv file
    :param str class_column_name: the name of the csv column with the class labels
    :param int n_samples: Number of samples to use in plot
    :param list[str] selected_att: The attributes (column names) from the CSV file to
    compare in the scatter matrix
    """

    # Reads CSV file with data
    dataset = pandas.read_csv(csv_file)

    # Splits CSV file by chosen atributes
    if selected_att:
        ds_sel = dataset[ selected_att ]
    else:
        ds_sel = dataset

    #Remove valuens with 'NaN'
    ds_sel.dropna(inplace=True) 

    #Print dataset head
    print(ds_sel.head())

    # Chooses N examples for each class for plotting
    df1 = ds_sel.loc[ds_sel[class_column_name] == 'benign'].sample(n=n_samples)
    df2 = ds_sel.loc[ds_sel[class_column_name] == 'spam'].sample(n=n_samples)
    df3 = ds_sel.loc[ds_sel[class_column_name] == 'phishing'].sample(n=n_samples)
    df5 = ds_sel.loc[ds_sel[class_column_name] == 'malware'].sample(n=n_samples)
    df4 = ds_sel.loc[ds_sel[class_column_name] == 'Defacement'].sample(n=n_samples)
    df = pandas.concat([df1, df2, df3, df4, df5])
   
    #Creates an array with a code for each class for each example
    class_colors = df[class_column_name].astype("category").cat.codes

    #Resize class labels
    plt.rcParams['axes.labelsize'] = 5

    pandas.plotting.scatter_matrix(
        df, 
        c=class_colors, 
        figsize=(30,30), 
        s=100, 
        marker='.', 
        alpha=.7
    )
    plt.show()


if __name__ == '__main__':

    if len(sys.argv) < 2:
        exit("Usage: scattermatrix.py <csv_file>")
    
    scattermatrix(
        csv_file=sys.argv[1], 
        class_column_name=DATASET_CLASS_COLUMN_NAME,
        n_samples=50,
        selected_att=MANUALLY_SELECTED_ATT
    )

