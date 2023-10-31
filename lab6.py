#Juan Carlos Castaneda

#Encodes 8digit password using a 3shift
def encoder(pwd):

    encoded_pwd = ''
    for char in pwd:
        encoded_pwd += str(int(char) + 3)

    return encoded_pwd



