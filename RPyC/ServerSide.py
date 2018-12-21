from rpyc.utils import server
import rpyc

class MyService(rpyc.Service):

    def exposed_NoArgument_NoReturn(self):
        return

    def exposed_OneStringArgument_ReverseStringReturn(self, string):
        string_reversed = string[::-1]
        return string_reversed

    def exposed_OneLongArgument_OneLongReturn(self, long):
        return long

    def exposed_EightLongsArguments_OneLongReturn(self, long1, long2, long3, long4, long5, long6, long7, log8):
        return 88888888888888888

    def exposed_ThreeDoubleArgument_DoubleReturn(self, double1, double2, double3):
        return 4.23456

    def exposed_BinarySearch(self, tuple):
        e = 0
        d = len(tuple[0])-1
        
        while(e <= d):
            m = (int)((e + d)/2)
            if(tuple[0][m] < tuple[1]):
                e = m + 1
            if(tuple[0][m] > tuple[1]):
                d = m - 1
            if(tuple[0][m] == tuple[1]):
                return True
        return False

    def exposed_OneStringArgument_ArrayReturn(self, string):
        array = []
        array.append(string)
        array.append(string)
        array.append(string)
        return array
    
    def exposed_GetMiddleArrayValue(self, array):
        mIndex = int(len(array) / 2)
        return array[mIndex]

    
    def exposed_GetCountry_PersonPhone(self, person):
        country_response = "Unknown"

        if person.phone.code == 55:
            country_response = "Brazil"

        return country_response

    def exposed_AddTwoIntValues(self, values):
        return values[0] + values[1]

if __name__ == '__main__':
    print("SERVER is listening...")
    t = server.ThreadedServer(MyService, hostname='localhost', port=50051, authenticator=None, protocol_config={"allow_all_attrs":True, "allow_setattr":True, "allow_delattr":True})
    t.start()
 