import  rpyc, sys
sys.path.append("../RPC-Analist")
import Analyst as anly
import time

# Definição da chamada RPC para o servidor
# Estabelece conexão(endereço, porta) e realiza batch de serviços disponíveis
def RPC_CALL():

    # IPV4 Address : 192.168.1.36 port - 50051
    connection = rpyc.connect("localhost", 50051, config={"allow_all_attrs":True, "allow_setattr":True, "allow_delattr":True})
    test_cases = 10
    type = "localhost"

    # Teste 1 : Sem argumentos e retorno vazio
    array_results = []
    for i in range(test_cases):
        # Inicializa um contador para medir o tempo decorrido da chamada
        start = time.time()
        
        # Operação 1 : Sem argumentos e Sem retorno
        connection.root.NoArgument_NoReturn()
        
        # Encerra a chamada do time inicializado na linha 11 e calcula a diferença
        end = time.time()
        array_results.append(end - start)

    outputName = "T1Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2 : Recebe String e devolve invertida(Tamanho 4)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneStringArgument_ReverseStringReturn("Luan")
        end = time.time()
        array_results.append(end - start)

    outputName = "T2Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.1 : Recebe String e devolve invertida(Tamanho 8)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneStringArgument_ReverseStringReturn("LuanLuan")
        end = time.time()
        array_results.append(end - start)

    outputName = "T2.1Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.2 : Recebe String e devolve invertida(Tamanho 16)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneStringArgument_ReverseStringReturn("LuanLuanLuanLuan")
        end = time.time()
        array_results.append(end - start)

    outputName = "T2.2Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.3 : Recebe String e devolve invertida(Tamanho 32)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneStringArgument_ReverseStringReturn("LuanLuanLuanLuanLuanLuanLuanLuan")
        end = time.time()
        array_results.append(end - start)

    outputName = "T2.3Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.4 : Recebe String e devolve invertida(Tamanho 64)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneStringArgument_ReverseStringReturn("LuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuan")
        end = time.time()
        array_results.append(end - start)

    outputName = "T2.4Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.5 : Recebe String e devolve invertida(Tamanho 128)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneStringArgument_ReverseStringReturn("LuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuan")
        end = time.time()
        array_results.append(end - start)

    outputName = "T2.5Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 3 : Argumento Long e Retorno Long
    long_number = 92233720368547
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneLongArgument_OneLongReturn(long_number)
        end = time.time()
        array_results.append(end - start)
   
    outputName = "T3Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 4 : Oito Argumentos Long e Retorno Long
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.EightLongsArguments_OneLongReturn(long_number+1, long_number+2, long_number+long_number, long_number*2, long_number*3, long_number*10, long_number*15, long_number )
        end = time.time()
        array_results.append(end - start)
    
    outputName = "T4Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 5 : Soma de valores int 32 a e b
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.AddTwoIntValues((5, 6))
        end = time.time()
        array_results.append(end - start)
    
    outputName = "T5Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 6.0 : Dois inteiros int32 com 9 digitos
    int_bigger = 536870912
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.AddTwoIntValues((int_bigger, int_bigger))
        end = time.time()
        array_results.append(end - start)
    
    outputName = "T6Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 7.0 : Três argumentos doubles, um retorno double
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.ThreeDoubleArgument_DoubleReturn(4.562, 4.632, 23.43561)
        end = time.time()
        array_results.append(end - start)

    outputName = "T7Rpc-" + type
    anly.makeTestFile(array_results, outputName)

   # Teste 8.0 : Serviço de busca binária que retorna um booleano
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.BinarySearch(([2, 3, 6, 7, 10, 15, 22, 34, 44, 52], 66))
        end = time.time()
        array_results.append(end - start)

    outputName = "T8Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 9.0 : Recebe um string e retorna uma array de strings
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.OneStringArgument_ArrayReturn("Luan")
        end = time.time()
        array_results.append(end - start)

    outputName = "T9Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 10.0 : Pega o valor no meio da array
    array_results = []
    for i in range(test_cases):
        start = time.time()
        connection.root.GetMiddleArrayValue([32, 66, 45, 33, 90])  
        end = time.time()
        array_results.append(end - start)

    outputName = "T10Rpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 11.0 : Classe complexa, retorna o país do código de area do telefone
    array_results = []
    for i in range(test_cases):
        home_phone = Phone(55, 11, 45456545)
        person = Person("Maria", 22, home_phone)
        start = time.time()    
        connection.root.GetCountry_PersonPhone(person)
        end = time.time()
        array_results.append(end - start)

    outputName = "T11Rpc-" + type
    anly.makeTestFile(array_results, outputName)

class Person:
    
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = P  hone(phone.code, phone.ddd, phone.number)

class Phone:
    
    def __init__(self, code, ddd, number):
        self.code = code
        self.ddd = ddd
        self.number = number

# Chamada para o servidor
if __name__ == '__main__':
    RPC_CALL()