
def start_app(text):
    line1 = ["⬜️", "️⬜️", "️⬜️"]
    line2 = ["⬜️", "⬜️", "️⬜️"]
    line3 = ["⬜️️", "⬜️️", "⬜️️"]
    map = [line1, line2, line3]
    print("Hiding your treasure! X marks the spot.")
    position = input()  # Where do you want to put the treasure?
    # 🚨 Don't change the code above 👆
    # Write your code below this row 👇
    letter = position[0]
    number = int(position[1])

    letter_index = list('ABCDEFGHI')
    my_index = letter_index.index(letter)

    map[number-1][my_index] = 'X'
    print(map)

    # Write your code above this row 👆
    # 🚨 Don't change the code below 👇
    print(f"{line1}\n{line2}\n{line3}")


@report.step('REST: Confirm email')
def confirm_email(self, email: str, user_id: int) -> BaseSignUpRest:
    """
    Confirm email by request for generated link

    Hash generating and secret key taken from backend code

    :param email: email Str
    :param user_id: user id Int
    :return: SignUpRest
    """
    json = {
        'hash': str(hmac.new(b'secret', email.encode('utf-8'), sha1).hexdigest()),
    }

    self.session.post(self.verify_email_path.format(user_id), json=json)

    return self


if __name__ == '__main__':
    confirm_email()
