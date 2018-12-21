import grpc
import time
import sys
sys.path.append("../RPC-Analist")
import messages_struct_pb2 as proto
import messages_struct_pb2_grpc as proto_grpc
import Analyst as anly

def RunClient():

    # Criando canal para conexão com o servidor do lado cliente e instanciando stub dos serviços
    # IPV4 Address : 192.168.1.36 port - 50051
    # Type pode ser external ou localhost
    type = "localhost"
    channel = grpc.insecure_channel('localhost:50051')
    stub = proto_grpc.ServicesStub(channel)
    test_cases = 10
    
    # Teste 1 : Sem argumentos e retorno vazio
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.NoArgument_NoReturn(proto.Empty())
        end = time.time()
        array_results.append(end - start)

    outputName = "T1Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.0 : Recebe String e devolve invertida(Tamanho 4)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneStringArgument_ReverseStringReturn(proto.String(name = "Luan"))
        end = time.time()
        array_results.append(end - start) 

    outputName = "T2Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.1 : Recebe String e devolve invertida(Tamanho 8)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneStringArgument_ReverseStringReturn(proto.String(name = "LuanLuan"))
        end = time.time()
        array_results.append(end - start) 

    outputName = "T2.1Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.2 : Recebe String e devolve invertida(Tamanho 16)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneStringArgument_ReverseStringReturn(proto.String(name = "LuanLuanLuanLuan"))
        end = time.time()
        array_results.append(end - start)    

    outputName = "T2.2Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.3 : Recebe String e devolve invertida(Tamanho 32)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneStringArgument_ReverseStringReturn(proto.String(name = "LuanLuanLuanLuanLuanLuanLuanLuan"))
        end = time.time()
        array_results.append(end - start) 

    outputName = "T2.3Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.4 : Recebe String e devolve invertida(Tamanho 64)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneStringArgument_ReverseStringReturn(proto.String(name = "LuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuan"))
        end = time.time()
        array_results.append(end - start)  

    outputName = "T2.4Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 2.5 : Recebe String e devolve invertida(Tamanho 128)
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneStringArgument_ReverseStringReturn(proto.String(name = "LuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuanLuan"))
        end = time.time()
        array_results.append(end - start) 

    outputName = "T2.5Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 3.0 : Recebe um long e devolve um long
    long_number = 92233720368547
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneLongArgument_OneLongReturn(proto.Long(a = long_number))
        end = time.time()
        array_results.append(end - start)

    outputName = "T3Grpc-" + type
    anly.makeTestFile(array_results, outputName)
    
    # Teste 3.1 : Recebe um long em tempo de execução(oneOf) e devolve um long
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneLongArgument_OneOf_OneLongReturn(proto.OneofLong(d = long_number))
        end = time.time()
        array_results.append(end - start)

    outputName = "T3.1Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 4.0 : Comparando envio de oito argumentos long com o envio de um argumento long
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.EightLongsArguments_OneLongReturn(proto.RealLong(a = long_number+1, b = long_number+2, c = long_number+long_number, d = long_number*2, e = long_number*3, f = long_number*10, g = long_number*15, h = long_number))
        end = time.time()
        array_results.append(end - start)

    outputName = "T4Grpc-" + type
    anly.makeTestFile(array_results, outputName)
    
    # Teste 5.0 : Envia dois inteiros de tamanho 1 e retorna 1 inteiro
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.AddTwoIntValues(proto.AddRequest(a = 5, b = 6))
        end = time.time()
        array_results.append(end - start)

    outputName = "T5Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 6.0 : Dois inteiros int32 x inteiros fixed
    array_results = []
    for i in range(test_cases):
        int_bigger = 536870912
        start = time.time()
        stub.AddTwoIntValues(proto.AddRequest(a = int_bigger, b = int_bigger))
        end = time.time()
        array_results.append(end - start)

    outputName = "T6Grpc-" + type
    anly.makeTestFile(array_results, outputName)
    
    # Teste 6.1 : Adicionado dois inteiros fixed, comparação para valores acima de 2^28-1 com int32
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.AddTwoIntValues_FixedInt(proto.AddRequest(a = int_bigger, b = int_bigger))
        end = time.time()
        array_results.append(end - start)

    outputName = "T6.1Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 6.2 : Comparando signed int com int32 para valores negativos
    negative_a = -82102222
    negative_b = -8900989
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.AddTwoIntValues(proto.AddRequest(a = negative_a, b = negative_b))
        end = time.time()
        array_results.append(end - start)

    outputName = "T6.2Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 6.3 : Adicionado dois inteiros signed negativos, comparando com int32
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.AddTwoIntValues_SignedInt(proto.AddRequest(a = negative_a, b = negative_b))
        end = time.time()
        array_results.append(end - start)

    outputName = "T6.3Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 7.0 : Três argumentos doubles, um retorno double
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.ThreeDoubleArgument_DoubleReturn(proto.RealDouble(a = 4.562, b = 4.632, c = 23.43561))
        end = time.time()
        array_results.append(end - start)

    outputName = "T7Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 8.0 : Serviço de busca binária que retorna um booleano
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.BinarySearch(proto.Tuple(a = [2, 3, 6, 7, 10, 15, 22, 34, 44, 52], b = 66))
        end = time.time()
        array_results.append(end - start)

    outputName = "T8Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 9.0 : Recebe um string e retorna uma array de strings
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.OneStringArgument_ArrayReturn(proto.String(name = "Luan"))
        end = time.time()
        array_results.append(end - start)

    outputName = "T9Grpc-" + type
    anly.makeTestFile(array_results, outputName)
    
    # Teste 10.0 : Pega o valor no meio da array
    array_results = []
    for i in range(test_cases):
        start = time.time()
        stub.GetMiddleArrayValue(proto.ItemQuery(i = [32, 66, 45, 33, 90]))  
        end = time.time()
        array_results.append(end - start)

    outputName = "T10Grpc-" + type
    anly.makeTestFile(array_results, outputName)

    # Teste 11.0 : Classe complexa, retorna o país do código de area do telefone
    array_results = []
    for i in range(test_cases):
        home_phone = proto.Phone(code = 55, ddd = 11, number = 45456545)
        start = time.time()
        stub.GetCountry_PersonPhone(proto.Person(name = "Maria", age = 22, phone = home_phone))
        end = time.time()
        array_results.append(end - start)

    outputName = "T11Grpc-" + type
    anly.makeTestFile(array_results, outputName)
   
   # Teste Extra - Grpc : map e Classes complexa
    array_results = []
    for i in range(test_cases):
        md5_algorithm = proto.Hash.Algorithm(name = "MD5", output_size = 128, block_size = 512)
        md5_hash = proto.Hash(algorithms = [md5_algorithm], intern_size = 128, rounds = 64)
        sha1_algorithm = proto.Hash.Algorithm(name = "SHA1", output_size = 160, block_size = 512)
        sha1_hash = proto.Hash(algorithms = [sha1_algorithm], intern_size = 160, rounds = 80)
        sha2_algorithm = proto.Hash.Algorithm(name = "SHA-256", output_size = 256, block_size = 512)
        sha2_hash = proto.Hash(algorithms = [sha2_algorithm], intern_size = 256, rounds = 64)
        start = time.time()
        stub.SetHashFunction(proto.HashFunction(cryp_hashes = {'MD5': md5_hash, 'SHA1' : sha1_hash, "SHA-256" : sha2_hash}))
        end = time.time()
        array_results.append(end - start)

    outputName = "T12Grpc-" + type
    anly.makeTestFile(array_results, outputName)


if __name__ == '__main__':
    RunClient()