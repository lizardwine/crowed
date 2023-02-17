from misc import *
import time
import pickle
import os
import random
import getpass
import hashlib
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
def ash(stri):
    return hashlib.sha256(stri.encode('utf-8')).hexdigest()
def gen_number(Except = [34,39,92,96],fromto=[33,126]):
	r = random.randint(fromto[0],fromto[1])
	while r in Except:
		r = random.randint(fromto[0],fromto[1])
	return r

def gen_pass(length = 32,Ascii=[33,126]):
	password = ""
	for i in range(length):
		password += chr(gen_number())
	for i in range(10):
		if str(i) in password:
			break
	else:
		password += str(random.randint(0,100))
	for i in range(65,91):
		if chr(i) in password:
			break		
	else:
		password += chr(random.randint(65,90))
	for i in range(97,123):
		if chr(i) in password:
			break
	else:
		password += chr(random.randint(97,122))
	return password
def write_data(data,key):
    data = str(data).encode() + b"########"
    open(f"/home/{username}/crowed/passwords.dbc","wb").write(pickle.dumps(encript(data,key)))
def load_data(key):
	data = open(f"/home/{username}/crowed/passwords.dbc","rb").read()
	data = pickle.loads(data)
	return eval(decript(data,key))

def new_password(password,email,page,account,uname,key):
	data = load_data(key)
	if uname not in [x["uname"] for x in data]:
		data.append({"uname":uname,"page":page,"email":email,"account":account,"password":password}) 
	else:
		return f"{Fore.LIGHTYELLOW_EX}Unique name is already in use"
	write_data(data,key)
def read_register(var_name,expedcted_value ,key):
    data = load_data(key)
    result = ""
    Flag = ""
    for register in data:
        if eval(f"'{register[var_name]}' {'==' if expedcted_value != '*' else 'or'} '{expedcted_value}'"):
            result += f"=======\nUnique name: {Fore.RED}{register['uname']}{Style.RESET_ALL}\n{Fore.RESET}Page: {Fore.LIGHTYELLOW_EX}{register['page']}\n{Fore.RESET}Email: {Fore.LIGHTCYAN_EX}{register['email']}\n{Fore.RESET}Account: {Fore.LIGHTBLUE_EX}{register['account']}\n{Fore.RESET}Password: {Fore.LIGHTMAGENTA_EX}{register['password']}\n{Fore.RESET}"
            Flag = "True"
    if Flag == "True":
        return result
    elif data == []:
        return f"{Fore.LIGHTYELLOW_EX}The database is empty"
    else:
        return f"{Fore.LIGHTYELLOW_EX}no register found for {Fore.RED}{var_name.title() if not var_name == 'uname' else 'Unique name'} {Fore.LIGHTYELLOW_EX}= {Fore.LIGHTYELLOW_EX}\"{Fore.RED}{expedcted_value}{Fore.LIGHTYELLOW_EX}\""
def renew_password(uname,new_password,key):
    data = load_data(key)
    index = 0
    for register in data:
        if register["uname"] == uname:
            data[index]["password"] = new_password
            write_data(data,key)
            return f"{Fore.LIGHTGREEN_EX}Password succefully changed"
        index += 1
    else:
        return f"{Fore.LIGHTYELLOW_EX}No register found whit {Fore.RED}Unique name{Fore.LIGHTYELLOW_EX} = \"{Fore.RED}{uname}{Fore.LIGHTYELLOW_EX}\""
def delete_register(uname,key):
    data = load_data(key)
    index = 0
    for register in data:
        if register["uname"] == uname:
            data.pop(index)
            write_data(data,key)
            return f"{Fore.LIGHTGREEN_EX}Register succefully deleted"
        index += 1
    else:
        return f"{Fore.LIGHTYELLOW_EX}No register found whit {Fore.RED}Unique name{Fore.LIGHTYELLOW_EX} = \"{Fore.RED}{uname}{Fore.LIGHTYELLOW_EX}\""
def change_data(uname,var_name, new_value,key):
    data = load_data(key)
    index = 0
    for register in data:
        if register["uname"] == uname:
            data[index][var_name] = new_value
            write_data(data,key)
            return f"{Fore.LIGHTGREEN_EX}{var_name.title() if not var_name == 'uname' else 'Unique name'} succefully changed"
        index += 1
    else:
        return f"{Fore.LIGHTYELLOW_EX}No register found whit {Fore.RED}Unique name{Fore.LIGHTYELLOW_EX} = \"{Fore.RED}{uname}{Fore.LIGHTYELLOW_EX}\""
    
