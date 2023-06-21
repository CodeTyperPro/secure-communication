server = Server()
client = Client()

server_rsa_enc_key, server_rsa_sign_key = server.generate_keys_server_side()
client_rsa_enc_key, client_rsa_sign_key = client.generate_keys_client_side()

server_public_random = server.generate_public_random_32_bytes()
client_public_random = client.generate_public_random_32_bytes()

server.generate_private_random_48_bytes()
client.generate_private_random_48_bytes()

encrypted_signature_chunk_server = server.sign_and_send(client_rsa_enc_key.publickey())
encrypted_signature_chunk_client = client.sign_and_send(server_rsa_enc_key.publickey()) # server_rsa_enc_key

print("Client chunk: ", encrypted_signature_chunk_server)
print("Server chunk: ", encrypted_signature_chunk_client)

print("", end="\n")
print("", end="\n")

server.receive_signature_from_client_and_verify(encrypted_signature_chunk_client, client_rsa_sign_key.publickey())
client.receive_signature_from_server_and_verify(encrypted_signature_chunk_server, server_rsa_sign_key.publickey()) # server_rsa_sign_key