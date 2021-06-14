class AffineCipher:
  """
  The Affine cipher is a special case of the more 
  general monoalphabetic substitution cipher.

  The 'key' for the Affine cipher consists of 2 numbers, we'll call them a and b. 

  Source: http://practicalcryptography.com/ciphers/classical-era/affine/
  """

  _encoder = ''
  _decoder = ''


  def __init__(self, a, b):
    encoder = [None] * 26
    decoder = [None] * 26

    for i in range(26):
      # (ax + b) % 26
      encode_letter_index = (a * i + b) % 26
      # a(-1) * (x - b) % 26
      decode_letter_index = pow(a, -1, 26) * (i - b) % 26
      # convert index to letter
      encoder[i] = chr(ord('A') + encode_letter_index)
      decoder[i] = chr(ord('A') + decode_letter_index)
    
    self._encoder = ''.join(encoder)
    self._decoder = ''.join(decoder)

  
  def encode(self, source_msg):
    return self._transform(source_msg, self._encoder)


  def decode(self, source_msg):
    return self._transform(source_msg, self._decoder)


  def _transform(self, source_msg, coder):
    msg = list(source_msg)
    for i in range(len(msg)):
      if msg[i].isupper():
        letter_index = ord(msg[i]) - ord('A')
        msg[i] = coder[letter_index]
    return ''.join(msg)




if __name__ == '__main__':
  cipher = AffineCipher(5, 7)

  source_message = 'ATTACK AT DAWN'
  print(f'Source: {source_message}')

  encoded_message = cipher.encode(source_message)
  print(f'Encoded: {encoded_message}')

  decoded_message = cipher.decode(encoded_message)
  print(f'Decoded: {decoded_message}')
