tests = int(input())
ans = []

for _ in range(tests):
  
  n, q, g = input().split()
  n = int(n) # n is number of people
  q = int(q) # q is number of songs + qns
  g = int(g) # g is number of genres

  people_hash = {}
  
  
  for i in range(q):
    temp = []
    temp = input().split()
    
      
    if temp[0] == 'P':
      
      s = int(temp[1]) # this is genre
      p = int(temp[2]) # this are numb of people
      
      for j in range(3, 3+p):
        people_hash[temp[j]] = s
        
      
    else:
      check = int(temp[1])
      ans_temp = 0
      
      for _ in people_hash:
        if (people_hash[_] == check):
          ans_temp += 1

      ans.append(ans_temp)

for a in ans:
  print(a)
  