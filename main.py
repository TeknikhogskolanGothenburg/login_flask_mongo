from werkzeug.security import generate_password_hash, check_password_hash


def main():
    email = 'nisse@email.com'
    # Hämta användaren med denna email från databasen
    # Om vi inte hittar denna användare säg att epost eller lösenord är fel
    password = "s3cr37"
    # hashed = generate_password_hash(password)
    print(hashed)
    entered_password = 's3cr37'
    print(check_password_hash(hashed, entered_password))


if __name__ == '__main__':
    main()
