import r2pipe
import json

class NetworkString:
    # Attributes
    value
    address
    comment
    section
    
    def __init__(self,value,address,comment,section):
        self.value = value
        self.address = address
        self.comment = comment
        self.section = section
    
    