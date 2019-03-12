import pprint

class LogRow:

    def __init__(self):
        self.row = {}

    @staticmethod
    def sliceUntil(begin_char,stop_char, msg):
        chunk=""
        offset = 0
        for i, char in enumerate(msg):
            offset += 1
            if char == begin_char:
                for i, char in enumerate(msg[offset:]):  #start slicing from first quotation
                    offset += 1
                    if char != stop_char:
                        chunk += char
                    else:
                        break
                break
        return(chunk,offset)

    def parseRow(self, msg):
        ip = ""
        for i, char in enumerate(msg):
            pointer = i
            if char[0] != " ":
                ip += char[0]
            else:
                break
        #parse date
        date = msg[pointer+6:pointer+32]
        pointer = pointer+32
        #parse http
        http, offset= self.sliceUntil("\"","\"", msg[pointer:])
        pointer+=offset

        #parse response
        response, offset = self.sliceUntil(" ","-", msg[pointer:])
        response = response[:-2]
        pointer += offset


        #parse dash

        dash, offset = self.sliceUntil("\"", "\"", msg[pointer-2:])
        os = msg[pointer+3:]
        row = {
            "ip": ip,
            "date": date,
            "http": http,
            "response": response,
            "os": os
        }
        self.ip = ip
        self.date = date
        self.http = http
        self.response = response
        self.os = os
        return(row)



