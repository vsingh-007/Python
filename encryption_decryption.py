#-------------------------------------------------------------------------------
#Encryptioon
#-------------------------------------------------------------------------------
#import string
#def encrypt(text,key):
#    
#    encrypted = list(range(len(text)))
#    alphabet = string.ascii_lowercase
#    
#    f_half = alphabet[:key]
#    s_half = alphabet[key:]
#    
#    shifted_alphabet = s_half+f_half
#    
#    for i,latter in enumerate(text.lower()):
#        if latter in alphabet:
#            org_index = alphabet.index(latter)
#            new_latter = shifted_alphabet[org_index]
#            encrypted[i] = new_latter
#        else:
#            encrypted[i] = latter
#    return ''.join(encrypted)
#
#message = encrypt('Hello agent welcome',3)
#print(message)

#-------------------------------------------------------------------------------
#Decryption
#-------------------------------------------------------------------------------
#import string
#def decrypt(text,key):
#    
#    decrypted = list(range(len(text)))
#    alphabet = string.ascii_lowercase
#    
#    f_half = alphabet[:key]
#    s_half = alphabet[key:]
#    
#    shifted_alphabet = s_half+f_half
#    
#    for i,latter in enumerate(text.lower()):
#        if latter in alphabet:
#            index = shifted_alphabet.index(latter)
#            org_latter = alphabet[index]
#            decrypted[i] = org_latter
#        else:
#            decrypted[i] = latter
#    return ''.join(decrypted)
#
#message = decrypt('khoor ylslq vlqjk',3)
#print(message)