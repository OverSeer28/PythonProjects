import pikepdf
from tqdm import tqdm


a = True
x = 548213



while a:
    try:
        # open PDF file
        with pikepdf.open("account.pdf", password= str(x)) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", x)
            a = False
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        print(x)
        x += 1
        continue