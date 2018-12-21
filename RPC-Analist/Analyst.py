import sys, os
sys.path.append("../")
import numpy as np
import PlotGraph as plt

def makeTestFile(array, name):
    
    f = open(os.path.join("Data/", name), "w")
    
    for item in array:
        f.write("%s\n" %(str(item)))

def makeArrayFromFile(name):

    f = open(os.path.join("Data/", name), "r+")
    array_results = []
 
    i = 0
    while i < 9:
        c = f.readline()

        array_results.append(float(c.strip()))
        i = i + 1

    return array_results

# Criação de gráfico para comparação de doois conjuntos de dados
def makeGraphTypeI(): 
    
    array_compare =[]
    inputName = "T1Rpc-external"
    array_rpc = makeArrayFromFile(inputName)
    inputName = "T1Grpc-external"
    array_grpc = makeArrayFromFile(inputName)

    array_compare.append(array_rpc)
    array_compare.append(array_grpc)

    figure_name = "Compare_GRPCxRPYC_T1"
    text = "Análise Comparativa I : Sem Argumentos - Sem Retorno"

    plt.PlotGraph(array_compare, figure_name, text)

# Criação de gráfico para comparação de mais de dois conjuntos de dados
def makeGraphTypeII(nGroups):

    array_mean_localhost = []
    array_mean_external = []
    array_std_localhost = []
    array_std_external = []

    inputName = "T2Rpc-external"
    array_rpc = makeArrayFromFile(inputName)
    inputName = "T2Grpc-external"
    array_grpc = makeArrayFromFile(inputName)

    array_mean_localhost.append(np.mean(array_rpc))
    array_mean_external.append(np.mean(array_grpc))
    
    array_std_localhost.append(np.std(array_rpc))
    array_std_external.append(np.std(array_grpc))

    i = 1

    while(i < nGroups):
        inputName = "T2.%iRpc-external" %i
        array_rpc = makeArrayFromFile(inputName)
        inputName = "T2.%iGrpc-external" %i
        array_grpc = makeArrayFromFile(inputName)

        array_mean_localhost.append(np.mean(array_rpc))
        array_mean_external.append(np.mean(array_grpc))
    
        array_std_localhost.append(np.std(array_rpc))
        array_std_external.append(np.std(array_grpc))
        i = i + 1

    list_values = ['String(4)','String(8)', 'String(16)', 'String(32)', 'String(64)', 'String(128)']
    text = "Análise Comparativa II : Comparação de Strings de Diferentes Tamanhos"
    figure_name = "Compare_GRPCxRPYC_T2"
    plt.PlotGraphII(array_mean_localhost, array_mean_external, array_std_localhost, array_std_external, nGroups, list_values, text, figure_name)


if __name__ == '__main__':

    makeGraphTypeI()
    makeGraphTypeII(6)
