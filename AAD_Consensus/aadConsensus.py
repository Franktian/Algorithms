import math

class AADConesnsus():

    pid = 0
    val = 0
    rounds = 1
    maxrounds = 0

    def __init__(pid, v, e, value_range):
        val = v
        maxrounds = math.log(value_range / float(e)) / math.log(2) 

    def broadcast(pid, value, rd):
        '''
        Abstract Method
        '''
        raise NotImplementedError()

    def on_received_message(process, message, rd):
