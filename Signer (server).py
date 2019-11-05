import socket
from decimal import Decimal 

#Declartion
mysocket = socket.socket()
host = "127.0.0.1"
port = 4000

#Prevent socket.error: [Errno 98] Address already in use
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mysocket.bind((host, port))

mysocket.listen(5)

c, addr = mysocket.accept()

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 

# p = int(input('Enter the value of p = ')) 
p = 53
# q = int(input('Enter the value of q = ')) 
q = 59
# no = int(input('Enter the value of text = ')) 
n = p*q 
t = (p-1)*(q-1)

#calculating e which is public key
for e in range(2,t): 
	if gcd(e,t)== 1: 
		break
print "Public Key (e,n): (",e,',',n,')'

#calculating d which is private key
for i in range(1,10):
	x = 1 + i*t
	if x % e == 0:
		d = int(x/e)
		break
print "Private Key (d,n): (",d,',',n,')'

#Wait for 'Okay'
data = c.recv(1024)
if (data == "Okay"):
    c.send("PublicKey"+str(e))

#wait until data is received
data = c.recv(1024)
data = data.replace("BlindedMsg",'')
print "Blinded message: ",data
blindedMsg = int(data)
# break

signedMsg = pow(blindedMsg,d,n)
print "Signed Msg: ",signedMsg
c.send("SignedMsg"+str(signedMsg))
c.close()
