# It is to time function and return average time

def time_fn(fn, *args, rep=4, **kwargs):
  start = time.perf_counter()
  for i in range(rep):
    fn(*args, **kwargs)
  end = time.perf_counter()
  return(end - start) / rep
# Create some functions to time them

def compute_fn_1(n, *, start=0, end):
  results = []
  for i in range(start, end):
    results.append(i**3)
  return results

def compute_fn_2(n, *, start = 1, end):
   return [n**i for i in range(start, end)] 

def compute_fn_3(n, *, start = 1, end):
  return(n**i for i in range(start,end))

# run functions to see results
  
  
    

   
   
   