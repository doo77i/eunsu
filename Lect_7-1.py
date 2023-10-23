#file exist 
"""import os 

fp = "temp.txt"
#fp = "temp1.txt"
if os.patg.exists(fp) :
    print("ok")
else :
    print("error")
    """
#exception  file read 
# import os 
# fp = "temp.txt"
# if os.path.exists(fp) :
#     f = open(fp, "r")
#     for line in f : 
#         print(line)
# else : 
#      f = open (fp, "w")
#      for i in range(100) :
#          f.write(str(i) + /n" )
#     # print("error")


#파일 삭제
# import os 
# fp = "new.txt"

# f = open(fp, "w")
# f.close()

# os.remove(fp)
# print("complete")

#파일 삭제
# import os
# fp = "new.txt"
# f = open(fp, "w")
# f.close()

# os.remove(fp)

# print("complete")


#파일명 변경
# import os 
# fp = "new.txt"
# f = open(fp,"w")
# f.close()
# os.rename(fp, "new1.txt")
# print("complete")


#재변경 예외처리 
# import os
# fp = "new.txt"
# tp = "new1.ttxt"

# f = open(fp, "w")
# f.close()

# if os.path.exists(tp) :
#     print("exist, same name file")
#     os.remove(tp)
# else :
#     os.rename(fp, "new1.txt")
#     print("complete")



#파일명 변경 확인 

import os
def dir_print(p) :
     files = os.listdir(p)
     for f in files :
         print(f)
fp = "new.txt"
tp = "new1.txt"
f = open(fp, "w")
f.close()
dir_print("./")
print("/n=======================================")
if os.path.exists(tp) :
    os.remove(tp)
    dir_print("./")
    print("exist, same same file")
else :
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("complete")