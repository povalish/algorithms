class AtbashCipher: 
  """
  The Atbash cipher is a substitution cipher with a specific key 
  where the letters of the alphabet are reversed. 
  I.e. all 'A's are replaced with 'Z's, all 'B's are replaced with 'Y's, and so on.

  Message: ATTACK AT DAWN
  Encoded: ZGGZXP ZG WZDM

  Source: http://practicalcryptography.com/ciphers/classical-era/atbash-cipher/
  """

  # English alphabet
  _alphabet_length = 26
  _source_alphabet = [None] * 26


  def __init__(self):
    # generate alphabet
    for i in range(self._alphabet_length):
      # from A to Z (A - 0, Z - 26)
      self._source_alphabet[i] = chr(i + ord('A'))


  def encode(self, message):
    return ''.join(self._reverse_message(message))


  def decode(self, message):
    return ''.join(self._reverse_message(message))


  def _reverse_message(self, message):
    source_message = list(message)
    reversed_message = list(message)
    # iterate over source message
    # and repalce each letter with 'reversed' letter
    for i in range(len(source_message)):
      letter = message[i]
      # check if symbol is letter and in upper case
      if letter.isupper():
        letter_index = self._source_alphabet.index(letter)
        reversed_index = self._alphabet_length - letter_index - 1
        reversed_message[i] = self._source_alphabet[reversed_index]

    return reversed_message





chipher = AtbashCipher()

source_message = 'ATTACK AT DAWN'
encoded_message = chipher.encode(source_message)
decoded_message = chipher.decode(encoded_message)

print(f'Source message: {source_message}')
print(f'Encoded message: {encoded_message}')
print(f'Decoded message: {decoded_message}')
