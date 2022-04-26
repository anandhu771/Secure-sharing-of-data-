from pathlib import Path
from functools import partial
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import datetime


class file_rsa:
    def __init__(self):
        self.DATA_PATH = Path(__file__).parent
        print("path   :",self.DATA_PATH)
        self.BLOCK_SIZE = 64
        self.static_path=r"C:\Users\vineeth pk\PycharmProjects\userchoice\static\\"


    def encrypt(self,file,pub_key):
        """ input :
                file : """
        ext =str(file).split(".")[-1]
        print("O_ext",ext)
        dd=datetime.datetime.now()
        fl_name=str(dd.year)+"_"+str(dd.month)+"_"+str(dd.day)+"_"+str(dd.minute)+"."+ext+".rsa"
        enc_path=self.static_path+"encrypted\\doc\\"+fl_name
        in_path = self.DATA_PATH / file
        print("IN_PATH   : ",in_path)
        with open(enc_path, 'wb') as out_file:
            with in_path.open('rb') as in_file:
                cipher = PKCS1_OAEP.new(pub_key)
                print("Pub key   : ", pub_key)
                for data in iter(partial(in_file.read, self.BLOCK_SIZE), b''):
                    dt = cipher.encrypt(data)
                    out_file.write(dt)
        return fl_name


    def decrypt(self,enc_file,pri_key):
        ext = str(enc_file).split(".")[-2]
        print("E_ext", ext)
        dd = datetime.datetime.now()
        fl_name=str(dd.year)+"_"+str(dd.month)+"_"+str(dd.day)+"_"+str(dd.minute)+"."+ext
        print("ppp : ",self.DATA_PATH)
        in_path = self.static_path+"encrypted\\doc\\"+ enc_file
        print("Enc  : ",in_path)
        dec_path=self.static_path+"decrypted\\doc\\"+fl_name
        with open(dec_path, 'wb') as out_file:
            with open(in_path, 'rb') as in_file:
                cipher = PKCS1_OAEP.new(pri_key)
                print("Pri key   : ", pri_key)
                for data in iter(partial(in_file.read, self.BLOCK_SIZE * 2), b''):
                    dt = cipher.decrypt(data)
                    out_file.write(dt)
        return dec_path





class file_des:
    def __init__(self):
        self.DATA_PATH = Path(__file__).parent
        self.BLOCK_SIZE = 1024
        self.static_path=r"C:\Users\vineeth pk\PycharmProjects\userchoice\static\\"
        self.dec_path = self.static_path+"decrypted\\doc\\"
        self.enc_pth = self.static_path+"encrypted\\doc\\"

    def des_encrypt(self,in_path,key):
        ext = str(in_path).split(".")[-1]
        print("O_ext", ext)
        dd = datetime.datetime.now()
        fl_name = str(dd.year) + "_" + str(dd.month) + "_" + str(dd.day) + "_" + str(dd.minute) + "." + ext + ".des"
        self.enc_file=self.enc_pth+fl_name
        with open(self.enc_file, 'wb') as out_file:
            with open(in_path, 'rb') as in_file:
                cnt=0
                for data in iter(partial(in_file.read, self.BLOCK_SIZE), b''):
                    msg = key.encrypt(data, padding=True)
                    print(len(msg))
                    print("Encryption in stage :", cnt)
                    cnt += 1
                    out_file.write(msg)
        return fl_name

    def des_decrypt(self,enc_path,key):
        lst = str(enc_path).split(".")
        lst.pop()
        filename=".".join(lst)
        enc_file = self.static_path+"encrypted\\doc\\" + enc_path
        print("Enc  : ", enc_file)
        dec_path = self.static_path+"decrypted\\doc\\" + filename
        with open(dec_path, 'wb') as out_file:
            with open(enc_file, 'rb') as in_file:
                cnt=0
                for data in iter(partial(in_file.read, 1032), b''):
                    msg = key.decrypt(data, padding=True)
                    print("Decryption in stage :", cnt)
                    cnt += 1
                    out_file.write(msg)
        return dec_path
