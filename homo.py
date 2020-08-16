# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import os
import csv
import codecs

def main():

    instance_path = "/Users/tassio/PycharmProjects/Graph---Network-Analyzer"

    file_list = [f for f in os.listdir(instance_path)
    if f.startswith('') and f.endswith('1408.csv')]
    for filename in sorted(file_list):
        G = nx.MultiGraph()
        print(filename)
        path = os.path.join(instance_path, filename)
        imports=0
        calcamento = []
        with codecs.open(path,'r') as f:
            calcamento.append("yellow")
            csv_f = csv.reader((line.replace('\0','') for line in f), delimiter=';')
            print("Creating Graph")
            for row in enumerate(csv_f):
                if imports != 0:
                    cal = row[1][1]
                    nis = row[1][0]
                    cep = row[1][2]
                    G.add_edge(cep, nis)
                    if cal == "total":
                        calcamento.append("red")
                    elif cal == "nao_existe":
                        calcamento.append("blue")
                    else:
                        calcamento.append("green")

                if imports % 10000 == 0:
                    print("Lines Imports: {} ".format(imports))

                imports+=1

        nx.draw(G, node_color=calcamento, with_labels=True)
        plt.show()

if __name__ == '__main__':
    main()
