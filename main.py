import streamlit as st
from cryptography import encrypt, decrypt

st.set_page_config(page_title="Cryptography App", layout="centered")

st.title("Cryptography App")
st.write("Securely encrypt and decrypt messages using your custom keys.")

st.divider()

st.subheader("Encryption")

with st.container(border=True):
    encryption_key = st.text_input("Encryption Key (Has to be comma separated string of numbers)", key="encryption_key")
    message_to_encrypt = st.text_area("Message to Encrypt", key="message_to_encrypt")

    if st.button("Encrypt Message"):
        if not encryption_key or not message_to_encrypt:
            st.warning("Please provide both a key and a message.")
        else:
            encrypted_message = encrypt(message=message_to_encrypt, key=encryption_key)
            st.success("Message successfully encrypted!")
            st.write(encrypted_message)
            st.code(encrypted_message, language="plaintext")

st.divider()

st.subheader("Decryption")

with st.container(border=True):
    decryption_key = st.text_input("Decryption Key (Has to be comma separated string of numbers)", key="decryption_key")
    message_to_decrypt = st.text_area("Message to Decrypt", key="message_to_decrypt")

    if st.button("Decrypt Message"):
        if not decryption_key or not message_to_decrypt:
            st.warning("Please provide both a key and an encrypted message.")
        else:
            try:
                decrypted_message = decrypt(message=message_to_decrypt, key=decryption_key)
                st.success("Message successfully decrypted!")
                st.code(decrypted_message, language="plaintext")
            except Exception as e:
                st.error("Decryption failed. Please check your key or message.")
