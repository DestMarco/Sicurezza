
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
keyDER = base64.b64decode(pubkey)
seq = base64.asn1.DerSequence()
seq.decode(keyDER)
keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo

# # Generating RSA Key Pair
# # Una volta stampate, non serve più
key_pair = RSA.generate(2048)
print(key_pair.export_key())
public_key = key_pair.publickey()
print(public_key.export_key())
exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEApwN+vpTVlFF9n6r7CN7WOj26WEVXVeoeOyn5+QgEgUU/ZtBK\nzZ7xEPwrB1k5T1Wsf5Cp7s9TrZvQ5Fqm0h7pMaK73og+oNMRzfByw4YlwxlZGmtM\n1F43MnNYLJYmOVFC30Pp8IPc7iU3z8bcVuv2M5lDPt7fdYDmpwJsRwtAQAeCuMa+\nS5F80x6pG/2cjAjJHesGCWg/K7SwqwUBivbjAnqh0AKZPtCooSZBpFPui72JHrxz\nlgAZyPzM/KNgtVg31EXnUu3ZrEgMIYfQ/S+N1W5fn5FzrQtipdO90W3/vt/2jF19\nXZGh+RVwR4FV5wxNxPeD6IizcEpe/k5J7a54bwIDAQABAoIBACNTt28Ln2PImvh3\nm7MEI69dGDoMrM0VAQEFv4TgH8fSRHd0bqYwzRAJLvbWditkVWEEUhWcEDikQVrU\nG/5NIIlpwTBwhELTcqwrhLL8AKfUiEbw1GcFaMqIoGmJ9xrfp/P+8xB3a/eJstUF\n3Nyb+89tR06YqQ67Tc6c0hdy90uzk01PIL5ErJxRimppcZFZDgU6atkpQOQngtTC\n9uoQ2Is9OEN9l2K43qp2fs8vRFZRRfTUbLomx6xDdWZeAvqSB3FSdpoMxzkl5M1f\nVLHIgcAhVOoAtTtwgTZdVk3JqVym7HecJrHhZU7Gd55Eoz/bLPbKMVg3121IM0nC\nb4emjpUCgYEAwHttH0dl27iXOVmcGST7GokGpsP1sBhCYM4DVV9vXs3wtY+iMkwW\n+zYFSFOVD+glFw0FB8QLEoe88khMUHiD04JW+YB3Uiagj76DGZJASpyhedvWm2is\nIe6TIbT/8DYhU/Ie1JWZ7MY3WuyP+ys3/F13dsMASpCBUqi/aCww7mUCgYEA3iCI\nkqB1ez8JIsVY9EScLSsTqjpM/JQI39ideeIzc8SYe+5GSr48tBaTAyoOPaaREBvP\nmk9D81/PXkbEa0wcbCl9/FZGKLai0ujPXSOl366Gy67QSjvmijVAna2u9eMGZWSK\nUDZfFUVDz7PIgUGUITSxwMcR/J4pAtfGUJDkhEMCgYEAhHnupuKLFmi7nDsylpO/\nR4oby9d/V4260cm4vZ+LlWKEU1HiPl/kSU3q4Na191a9gFnzpl6liEFoKBDehVwM\nzxwcJGjott/jDkv/CzB/k1quQKKv2BJ4tnnvRfm/VWLMGWzBD2tPn4jlPG0ow6QB\nSm5B9LlNkARZHb0Kz/XqT4kCgYEAiUdEAJKIaMX5aHLc2gH5H3Uq7x6e6861eVpP\nYL9qmxaaQqVs7c6Kh6YX73GzYWiq6HC3qh9o2GWTLCnCRKnCOxqdkTDkpU7SbFST\nq3VXk1kyV3lPo0FH5oyoxYpMwgwvrMQpMw+XTfcDxL7QoQmdebQuUvz04dIBeI9Q\nMgSKJi8CgYAbVpFVcqC5b09LZ2rAu470ym3ZcqZH3JMrjBOPQfSkuPdQANxkZzKI\nb1s0CILqT9G2EhVbUBlBG2ze8P4kJILraDJK9nAU82M9B5cYLVW99+p+5Pli2bK7\nP3YmAGrgFW/FWXqp/1xSVKb+ZS6e1y68UW3WDfjxjpzbzUugUOKM1Q==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApwN+vpTVlFF9n6r7CN7W\nOj26WEVXVeoeOyn5+QgEgUU/ZtBKzZ7xEPwrB1k5T1Wsf5Cp7s9TrZvQ5Fqm0h7p\nMaK73og+oNMRzfByw4YlwxlZGmtM1F43MnNYLJYmOVFC30Pp8IPc7iU3z8bcVuv2\nM5lDPt7fdYDmpwJsRwtAQAeCuMa+S5F80x6pG/2cjAjJHesGCWg/K7SwqwUBivbj\nAnqh0AKZPtCooSZBpFPui72JHrxzlgAZyPzM/KNgtVg31EXnUu3ZrEgMIYfQ/S+N\n1W5fn5FzrQtipdO90W3/vt/2jF19XZGh+RVwR4FV5wxNxPeD6IizcEpe/k5J7a54\nbwIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")





Dc="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs08Sg3uQNoFANHIQAeUf\nHm6mGfXQhSuyBJ7bHMb94CGo5x6LFSc5WWEysrqm9MW0Wbp484kZQ+nRy4EpgoCU\ndqsLETv3Kb+LBmDqwtjForLC9SYvxGT69ZQG0Bsw1+SLSi1KikmdiyC4QdHBm8cn\nAP6MJOtuUrC9vzivK/l1NdKJpEdg416efRZMmZsjEOJerBZAo/8sy79VNjKieG6X\n1jfZNucSewr6CDgjp4hL6K+UoUubOZQA4FPL687S5gHx3PLsRAvUtBSf5ab9K/tj\n4nd7ZplA0or3zeGZvKGdt8E63W2YKQnjuwWWKhmHeNXrwsrdmDiAlkh0ZVIZihTy\nOQIDAQAB\n-----END PUBLIC KEY-----"
Dpublic_ket=RSA.import_key(Dc)
message = "lazio"
encrypted_message = encrypt_message(message, Dpublic_ket)
print("Encrypted Message:", encrypted_message)




cifrato = "E7rtg6uLBrJ5htmU2E2f+QC798Pw3ka/9hAK2UDOMuZw+hYQD0XC59dAY5dVicDOr3hmaW3Yee8lnkpcsq3f/zbb/YflFCE/mfnBckktO8xC0o9SJCK0SBAfOJPA1/OEBv2LN9rRb/zuGwJep8FGWJFgKGIgM9f9MFP8jyVw6W8mcp/83iiFf16vQ9ozQ/a68F6J7f5lDLB1mkwEzAFNMp6V2cd5rq/Ak3yEuwOoWporsz45c4TPBBluyIhn0sYa6yoDrriN3t1Oc96C1rpmjkO3fCcwwBDWwCngG6wjhIDvfAEy+Ejp+cKsv4bl5hT9WWoHILBblwDvz0fM5R3mzw=="
decifrato = decrypt_message(cifrato, key_pair)
print("Il messaggio decifrato: ", decifrato)

