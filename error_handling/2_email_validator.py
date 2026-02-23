class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_LEN_IN_EMAIL = 5
VALID_DOMAINS = ["com", "bg", "org", "net"]

while True:
    line = input()
    if line == "End":
        break

    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")

    if len(line.split("@")[0]) < MIN_LEN_IN_EMAIL:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = line.split(".")[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
