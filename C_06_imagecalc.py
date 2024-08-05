

def int_check(question, low):

        error = "Please enter a number that is more than or equal to {low}\n"
        while True:

            try:
                response = int(input(question))

                if response >= low:
                    return response
                else:
                    print(error)

            except ValueError:
                print(error)


def image_calc():

    width = int_check("Width: ",   1)
    height = int_check("Height: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    answer = f"Number of pixels: {width} x {height} = {num_pixels} " \
        f"\nNumber of bits: {num_pixels} x 24 = {num_bits}"

    return answer


image_ans = image_calc()
print(image_ans)
