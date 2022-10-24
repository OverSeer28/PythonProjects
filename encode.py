



import string


# The message to be encoded shifts by 23 to the right,
shift = 23

print(' Encoding Program '.center(40, '*'))




message = input('Enter the Message: ')
print("\n Message Received\n")




def encode_message(message, shifts):
    """This encodes a message using Caesar cipher."""

    # Variable for storing the encoded word.
    encoded_message = ''

    for i in message:

        # Check for space and tab
        if ord(i) == 32 or ord(i) == 9:
            shifted_message = ord(i)

        # Check for punctuations
        elif i in string.punctuation:
            shifted_message = ord(i)

        # Check if the character is lowercase or uppercase
        elif i.islower():
            shifted_message = ord(i) + shifts

            # Lowercase spans from 97 to 122 (decimal) on the ASCII table
            # If the chars exceeds 122, we get the number it uses to exceed it and add to 96 (the character before a)
            if shifted_message > 122:
                shifted_message = (shifted_message- 122) + 96

        else:
            shifted_message = ord(i) + shifts

            # Uppercase spans from 65 to 90 (decimal) on the ASCII table
            # If the chars exceeds 90, we get the number it uses to exceed it and add to 64 (the character before A)
            if shifted_message > 90:
                shifted_message = (shifted_message - 90) + 64

        encoded_message = encoded_message + chr(shifted_message)

    print('Message:', message.upper())
    print('Encoded Message:', encoded_message.upper(),"\n")






encode_message(message, shift)