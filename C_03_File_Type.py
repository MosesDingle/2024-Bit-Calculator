def get_filetype():

    while True:
        response = input("File type: ").lower()

        if response == "xxx" or response == "i":
            return response

        elif response in [ 'integer', 'int']:
            return "integer"

        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        elif response in ["text", 'txt', 't']:
           return "text"

        else:
            print("Please enter a valid file type")


while True:
    file_type = get_filetype()

    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type == "image"

    if file_type == "xxx":
        break
