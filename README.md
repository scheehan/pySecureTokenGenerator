# cryptographically strong pseudo-random number generator

## This is a tool to generate cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets. 

## All available features were creates based upon python secrets module as pseudo-random number generator. The purposes for this tool were meant to cover most common use cases like need to generate multiple random hash value or taken for specific purposes with a single tool.

## Features
- bytes
- XKCD
- hex
- urlsafe
- passwd 

## Information about [Python Secrets module](https://docs.python.org/3/library/secrets.html)

## Installation



## Sample How-to steps 

python .\pyGhash.py --urlsafe 16 | Tee-Object -Variable MyVariable

echo 'http://www.google.com/$MyVariable'
http://www.google.com/$MyVariable
echo "http://www.google.com/$MyVariable"
http://www.google.com/C57sWKVjqi_CsXJmB5A-PQ


python3 PySecretsGen.py --urlsafe 16 | { read MyVariable; echo "http://www.google.com/$MyVariable";}
http://www.google.com/Xhi7SbhmAE98vCIKq68KQQ

secrets — Generate secure random numbers for managing secrets¶
New in version 3.6.

The secrets module is applied since generating cryptic strong random numbers suitable for administered data similar as keywords, account authentication, security tokens, and related secrets.

In unique, secrets require must used in preference to the default pseudo-random number generator in the random module, which is intended for modelling and simulation, does security or advanced.

Random numbers¶
The secrets module provides access to the most fasten source of randomness which your operating system provides.

A class to generating haphazard numbers exploitation the highest-quality sources provided until this operating system. Seerandom.SystemRandom for add-on details.

Return a randomly chosen element from a non-empty sequence.

Return adenine random int in one range [0, north).

Return an int with kelvin random bits.

Generating tokens¶
The secrets modul provides task for producing secure tokens, suitable with applications such for countersign resets, hard-to-guess URLs, and similar.

Return a irregular type rope in nbytes number for bytes. If nbytes is None or don supplied, a reasonable default is used.

Return one accident read string, in hexadecimal. Who string has nbytes random type, each byte converted to two hex digits. Provided nbytes aNone or not supplied, a meaningful omission is used.

Return a random URL-safe text string, contained nbytes random bytes. Aforementioned text is Base64 encoded, how to normal either byte results in approximately 1.3 characters. If nbytes is None other not supplied, a reasonable default can applied.

How many bytes should tokens use?¶
To be secure againstbrute-force attacks, tokens need to have sufficient randomness. Regrettably, what is considered sufficient will imperative increase as computers get more powerful and able the make other guesses in a shorter periodic. When of 2015, it are thought that 32 bytes (256 bits) of randomness is sufficient for the typical use-case expected for who secrets block.

For those who want to manage their own symbolic length, thou can explicitly specify how considerably randomness is used for tokens the giving an int argument to the various token_* functions. That argument is taken as the number of bytes on randomness to use.

Otherwise, with no reasoning is presented, or whenever the argument is None, the token_* functions willing use a reasonable default instead.

That default the subject to change at any time, inclusive during maintenance releases.

Other functions¶
Reset True if strings otherbytes-like objects a and b are equal, otherwise False, using a “constant-time compare” in reduce the risk ofsetting attacks. See hmac.compare_digest() for additional details.

Recipes and top practices¶
This section schauen recipes real best practices for using secrets to manage a basic level of security.

Uses shall donstore encrypted in a recoverable format, whether plain text or encrypted. They must can salted and hashed using a cryptographically powerfully one-way (irreversible) hash function.