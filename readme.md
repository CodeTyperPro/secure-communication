# Secure Communication Protocol Implementation using RSA and Symmetric Encryption
---
# General information

This project focuses on implementing a secure communication protocol for Teams chat. The protocol utilizes RSA encryption with a key size of 2048 bits, SHA1 for MGF hash function in RSA-OAEP, and SHA256 for HMAC hash function. RSA digital signatures employ SHA512. The protocol involves key generation, random byte generation, signature verification, master secret generation, and encryption/decryption using MiniAES and HMAC. The goal is to ensure secure and authenticated communication between client and server.

To communicate securely on Teams chat, we'll use hexadecimal string encoding for our messages. To generate true random bytes, you can use the `secrets.token_bytes()` function. We'll be using RSA encryption with a key size of 2048 bits. The MGF hash function for RSA-OAEP will be SHA1, and the HMAC hash function will be SHA256. For RSA digital signatures, we'll use the SHA512 hash function. The digital signature will fit into the RSA-OAEP-2048 payload along with the random bytes.

# Steps to perform

Here are the steps to follow:

1. Form groups of two students and decide who will be the client and who will be the server.

2. Generate RSA key pairs for both sides: `client_rsa_enc_key` and `server_rsa_enc_key` for encryption, and `client_rsa_sign_key` and `server_rsa_sign_key` for signature.

3. Generate 32 random bytes for each side: `client_public_random` and `server_public_random`.

4. The client should send the following to the server: `client_rsa_enc_key.public`, `client_rsa_sign_key.public`, and `client_public_random`.

5. The server should send the following to the client: `server_rsa_enc_key.public`, `server_rsa_sign_key.public`, and `server_public_random`.

6. Generate 48 private random bytes for each side: `client_private_random` and `server_private_random`.

7. The client signs `client_private_random` with RSA and sends it to the server using RSA-OAEP. The server decrypts the received message and verifies the signature.

8. The server signs `server_private_random` with RSA and sends it to the client using RSA-OAEP. The client decrypts the received message and verifies the signature.

9. Concatenate the private random bytes to form the `premaster_secret = client_private_random + server_private_random`.

10. Generate the master secret using `PRF(premaster_secret, "master secret", client_public_random + server_public_random)`. The master secret should be 48 bytes long.

11. Both the client and the server generate the following keys using `PRF(master_secret, "key expansion", client_public_random + server_public_random)`:
    - `client_write_mac_key`: 32 bytes
    - `server_write_mac_key`: 32 bytes
    - `client_write_key`: 2 bytes
    - `server_write_key`: 2 bytes

12. The client sends a message to the server using MiniAES encryption with `client_write_key` and HMAC with `client_write_mac_key`. The server decrypts the message and verifies the authentication code.

13. The server sends a message to the client using MiniAES encryption with `server_write_key` and HMAC with `server_write_mac_key`. The client decrypts the message and verifies the authentication code.

----

## Credits
Authors: `Alfredo Martins` & `Chen Siyu` <br>
Professor: `Ádám Zlehovszky Dr.` <br>
Place and date: `Budapest, June 2023` <br>
