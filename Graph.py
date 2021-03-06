# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import os
import csv
import codecs
import random

def main():

    instance_path = "/Users/tassio/PycharmProjects/Graph---Network-Analyzer"

    file_list = [f for f in os.listdir(instance_path)
    if f.startswith('') and f.endswith('.csv')]
    for filename in sorted(file_list):
        G = nx.Graph()
        print(filename)
        path = os.path.join(instance_path, filename)
        imports=0
        with codecs.open(path,'r') as f:
            csv_f = csv.reader((line.replace('\0','') for line in f), delimiter=';')
            print("Creating Graph")
            for row in enumerate(csv_f):
                if imports != 0:
                    cep = row[1][1]
                    pessoa = row[1][0]
                    G.add_node(cep)
                    G.add_node(pessoa)
                    G.add_edge(cep, pessoa)

                if imports % 10000 == 0:
                    print("Lines Imports: {} ".format(imports))

                imports+=1

        C=nx.connected_component_subgraphs(G)
        for g in C:
            c=[random.random()]*nx.number_of_nodes(g)
            nx.draw_random(g,node_size=40,node_color=c,vmin=0.0,vmax=1.0,with_labels=False)
        plt.savefig('graph.png', dpi=300)
        plt.show()

if __name__ == '__main__':
    main()
