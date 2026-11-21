# k test cases
# 	n,m,s = nodes, edges, petrol station
#   t = tank space in mililiter
#   m lines
#     a,b,f = a&b shows there is road between node a and b 
#             f means fuel needed in ml
#   s lines
#     x, p = x is node of petrol station, price at that station
#   c,d = c node of company, d is destination
  
  
import sys

def main():

    data = sys.stdin.buffer.read().split()
    p = 0

    k = int(data[p]); p+=1

    for _ in range(k):
        n = int(data[p]); p+=1 # number of nodes
        m = int(data[p]); p+=1 # number of edges
        s = int(data[p]); p+=1 # number of petrol station
        t = int(data[p]); p+=1 # tank space in ml
        
        temp = iter(map(int, data[p: p+m*3])); p += m*3 # input from m lines (not ready yet)
        m_lines = list(zip(temp,temp,temp))
        
        temp = iter(map(int, data[p: p+s*2])); p += s*2 # input of petrol station and price
        s_lines = list(zip(temp,temp))
        
        c, d = int(data[p]), int(data[p+1]); p+=2 # c = starting point, d = destination

        
        
main()