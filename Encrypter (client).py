import socket
from decimal import Decimal 

server = socket.socket()
host = "127.0.0.1"
port = 4000

server.connect((host, port))

def gcd(a,b): 
	if b==0: 
		return a 
	else:
		return gcd(b,a%b)

# p = int(input('Enter the value of p = ')) 
p = 53
# q = int(input('Enter the value of q = ')) 
q = 59
no = int(input('Enter the value of text = ')) 
n = p*q 
t = (p-1)*(q-1) 


#generate r which is relatively prime to n to blind
for r in range(2,n):
	if gcd(r,n)== 1: 
		break

print "Random Co-prime no. (r) is: ",r

server.sendall("Okay")

resp = server.recv(1024)
resp = resp.replace("PublicKey",'')
e = int(resp)   #publicKey


#blinding
ctt = pow(r,e,n) 
blindedMsg = ctt*no

# blindedMsg now holds the blinded msg
print "Blinded Msg: ",blindedMsg
server.sendall("BlindedMsg"+str(blindedMsg))

server_string = server.recv(1024)
server_string = server_string.replace("SignedMsg",'')
signedMsg = int(server_string)
print "Signed Msg: ",signedMsg

og = pow((signedMsg/r),e,n)
print "original msg: ",og
