import threading 
import socket
import time
from queue import Queue
from netaddr.ip import IPNetwork 
class Scanner():
    print_lock = threading.Lock()
    def __init__(self, ip):
        self.q = Queue()
        self.target = ip
    def portscan(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((self.target, port))
            with print_lock:
                print('Port: '+ str(port) + ' is open')
            con.close()
        except:
            pass
    def threader(self):
        while True:
            worker = self.q.get()
            portscan(worker)
            self.q.task_done()
    # Starts threading
    def start(self):
        for x in range(30):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start
        start = time.time()
    # port range 1-1024
    def ports(self):
        for worker in range(1, 1024):
            self.q.put(worker)
        self.q.join()