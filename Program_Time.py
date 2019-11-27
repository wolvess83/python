import time

start  = time.time()
for i in range(100):
    for j in range(100):
        print(i*j)
end = time.time()  

print(end - start)