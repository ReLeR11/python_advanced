class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


SPECIAL_CHARACTERS = ["@", "*", "&", "%"]

def password_too_common(psw, specials):
    only_digits = psw.isdigit()
    only_letters = psw.isalpha()
    only_specials = all(ch in specials for ch in psw)
    return only_digits or only_letters or only_specials


while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_CHARACTERS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
