def karaca(message: str) -> str:
    def is_valid_encrypted_text(text: str) -> bool:
        """Check if the given text is a valid encrypted text."""
        return len(text) >= 3 and text.endswith("aca") and not any(c in "aeiouAEIOU" for c in text[:-3])

    # Mapping of vowels and their corresponding numbers
    vowels_mapping: Dict[str, str] = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'}

    if is_valid_encrypted_text(message):
        encrypted_text = message[:-3]
        # Reverse the vowels mapping for decryption
        reverse_vowels_mapping = {value: key for key, value in vowels_mapping.items()}
        decrypted_text = ''.join([reverse_vowels_mapping.get(char, char) for char in encrypted_text])
        return decrypted_text[::-1]
    else:
        reversed_text = message[::-1]
        encrypted_text = ''.join([vowels_mapping.get(char, char) for char in reversed_text])
        return encrypted_text + "aca"
