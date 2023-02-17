from cryptography.fernet import Fernet
import rsa

def AsimetricEncrypt(msg,key):
	return rsa.encrypt(msg,key)
def PublicKey(n,e):
	return rsa.PublicKey(n,e)
def PrivateKey(n,e,d,q,p):
    return rsa.PrivateKey(n, e, d, p, q)
def GenerateAsimetricKeys(size = 512,poolsize = 1)	:
	PublicKey,PrivateKey = rsa.newkeys(size,poolsize)
	return (PublicKey,PrivateKey)
def GenerateSimetricKey():
	SimetricKey = Fernet.generate_key()
	return SimetricKey
def SaveKeys(name,PublicKey,PrivateKey,dirs=""):
	open(f"{dirs}/{name}-PublicKey.pem","wb").write(PublicKey.save_pkcs1())
	open(f"{dirs}/{name}-PrivateKey.pem","wb").write(PrivateKey.save_pkcs1())
def LoadKeys(name,dirs=""):
	PrivateKey = rsa.PrivateKey.load_pkcs1(open(f"{dirs}/{name}-PrivateKey.pem","rb").read())
	PublicKey = rsa.PublicKey.load_pkcs1(open(f"{dirs}/{name}-PublicKey.pem","rb").read())
	return (PublicKey,PrivateKey)
def AsimetricDecrypt(msg,PrivateKey):
	return rsa.decrypt(msg,PrivateKey)
def SimetricEncrypt(msg:bytes,key:bytes) -> bytes:
	"""SimetricEncrypt

	Args:
		msg (str): the message to encript
		key (bytes): the key with which to encrypt the message

	Returns:
		bytes: the message encripted
	"""
	return Fernet(key).encrypt(msg)
def SimetricDecrypt(msg:bytes,key:bytes) -> bytes:
	decrypted = Fernet(key).decrypt(msg)
	return decrypted

