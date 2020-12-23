import re
import urllib.request
from multiprocessing import Process, Value, Lock
counter = Value('i', 0)


def multi_finder(proc_number, lock, pages_per_proc):
    for page_number in range((proc_number) * pages_per_proc, (proc_number) * pages_per_proc + pages_per_proc):
        if page_number > 57 or page_number == 0:
            break
        page = page_number
        with urllib.request.urlopen(urlr + "?page={}".format(page)) as response:
            html = response.read().decode()
            href = re.compile(r"Django 2.0")
            found = list(href.findall(html, re.DOTALL))
            lock.acquire()
            counter.value += len(found)
            lock.release()


urlr, n = input().split()
n = int(n)

lock = Lock()
procs = []

pages_per_proc = 59 // n

for proc_number in range(n):
    proc = Process(target=multi_finder, args=(proc_number, lock, pages_per_proc + 1))
    procs.append(proc)
    proc.start()

for index, proc in enumerate(procs):
    proc.join()

print(counter.value)
