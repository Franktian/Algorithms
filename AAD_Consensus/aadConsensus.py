import math

__author__ = "Tamaki Sakura"
__copyright__ = "Copyright 2015, Shirasaki Academy"
__license__ = "WTFPL"
__contact__ = "tamaki.sakura in hotmail.com"

class AADConesnsus():
    # AAD Consensus
    # Each Individual Instance of this object is
    # designed to be 1 process and can only running on 1 thread only.

    def __init__(self, num_proc, my_pid, value, value_range):
        self.my_pid = pid
        self.val = float(value)
        self.rounds = 1
        
        self.maxrounds = math.log(value_range / float(e)) / math.log(2) 
        self.num_proc = int(num_proc)
        self.maxerror = (self.num_proc - 1) / 4

        self.messgae_dic = {}
        self.accept_message_dict={}
        self.send_dict = {}

    def __run__():
        self._round_init()

    def broadcast(self, pid, value, rd):
        '''
        Abstract Method, should be implemented in your network protocal
        message should be a reliable broadcast to other processes here
        where message must includes all of
        (process_id, value_in_float, round_you_are_in)
        '''
        raise NotImplementedError()

    def on_received_message(self, process_send, process, message, rd):
        '''
        Attach this fucntion to your network listener.
        called with process_id_where_message_come_from, process_in_message, 
        value_received_in_message_in_float, round_you_recieved_in_message

        It's OK if the information received by the listener
        is unable to decoded into process/message/round,
        but at that situation it is useless 
        (and not harmful, if at least you trim their type right)
        to call this function.
        '''
        current_msg_count = self._add_to_message_stack(process_send, process, message, rd)
        if (process_send == process):
            self._message_echo(process, message, rd)
        if (current_msg_count >= self.maxerror + 1):
            self._message_echo(process, message, rd)
        else if (current_msg_count >= self.num_proc - self.maxerror):
            accept_msg_count = self._add_to_accpet_message_stack(message, rd)
            if (rd == self.rounds):
                self._try_process_to_next_round()

    def on_terminate(self, final_value):
        '''
        Abstract Method, called with the final decided value where
        you can received from this function and then quit the object.
        '''
        raise NotImplementedError()

    def _round_init(self):
        self.send_dict[(self.my_pid, self.rounds)] = True
        self.broadcast(self.my_pid, self.val, self.rounds)

    def _try_process_to_next_round(self):
        if (len(self.accept_message_dict[self.rounds]) >= self.num_proc - self.maxerror):
             accept_message_list = self.accept_message_dict[rd]
             accept_message_list.sort()
             self.val = (accept_message_list[t] + accept_message_list[-t-1]) / 2.0 
             if (self.rounds > self.maxrounds):
                 self.on_terminate(self.val)
             else:
                 self.rounds += 1
                 self._round_init()
                 self._try_process_to_next_round()

    def _message_echo(self, process, message, rd)
        if (self.send_dic.get((process, rd)) is None):
            self.send_dict[(process, rd)] = True
            self.broadcast(process, message, rd)

    def _add_to_message_stack(self, process_send, process, message, rd):
        if (self.message_dict.get(rd) is None):
            self.message_dict[rd] = {}
        now_message_dict = self.message_dict[rd]
        if (now_message_dict.get((process, messgae)) is None):
            now_message_dict[(process, message)] = set()
        now_message_set = now_message_dict[(process, message)]
        now_message_set.add(process_send)
        return len(now_message_set)

    def _add_to_accept_message_stack(self, message, rd):
        if (self.accept_message_dict.get(rd) is None):
            self.accept_message_dict[rd] = []
        accept_message_list = self.accept_message_dict[rd]
        accept_message_list.add(message)
        return len(accept_message_list)
         
