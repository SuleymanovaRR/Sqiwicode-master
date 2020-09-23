import time
print(time.gmtime(0))

for x in range(5):
    time.sleep(2)
    print("Slept for 2 seconds")

a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
print(a) # '2017-04-05-00.11.20'