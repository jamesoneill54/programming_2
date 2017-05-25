import sys
from string import ascii_uppercase, digits, punctuation

#cipher dict = {cipher : alphanum}

def cipher_shift(shift):
   cipher_key = {}
   alphanum = ascii_uppercase + digits
   cipher = alphanum[shift % len(alphanum):] + alphanum[:shift % len(alphanum)]
   i = 0
   while i < len(alphanum):
      cipher_key[cipher[i]] = alphanum[i]
      i += 1
   return cipher_key

def decode_text(line, shift):
   decoded = []
   for word in line:
      decoded_word = []
      for l in word:
         if l in punctuation:
            decoded_word.append(l)
            continue
         decoded_word.append(shift[l])
      decoded.append(''.join(decoded_word))
   return ' '.join(decoded)

def main():
   alphanum = ascii_uppercase + digits
   encoded_text = []
   shift = None
   for line in sys.stdin:
      encoded = line.strip().split()
      if shift == None:
         for word in encoded:
            if len(word) == 3:
               i = 0
               while i < len(alphanum) and alphanum[i] != word[0]:
                  i += 1
               shift = cipher_shift(i - 19)
               decoded_and = ''
               for l in word:
                 if l not in punctuation:
                     decoded_and += shift[l]
               if decoded_and != 'THE':
                  shift = None
                  continue
               else:
                  break
      if not shift:
         encoded_text.append(encoded)
         continue
      if encoded_text:
         for e in encoded_text:
            print (decode_text(e, shift))
         encoded_text = None
      print (decode_text(encoded, shift))


if __name__ == '__main__':
   main()