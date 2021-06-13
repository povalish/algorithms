class CaesarCipher:
  """
   Caesar cipher is to replace each plaintext letter 
   with a different one a fixed number of places down the alphabet.
  """

  _encode_str = ''
  _decode_str = ''


  def __init__(self, shift):
    encoder = [None] * 26
    decoder = [None] * 26
    # generate encoder/decoder alphabet
    for i in range(26):
      encoder[i] = chr(ord('A') + (i + shift) % 26)
      decoder[i] = chr(ord('A') + (i - shift) % 26)

    self._encode_str = ''.join(encoder)
    self._decode_str = ''.join(decoder)


  def encode(self, source_msg):
    """Encrupt message"""
    return self._transform(source_msg, self._encode_str)


  def decode(self, source_msg):
    """Decript message"""
    return self._transform(source_msg, self._decode_str)


  def _transform(self, source_msg, coder):
    msg = list(source_msg)
    for i in range(len(msg)):
      if msg[i].isupper():
        # get index of default string letter
        j = ord(msg[i]) - ord('A')
        msg[i] = coder[j]
    return ''.join(msg)
    

if __name__ == '__main__':
  cipher = CaesarCipher(3)
  
  source_message = 'THE EAGLE IS IN PLAY; MEET AT JOE S.'
  print(f'Sourc message: {source_message}')

  encoded_message = cipher.encode(source_message)
  print(f'Encoded message: {encoded_message}')

  decoded_message = cipher.decode(encoded_message)
  print(f'Decoded message: {decoded_message}')

