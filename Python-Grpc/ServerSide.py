import grpc

from concurrent import futures
import time

import messages_struct_pb2 as proto
import messages_struct_pb2_grpc as proto_grpc

class ServicesImplementation(proto_grpc.ServicesServicer):
    
    def AddTwoIntValues(self, request, context):  
        result = request.a + request.b
        return proto.AddResult(c = result)
    
    def AddTwoIntValues_SignedInt(self, request, context):
        result = request.a + request.b
        return proto.AddResponse_Signed(a = result)

    def AddTwoIntValues_FixedInt(self, request, context):
        result = request.a + request.b
        return proto.AddResponse_Fixed(a = result)

    def NoArgument_NoReturn(self, request, context):
        return proto.Empty()

    def OneStringArgument_ReverseStringReturn(self, request, context):
        string_reversed = request.name[::-1]
        return proto.String(name = string_reversed)

    def OneLongArgument_OneLongReturn(self, request, context):
        return proto.Long(a = request.a - 9000)

    def GetMiddleArrayValue(self, request, context):
        mIndex = int(len(request.i) / 2)
        return proto.ItemResponse(r = request.i[mIndex])

    def GetCountry_PersonPhone(self, request, context):
        country_response = proto.Country(name = "Unknown")

        if request.phone.code == 55:
            country_response = proto.Country(name = "Brazil")

        return country_response

    def SetHashFunction(self, request, context):
        hash_functions = dict(request.cryp_hashes.items())
        response = hash_functions.popitem()      
        return response[1]

    def EightLongsArguments_OneLongReturn(self, request, context):
        return proto.Long(a = 88888888888888888)

    def OneLongArgument_OneOf_OneLongReturn(self, request, context):
        return proto.Long(a = 88888888888888888)

    def BinarySearch(self, request, context):
        e = 0
        d = len(request.a)-1
        
        while(e <= d):
            m = (int)((e + d)/2)
            if(request.a[m] < request.b):
                e = m + 1
            if(request.a[m] > request.b):
                d = m - 1
            if(request.a[m] == request.b):
                return proto.Boolean(a = True)
        return proto.Boolean(a = False)

    def OneStringArgument_ArrayReturn(self, request, context):
        array = []
        array.append(request.name)
        array.append(request.name)
        array.append(request.name)
        return proto.StringArray(array = array)

    def ThreeDoubleArgument_DoubleReturn(self, request, context):
        return proto.RealDouble(a = 4.23456)

def StartServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    proto_grpc.add_ServicesServicer_to_server(ServicesImplementation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is listening...")

    try:
        while True:
            time.sleep(2000)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    StartServer()
