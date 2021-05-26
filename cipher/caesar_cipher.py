class CaesarCipher:
  """
   Caesar cipher is to replace each plaintext letter 
   with a different one a fixed number of places down the alphabet.
  """

  _alphabet = [None] * 26

  _shift = 0


  def __init__(self, shift):
    self._shift = shift

    # generate alphabet
    for i in range(26):
      self._alphabet[i] = chr(i + ord('A'))

  

alphabet = [None] * 26
for i in range(26):
  alphabet[i] = chr(i + ord('A'))


def encode(message):
  splitted_message = list(message)
  encoded_message = list(message)

  for i in range(len(splitted_message)):
    letter = splitted_message[i]
    if letter.isupper():
      actual_index = (ord(letter) - ord('A') + 3) % 26
      encoded_message[i] = alphabet[actual_index]

  return ''.join(encoded_message)


def decode(message):
  splitted_message = list(message)
  decoded_message = list(message)

  for i in range(len(splitted_message)):
    letter = splitted_message[i]
    if letter.isupper():
      actual_index = (ord(letter) - ord('A') - 3) % 26
      decoded_message[i] = alphabet[actual_index]

  return ''.join(decoded_message)




encoded = encode('THE EAGLE IS IN PLAY; MEET AT JOE S.')
decoded = decode(encoded)

print('Initial: THE EAGLE IS IN PLAY; MEET AT JOE S.')
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
