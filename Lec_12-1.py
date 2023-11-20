# import pandas as pd

# folder = "data/"
# target = folder + "fktemp.csv"

# df = pd.read_csv(target)

# print(df.name == "김명철")

# from faker fimport Faker as fk 
# import os 

# temp = fk("ko-KR")
# print(temp.name())

# fk("ko-KR")
# with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
#     f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

# with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
#     for i in range(30) :
# 			f.write(temp.name() + "," + 
#             temp.address() + "," + 
#             temp.postcode() + "," + 
#             temp.company() + "," + 
#             temp.job() + "," + 
#             temp.phone_number() + "," + 
#             temp.email() + "," + 
#             temp.user_name() + "," + 
#             temp.ipv4_private() + "," + 
#             temp.ipv4_public() + "," + 
#             temp.catch_phrase() + "," + 
#             temp.color_name() + "\n")


# temp = df[df.color+=="Ivory"].post.code.mean()
# print(temp)



# temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
# print(temp)

# temp = df[df.company.isnull()]
# temp = df.name.empty
# print(temp)

# temp = df.company.insull()
# for el in temp :
#     if el == True :
#         print(el)
        
# temp = df.name.empty
# temp = df[df.company.isnull()][["name", "postcode"]]
# #print(temp)

temp = df(df.color == "Ivory")
# temp = df[~(df.color == "Ivory")] 
# temp = df[~(df.color == "Ivory")]["name"]
# print(temp.count())
# print(temp.color.count())
# print(temp)


# df[(df.color == "Ivory") & (df.postcode > 70000)]
# df[(df.color == "Ivory") | (df.postcode > 70000)]


# df.sort_values("postcode")
# df.sort_values("postcode", ascending=False)
# temp = df.sort_values("name", ascending=False)

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)

print(df)
print("\n==============================\n")
print(df.pivot(index="color", columns="name", values="postcode"))