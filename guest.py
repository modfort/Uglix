from client import * 

a= Connection()
a.post("/bin/login",user="guest",password="guest")
t=a.get("/home/guest/INBOX/4080")
print(t)
