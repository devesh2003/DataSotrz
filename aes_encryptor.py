from Crypto import Random
from Crypto.Cipher import AES

def pad(text):
    return (text + b'\0' * (AES.block_size - len(text) % AES.block_size))

def unpad(text):
    return text.rstrip(b'\0')

def encrypt(text,key):
    text = pad(text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(text))

def decrypt(text,key):
    pass

def main():
    text = input("Enter some text : ")
    key = input("Enter key : ")
    cipher = encrypt(text,key)

    print("The encrypted version is : %s"%(cipher))

if __name__ == '__main__':
    main()
