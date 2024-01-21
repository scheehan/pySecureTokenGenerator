![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# Cryptographically strong pseudo-random number generator

## This is a tool to generate cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets. 

## All available features were creates based upon python secrets module as pseudo-random number generator. The purposes for this tool were meant to cover most common use cases like need to generate multiple random hash value or taken for specific purposes with a single tool.

## Features
- bytes: Generate a random byte string containing nbytes number of bytes. 
- XKCD: Generate an XKCD-style passphrase based upon a simple american dict compressed file.
- hex: Generate a random text string, in hexadecimal. 
- urlsafe: Generate a random URL-safe text string, containing nbytes random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
- passwd: Generate a random alphanumeric string with special symbol characters without whitespace. 

## Information about [Python Secrets module](https://docs.python.org/3/library/secrets.html)

## Installation
```
git clone https://github.com/scheehan/pySecureTokenGenerator
cd pySecureTokenGenerator
```

## Sample How-to steps 

### Sample acceptable argument
![powershell_ran_sample](https://github.com/scheehan/pySecureTokenGenerator/blob/master/images/ps_augs_sample.png)

### Generate random URLSafe token for one-time password recovery link ran under Windows Power Shell
```
python .\pyGhash.py --urlsafe 16 | Tee-Object -Variable MyVariable
echo 'http://www.example.com/pass-recover=$MyVariable'
```

![powershell_ran_sample](https://github.com/scheehan/pySecureTokenGenerator/blob/master/images/ps_sample.png)

### Generate random URLSafe token for one-time password recovery link ran under Linux Bash
```
# python3 PySecretsGen.py --urlsafe 16 | { read MyVariable; echo "http://www.example.com/pass-recover=$MyVariable";}
```

![bash_ran_sample](https://github.com/scheehan/pySecureTokenGenerator/blob/master/images/sh_sample.png)

### Generate a random alphanumeric string with special symbol characters without whitespace. 
![powershell_ran_passwd_sample](https://github.com/scheehan/pySecureTokenGenerator/blob/master/images/ps_passwd_sample.png)

### Generate a XKCD-style passphrase based upon a simple american dict compressed file.
![powershell_ran_xkcd_sample](https://github.com/scheehan/pySecureTokenGenerator/blob/master/images/ps_xkcd_sample.png)
