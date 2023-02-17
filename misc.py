import getpass
import blowfish
import pickle

def decript(data,key):
    cipher = blowfish.Cipher(key.encode())
    data_decrypted = b"".join(cipher.decrypt_ecb_cts(data))
    return data_decrypted
    
def encript(data,key):
    cipher = blowfish.Cipher(key.encode())
    data_encrypted = b"".join(cipher.encrypt_ecb_cts(data))
    return data_encrypted
def pack(data,Hash):
    package = {"Data":data, "Hash":Hash}
    package = pickle.dumps(package) + b"\nencripted"
    return package
def unpack(package):
    package = pickle.loads(package)
    return package
    
username = getpass.getuser()

menu = """0.-Exit
1.-New Password
2.-Read Register
3.-Renew Password
===========
4.-Delete Register
5.-Change Data
6.-cryptography
->"""

#test area
if __name__ == "__main__":
    ...