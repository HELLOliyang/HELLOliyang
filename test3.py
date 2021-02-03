import requests
import threading
class Test:
    def __int__(self):
        self.session = requests.session()
        return self.session
    def start(self):
        print(id(Test()))
    def test(self,arr):
        n = len(arr)
        for i in range(n):
            for j in range(0,n-j-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
        return arr
if __name__ == '__main__':
    base = Test()
    for i in range(3):
        threading.Thread(target=base.start).start()