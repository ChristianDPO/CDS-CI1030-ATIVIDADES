#!/usr/bin/env python
from pandas.plotting import scatter_matrix

import sys
import pandas
import numpy as np

import matplotlib.pyplot as plt

import sklearn.cluster as cluster
import sklearn.decomposition as decomposition


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

#More info in https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html
def kmeans_cluster_graph(csv_file, class_column_name, n_clusters=None, selected_att=None):
    """
    Creates a kmeans cluster graph for the a dataset, using Principal component analysis (PCA) to reduce dimensions

    :param str csv_file: path to the csv file
    :param str class_column_name: the name of the csv column with the class labels
    :param int n_clusters: Number of clusters to use. Defaults to number of unique class labels of the class column
    :param list[str] selected_att: The attributes (column names) from the CSV file to
    use
    """

    # Reads CSV file with data
    dataset = pandas.read_csv(csv_file, index_col=0)

    # Splits CSV file by chosen atributes
    if selected_att:
        df = dataset[ selected_att ]
    else:
        df = dataset

    #Remove valuens with 'NaN'
    df.dropna(inplace=True) 

    #Counts unique class labels
    if not n_clusters:
        n_clusters = len(df[class_column_name].unique())
    print(f"Using {n_clusters} clusters")

    #PDA to project the data in two dimensions for the graph
    df_data = df.drop(columns=[class_column_name])
    reduced_data = decomposition.PCA(n_components=2).fit_transform(df_data)

    #Kmeans
    kmeans = cluster.KMeans(init="k-means++", n_clusters=n_clusters)
    kmeans.fit(reduced_data)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = 0.02  # point in the mesh [x_min, x_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(
        Z,
        interpolation="nearest",
        extent=(xx.min(), xx.max(), yy.min(), yy.max()),
        cmap=plt.cm.Paired,
        aspect="auto",
        origin="lower",
    )

    plt.plot(reduced_data[:, 0], reduced_data[:, 1], "k.", markersize=2)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(
        centroids[:, 0],
        centroids[:, 1],
        marker="x",
        s=169,
        linewidths=3,
        color="w",
        zorder=10,
    )
    plt.title(
        "K-means clustering on the dataset (PCA-reduced data)\n"
        "Centroids are marked with white cross"
    )
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()


if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit("Usage: kmeans_cluster_graph.py <csv_file> <class_column_name> (opt) <n_clusters>")

    kmeans_cluster_graph(
        csv_file=sys.argv[1], 
        class_column_name=sys.argv[2],
    )

