""" import getpass

pw = getpass.getpass("Pass : ")
# pw = input("Pass :")
print(pw)
 """
 
""" import hashlib
hl = hashlib.sha256()
target = "hello"

hl.update(target.encode("utf-8"))
print(hl.hexdigest()) """


""" import Crypto.Hash.keccak as kek
kksh = keccak.new(digest_bits=256)
kksh.update(target.encode("utf-8"))
print(kksh.hexdigest())
print(kksh.digest())
 """
"""  """
#활용
"""import hashlib
import os 

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass:')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True
if pwInsert():
    pw = input('new pass :')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password")"""


#시스템정보 확인
"""import platform as pf
pn = pf.uname()
pm = pf.machine()
pp = pf.processor()
ps = pf.system()

print(pn)
print(pm)
print(pp)
print(ps)"""

#웹페이지 읽기
# import urllib.request as ur

# url = 'https://www.google.com'

# # res = urllib.request.urlopen(url)
# res = ur.urlopen(url)
# web = res.read()

# with open("ul.html", "wb") as fp:
#     fp.write(web)

# print(web)

"""import http.client as hc
url = 'v.daum.net'

# conn = http.client.HTTPSConnection(url)
conn = hc.HTTPSConnection(url)
conn.request("GET", "/v/20231106154200061")

r = conn.getresponse()
with open("ulcl.html", "wb") as fp:
    fp.write(r.read())
print(r)
"""




# import requests
# url = "https://www.google.com"
# res = requests.get(url)
# web = res.content

# with open("ulrp.html", "wb") as fp:
#     fp.write(web)


#멀티 스레드 
""" import threading
def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
start = time.time()
for i in range(3) :
    counter(f"num{i}")
end = time.time()
    print("single end")
print("single end", end - start)
     """
    
"""import threading as td
import time
def counter(str_name):
    for i in range(50000):
         print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.thread(target=counter, args=("1num",))
thread2 = td.thread(target=counter, args=("2num", ))
thread3 = td.thread(target=counter, args=("3num", ))

start = time.time()
thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()

"""

"""
#멀티 프로세싱
import time
import multiprocessing            \
def counter(str_name):
    for i in range(50000):
         print(f"Countdown {i}, name : {str_name}\n")


process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))


start = time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()

"""


#main 실행
def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run()

main()







#비동기 처리









#스케즐









#문자열 비교








