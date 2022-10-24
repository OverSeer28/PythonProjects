

# import string


# # The message to be encoded shifts by 23 to the right, while the word to be decoded shifts by 23 to the left.
# shift = 23

# print(' Decoding Program '.center(40, '*'))




# message = input('Enter the Message: ')
# print("\n Message Received\n")




# def decode_message(message, shifts):
#     """This decodes a message using Caesar cipher"""

#     # Variable for storing the decoded message.
#     decoded_message = ''

#     for i in message:

#         # Check for space and tab
#         if ord(i) == 32 or ord(i) == 9:
#             shifted_message = ord(i)

#         # Check for punctuations
#         elif i in string.punctuation:
#             shifted_message = ord(i)

#         # Check if the character is lowercase or uppercase
#         elif i.islower():
#             shifted_message = ord(i) - shifts

#             # If the char is less 122, we get difference subtract from 123 (the character after z)
#             if shifted_message < 97:
#                 shifted_message = (shifted_message - 97) + 123

#         else:
#             shifted_message = ord(i) - shifts

#             # If the char is less 65, we get difference and subtract from 91 (the character after Z)
#             if shifted_message < 65:
#                 shifted_message = (shifted_message - 65) + 91

#         decoded_message = decoded_message + chr(shifted_message)

#     print('Message:', message.upper())
#     print('Decoded Message:', decoded_message.upper(),"\n")



    


# decode_message(message, shift)


print(min(max(False, -1, -4), 2, 7))