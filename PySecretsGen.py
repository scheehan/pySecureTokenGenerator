import secrets, sys, zipfile, string, io

# variable for alphanumatic and special symbol characters with whitespace
alphabet = string.printable             # combination of digits, ascii_letters, punctuation, and whitespace
nospace_alpha = alphabet.strip()        # remove/strip whitespace
spcchar = string.punctuation            # String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~. without whitespace

# list variable for comparison with respective data type digit and string digit
str_base_4 = ['16', '32', '64']
str_num = ['4', '5', '6', '7', '8', '9', '10', '11', '12']
str_range = ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

DEFAULT_ENTROPY = 32  # number of bytes to return by default if no input provided

# generate an XKCD-style passphrase based upon a simple american dict compressed file
def xkcd(exrp):
    # locate compressed dict file, and uncompress zip file with read mode
    with zipfile.ZipFile('american-english.zip', mode='r') as myzip:
        # access uncompressed file with read mode 
        with myzip.open('american-english', mode='r') as f:
            # convert byte object into TextIOWrapper with encoding cp1252, and remove/strip whitespace
            words = [word.strip() for word in io.TextIOWrapper(f, encoding='cp1252')]
            # use secrets module choice func to choice words (join words without whitespace) from uncompressed file content loop cycle based on input value exrp
            password = ''.join(secrets.choice(words) for i in range(exrp))
    return password 

# generate a random text string, in hexadecimal. The string has nbytes random bytes, each byte converted to two hex digits.
def hex(exrp):
    return secrets.token_hex(exrp)

# generate a random URL-safe text string, containing nbytes random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
def urlsafe(exrp):
    return secrets.token_urlsafe(exrp)

# generate a random byte string containing nbytes number of bytes. 
def bytes(exrp):
    return secrets.token_bytes(exrp)

# generate a random alphanumeric string with special symbol characters without whitespace. 
# at least one lowercase character, at least one uppercase character, at least one special symbol character and at least three digits
def passwd(exrp):
    while True:
        password = ''.join(secrets.choice(nospace_alpha) for i in range(exrp))
        if (any(j.islower() for j in password)
            and any(j.isupper() for j in password)
            and any(j in spcchar for j in password)
            and sum(j.isdigit() for j in password) >= 3):
            break
    return password


def main():
    
    # define args argument variable to capture input sliding start index 1 and after 
    args = sys.argv[1:]
    
    # check augs input if is empty; return msg
    if not args:
        print('default value will be use if no value provided')
        print('usage: [--xkcd 4][--hex 32][--urlsafe 32][--byte 32][--passwd 9]')
        sys.exit(1)

    # check args if match condition
    if args[0] == '--xkcd':
        # check if argv len got index 1 input; it will be 3 if got input
        if len(sys.argv) > 2:
            # check if beyond covered range
            if args[1] not in str_num:
                print('''acceptable integer value is between 4 - 12''')
                sys.exit(1)
            # assign input variable and set int type
            c_xkcd = int(args[1])
            # remove index 0 - 1
            del args[0:2]
            print(xkcd(c_xkcd))
            sys.exit(1)
        else:
            # assign default value if no input
            c_xkcd = 4
            print(xkcd(c_xkcd))
            sys.exit(1)
        
    # check args if match condition
    if args[0] == '--hex':
        # check if argv len got index 1 input; it will be 3 if got input
        if len(sys.argv) > 2:
            # check if beyond covered range
            if args[1] not in str_base_4:
                print('''acceptable integer value is either 16, 32, or 64''')
                sys.exit(1)
            # assign input variable and set int type
            c_hex = int(args[1])
            # remove index 0 - 1
            del args[0:2]
            print(hex(c_hex))
            sys.exit(1)
        else:
            # assign default value if no input
            print(hex(DEFAULT_ENTROPY))
            sys.exit(1)

    # check args if match condition 
    elif args[0] == '--urlsafe':
        # check if argv len got index 1 input; it will be 3 if got input
        if len(sys.argv) > 2:
            # check if beyond covered range
            if args[1] not in str_base_4:
                print('''acceptable integer value is either 16, 32, or 64''')
                sys.exit(1)
            # assign input variable and set int type
            c_urlsafe = int(args[1])
            # remove index 0 - 1
            del args[0:2]
            print(urlsafe(c_urlsafe))
            sys.exit(1)
        else:
            # assign default value if no input
            print(urlsafe(DEFAULT_ENTROPY))
            sys.exit(1)

    # check args if match condition 
    elif args[0] == '--bytes':
        # check if argv len got index 1 input; it will be 3 if got input
        if len(sys.argv) > 2:
            # check if beyond covered range
            if args[1] not in str_base_4:
                print('''acceptable integer value is either 16, 32, or 64''')
                sys.exit(1)
            # assign input variable and set int type
            c_byte = int(args[1])
            # remove index 0 - 1
            del args[0:2]
            print(bytes(c_byte))
            sys.exit(1)
        else:
            # assign default value if no input
            print(bytes(DEFAULT_ENTROPY))
            sys.exit(1)
    
    # check args if match condition         
    elif args[0] == '--passwd':
        # check if argv len got index 1 input; it will be 3 if got input
        if len(sys.argv) > 2:
            # check if beyond covered range
            if args[1] not in str_range:
                print('''acceptable integer value is between 9 - 24''')
                sys.exit(1)
            # assign input variable and set int type
            c_passwd = int(args[1])
            # remove index 0 - 1
            del args[0:2]
            print(passwd(c_passwd))
            sys.exit(1)
        else:
            # assign default value if no input
            c_passwd = 9
            print(passwd(c_passwd))
            sys.exit(1)
    
    else:
        # if doesn't match any expected augs; return msg and exit
        print('default value will be use if no value provided')
        print('usage: [--xkcd 4][--hex 32][--urlsafe 32][--byte 32][--passwd 9]')
        sys.exit(1)
    

if __name__ == "__main__":
  main()