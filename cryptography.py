import string
alphabet_list = list(string.ascii_uppercase)
alphabet_dict = {letter: index for index, letter in enumerate(alphabet_list)}

def get_shifted_letter(shift_amount: int, letter: str):
    letter = letter.upper()
    return alphabet_list[(shift_amount + alphabet_dict[letter]) % len(alphabet_list)]

def parse_key(key: str) -> list[int]:
    return [int(num.strip()) for num in key.split(",")]

def encrypt(message: str, key: str) -> str:
    encryption_pattern: list[int] = parse_key(key)
    cipher_text = ""
    for i in range(len(message)):
        if message[i].upper() in alphabet_list:
            cipher_text += get_shifted_letter(encryption_pattern[i % len(encryption_pattern)],
                                              message[i])
        else:
            cipher_text += message[i]
    return cipher_text

def decrypt(message: str, key: str) -> str:
    decryption_pattern: list[int] = parse_key(key)
    decrypted_text = ""
    for i in range(len(message)):
        if message[i].upper() in alphabet_list:
            decrypted_text += get_shifted_letter(-(decryption_pattern[i % len(decryption_pattern)]), message[i])
        else:
            decrypted_text += message[i]
    return decrypted_text
def run_tests():
    print("Running Tests...")

    # Test Case 1: Identity
    m1, k1 = "HELLO", "0"
    assert encrypt(m1, k1) == "HELLO", f"Failed Case 1: Expected HELLO, got {encrypt(m1, k1)}"
    assert decrypt("HELLO", k1) == "HELLO", "Failed Case 1 Decrypt"

    # Test Case 2: Key Looping
    m2, k2 = "AAAA", "1, 2"
    expected_2 = "BCBC"
    assert encrypt(m2, k2) == expected_2, f"Failed Case 2: Expected {expected_2}, got {encrypt(m2, k2)}"
    assert decrypt(expected_2, k2) == m2, "Failed Case 2 Decrypt"

    # Test Case 3: Wrapping (Modulo)
    m3, k3 = "ZOO", "1"
    expected_3 = "APP"
    assert encrypt(m3, k3) == expected_3, f"Failed Case 3: Expected {expected_3}, got {encrypt(m3, k3)}"
    assert decrypt(expected_3, k3) == m3, "Failed Case 3 Decrypt"

    # Test Case 4: Complex Multi-digit
    m4, k4 = "HELLO", "10, 4, 24"
    expected_4 = "RIJVS"
    assert encrypt(m4, k4) == expected_4, f"Failed Case 4: Expected {expected_4}, got {encrypt(m4, k4)}"
    assert decrypt(expected_4, k4) == m4, "Failed Case 4 Decrypt"

    print("All test cases passed!")
def main():
    run_tests()


if __name__ == '__main__':
    main()