def alphabet_position(text):
    unicode_number_a = 97
    unicode_number_z = 122
    exit_list = [str(ord(letter) - unicode_number_a + 1) for letter in text.lower() if unicode_number_a <= ord(letter) <= unicode_number_z]
    return ' '.join(exit_list)
