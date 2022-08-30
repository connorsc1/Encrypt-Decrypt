def a():
  def encrypt(message, shift):
    message = message.lower()
    encryptedMessage = ""
    for x in message:
      if x in "abcdefghijklmnopqrstuvwxyz":
        num = ord(x) 
        num = num + shift
        if num > ord("z"):
          num = num - 26
        char = chr(num)
        encryptedMessage = encryptedMessage + char
      else:
        encryptedMessage = encryptedMessage + x
    return encryptedMessage
  
  shift = 3
  msg = input("Enter your message: ")
  encryptedMessage = encrypt(msg, shift)
  print("The encrypted message is: ", encryptedMessage)
  decryptedMessage = decrypt(encryptedMessage, shift)
  print("The decrypted message is: ", decryptedMessage)
def decrypt(eMessage, shift):
  new = -abs(shift)
  decryptedMessage = ""
  for x in eMessage:
    if x in "abcdefghijklmnopqrstuvwxyz":
      num = ord(x)
      num = num + new
      if num < ord("a"):
        num = num + 26
      char = chr(num)
      decryptedMessage = decryptedMessage + char
    else:
      decryptedMessage = decryptedMessage + x
  return decryptedMessage
a()