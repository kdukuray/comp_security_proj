# Polyalphabetic Encryption & Decryption Tool

A Python-based application for encrypting and decrypting messages using a sequence of monoalphabetic ciphers (Vigenère/Shift). This project is built using **Streamlit** for the web interface.

## 👥 The Team

  * **Ivan Chen**
  * **Kalelo Dukuray**
  * **Lin Finnegan**
  * **Meherap Hossain**

-----

## 🚀 Installation & Usage

First, clone the repository to your local machine:

```bash
git clone https://github.com/kdukuray/comp_security_proj.git
cd comp_security_proj
```

### Option 1: Using `uv` (Recommended)

If you have `uv` installed, this is the fastest way to run the app. If you do not have `uv`, you can find the [installation documentation here](https://docs.astral.sh/uv/getting-started/installation/).

Run the following command in the project root:

```bash
uv run streamlit run main.py
```

### Option 2: Standard Python Virtual Environment

If you prefer using standard Python tools, follow these steps (instructions for macOS/Linux):

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2.  **Activate the environment:**

    ```bash
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    streamlit run main.py
    ```

-----

## 💻 How to Use

Once the command runs, a new tab will automatically open in your default web browser. The interface is divided into two main sections:

1.  **Encryption:** Enter your plaintext message and your numeric key sequence (comma separated) to generate ciphertext.
2.  **Decryption:** Enter the ciphertext and the numeric key sequence (comma separated) to retrieve the original message.

Example of Message: 
```
I Love Cyber Security
```
Example of Key Sequence (Comma Separated Numbers):
```
1, 14, 5
```