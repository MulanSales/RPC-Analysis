import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np
import os
    
def PlotGraph(array_results, figure_name, text):
    plt.figure(figsize=(13,6))

    plt.title(figure_name)

    array_mean = []
    array_stdev = []
    for array in array_results:
        array_mean.append(np.mean(array))
        array_stdev.append(np.std(array))

    array_fstdev = []
    array_fstdev.append(array_stdev)
    array_fstdev.insert(0, (0, 0))
    width = 0.25
    ind = np.arange(len(array_mean))
    colours = ['green','orange']

    plt.figure(figure_name, figsize=(12, 8))
    plt.title(text)
    plt.bar(ind, array_mean, width, color=colours, yerr=array_fstdev, ecolor='k')

    plt.xticks(ind,('RPyC','gRPC'))
    plt.xlabel('Cenários de Teste')
    plt.ylabel('Tempo Decorrido(s)')

    plt.savefig(os.path.join("../Outputs/",figure_name))

def PlotGraphII(array_mean_localhost, array_mean_external, array_std_localhost, array_std_external, n_groups, list_values, text, figure_name):
    plt.figure(figsize=(13,6))

    means_localhost = array_mean_localhost
    std_localhost = array_std_localhost

    means_external = array_mean_external
    std_external = array_std_external

    array_fstdev_localhost = []
    array_fstdev_localhost.append(std_localhost)
    array_fstdev_external = []
    array_fstdev_external.append(std_external)

    if(n_groups == 2):
        array_fstdev_localhost.insert(0, (0, 0))
        array_fstdev_external.insert(0, (0, 0))
    if(n_groups == 6):
        array_fstdev_localhost.insert(0, (0, 0, 0, 0, 0, 0))
        array_fstdev_external.insert(0, (0, 0, 0, 0, 0, 0))

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, means_localhost, bar_width,
                    alpha=opacity, color='green',
                    yerr=array_fstdev_localhost, error_kw=error_config,
                    label='RPyC')

    rects2 = plt.bar(index + bar_width, means_external, bar_width,
                    alpha=opacity, color='orange',
                    yerr=array_fstdev_external, error_kw=error_config,
                    label='gRPC')

    plt.xlabel('Cenários de Teste')
    plt.ylabel('Tempo Decorrido(s)')
    plt.title(text)
    plt.xticks(index + bar_width / 2, list_values)
    plt.legend()

    plt.savefig(os.path.join("../Outputs/", figure_name))