opc = "0"
password_hash = open(f"/home/{username}/crowed/password.txt").read()
user_password = ""
for i in range(3):
	user_password = getpass.getpass("password(hided for security): ")
	input_password_hash = ash(user_password)
	if password_hash == input_password_hash:
		opc = ""
		flag = True
		break
	print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}the password is wrong!")
else:
    print(f"{Fore.RED}{Style.BRIGHT}too many attempts!")
    flag = False
if flag:
    os.system("clear")
while not opc in ("0","exit"):
    opc = input(menu + " ")
    os.system("clear")
    print(menu,opc)
    if opc == "1":
        uname = input("Unique name: ")
        page = input("Page: ")
        account = input("Account: ")
        email = input("Email: ")
        length = input("Length(void for 32): ")
        if length == "":
            password = gen_pass(32)
        else:
            if length.isdigit():
                password = gen_pass(int(length))
            else:
                password = length
                
        
        errmsg = new_password(password,email,page,account,uname,user_password)
        if errmsg == None:
            print(f"The password is: {Fore.LIGHTMAGENTA_EX}{password}")
        else:
            print(errmsg)
            
    elif opc == "2":
        var_index = 0
        for var_name in ["uname","page","email","account"]:
            var = input(f"{var_name.title() if not var_name == 'uname' else 'Unique name'}: ")
            if var == "":
                var_index += 1 
                continue
            else:
                print(read_register(var_name,var,user_password))
                break
    elif opc == "3":
        uname = input("Unique name: ")
        length = input("Length(void for 32): ")
        length = 32 if not length.isdigit() else int(length)
        new_password = gen_pass(length)
        print(renew_password(uname,new_password,user_password))
    elif opc == "4":
        uname = input("Unique name: ")
        print(delete_register(uname,user_password))
    elif opc == "5":
        os.system("clear")
        opc2 = input("0.-Return to menu\n1.-Change password\n2.-Change unique name\n=========\n3.-Change email\n4.-Change account\n5.-Change page\n-> ")
        if opc2 == "0":
            continue
        elif opc2 == "1":
            uname = input("Unique name: ")
            new_password = input("New password: ")
            var_name = "password"
            print(change_data(uname,var_name,new_password,user_password))
        elif opc2 == "2":
            uname = input("Unique name: ")
            new_uname = input("New Unique name: ")
            var_name = "uname"
            print(change_data(uname,var_name,new_uname,user_password))
        elif opc2 == "3":
            uname = input("Unique name: ")
            new_email = input("New email: ")
            var_name = "email"
            print(change_data(uname,var_name,new_email,user_password))
        elif opc2 == "4":
            uname = input("Unique name: ")
            new_account = input("New account: ")
            var_name = "account"
            print(change_data(uname,var_name,new_account,user_password))
        elif opc2 == "5":
            uname = input("Unique name: ")
            new_page = input("New page: ")
            var_name = "page"
            print(change_data(uname,var_name,new_page,user_password))
    elif opc == "6":
        os.system("clear")
        opc2 = input("0.-Return to menu\n1.-Encript\n2.-Decript\n-> ")
        if opc2 == "0":
            continue
        elif opc2 == "1":
            file = input("file: ").replace("'","").strip()
            password = input("Password for file: ")
            data = open(file,"rb").read()
            data = encript(data,password)
            Hash = hashlib.sha256(password.encode()).hexdigest()
            data = pack(data,Hash)
            open(file,"wb").write(data)
            print(f"{Fore.LIGHTGREEN_EX}File succefully encripted")
        elif opc2 == "2":
            file = input("file: ").replace("'","").strip()
            password = input("File password: ")
            data = open(file,"rb").read()
            if data.endswith(b"encripted"):
                package = unpack(data)
                Hash = hashlib.sha256(password.encode()).hexdigest()
                if Hash == package["Hash"]:
                    data = decript(package["Data"],password)
                    open(file,"wb").write(data)
                    print(f"{Fore.LIGHTGREEN_EX}File succefully decripted")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}passwords don't match")
            else:
                print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}file aren't ecripted")
                
            
    elif opc == "0" or opc == "exit":
        os.system("clear")
    elif opc == "clear":
        os.system("clear")
    else:
        print(f"{Fore.LIGHTYELLOW_EX}Unknow option: \"{Fore.RED}{opc}{Fore.LIGHTYELLOW_EX}\"")
    """elif opc == "__RESET__":
        write_data("[       ]",user_password)"""
