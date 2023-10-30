
def encoder(pwd):

    encoded_pwd = ''
    for char in pwd:
        encoded_pwd += str(int(char) + 3)

    return encoded_pwd




if __name__ == "__main__":
    encoder()