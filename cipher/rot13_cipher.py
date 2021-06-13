class ROT13Cipher:
  """
  The ROT13 cipher is a substitution cipher with a specific 
  key where the letters of the alphabet are offset 13 places. 
  I.e. all 'A's are replaced with 'N's, all 'B's are replaced 
  with 'O's, and so on.
  """

  def encode(self, source_str):
    return self._transform(source_str, 13)


  def decode(self, source_str):
    return self._transform(source_str, -13)


  def _transform(self, source_str, shift_num):
    msg = list(source_str)

    for i in range(len(msg)):
      if msg[i].isupper():
        letter_index = ord(msg[i]) - ord('A')
        new_letter_index = (letter_index + shift_num) % 26
        msg[i] = chr(new_letter_index + ord('A'))

    return ''.join(msg)
    


if __name__ == '__main__':
  cipher = ROT13Cipher()

  source_message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
  print(f'Source: {source_message}')

  encoded_msg = cipher.encode(source_message)
  print(f'Encoded: {encoded_msg}')

  decoded_msg = cipher.decode(encoded_msg)
  print(f'Decoded: {decoded_msg}')
