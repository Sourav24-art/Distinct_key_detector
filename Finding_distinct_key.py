with open("data.txt", 'r') as msg:
  data = msg.read()

key_lst = list(data)
key_len = int(len(key_lst))

#Traditional method 

# for i in range(0,key_len):
#   if key_lst[i] == key_lst[i+1]:    
#     continue
#   elif key_lst[i] == key_lst[i+2]:
#     continue
#   elif key_lst[i] == key_lst[i+3]:
#     continue
#   else :
#     if key_lst[i+1] == key_lst[i+2]:
#       continue
#     elif key_lst[i+1] == key_lst[i+3]:
#       continue
#     else:
#       if key_lst[i+2] == key_lst[i+3]:
#         continue
#       else:
#         print(i+4)
#         break

msg_key_len = 14
total_iterations = 0
for i in range(0,msg_key_len):
  total_iterations = i + total_iterations
 

# High level method 

k = 0
j = 0
l = 0
final_count = 0
while k != total_iterations:
  for i in range(j,l+msg_key_len):
    if i == j:
      continue
    final_count +=1
    k+=1
    if key_lst[i] == key_lst[j]:
      #Reset all the values
      k = 0
      l += 1
      #because j should always be 4 values away from the l 
      j = l - 1
      break
    else: 
      continue 
  if k == total_iterations:
    print(l+14)
  j +=1

print(final_count)
print(k)
