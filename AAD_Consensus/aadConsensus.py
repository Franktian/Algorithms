import math

class AADConesnsus():


    def __init__(self, p_count, my_pid, v, e, value_range):
        self.n = p_count
        self.my_pid = pid
        self.val = float(v)
        self.rounds = 1
        self.maxrounds = math.log(value_range / float(e)) / math.log(2) 
        self.messgae_dic = {}
        self.send_dic = {}

    def broadcast(self, pid, value, rd):
        '''
        Abstract Method, should be implemented in your network protocal
        message should be broadcast to other processes here
        where message must includes all of
        (process_id, value_in_float, round_you_are_in)
        '''
        raise NotImplementedError()

    def on_received_message(self, process, message, rd):
        '''
        Attach this fucntion to your listener
        message is a three-variable tuple in the form of:
        (process_id, value_in_float, round_you_recieved)
        '''
        current_count = add_to_message_stack(message)
        messgae_echo(message)

        if (current_count > (n / 4)):
            # prepare to accpet
    
    def message_echo(message)
        (p, m, h) = message
        if (self.send_dic.get((p,h)) is None):
            # go with echo, but more detail is needed


    def add_to_message_stack(self, message):
        if (self.message_dic.get(messgae) is None):
            self,message_dic[message] = 1
            return 1
        else: 
            self.message_dic[message] += 1
            return self.message_dic[message]


