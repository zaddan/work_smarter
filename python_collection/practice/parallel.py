from joblib import Parallel, delayed  
import multiprocessing

inputs = range(100)  
def processInput(i, j):  
    print multiprocessing.current_process()._identity[0] - 1
    return i * j

num_cores = multiprocessing.cpu_count()

print("numCores = " + str(num_cores))
j = 0
results = Parallel(n_jobs=num_cores)(delayed(processInput)(i, j) for i in inputs)  

print(results)
