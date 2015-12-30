import sys

from key import *

# the second parameter iotype flag refers to wether Input or Output is in question
# the first argument option refers to wether the user is encrypting or decrypting a file. e = encryption d=decryption
def handel_filename_input_output(option,iotype):
  if iotype.lower()=='i':
    if option.lower() == 'e':
      input_file = input("Enter the filename of the file you want to encrypt!  ")
    else:
      input_file = input("Enter the filename of the file you want to decrypt!  ")
    return input_file
  else:
    if option.lower() == 'e':
      output_file = input("Enter the output filename which will hold the encrypted data! ")
    else:
      output_file = input("Enter the output filename which will hold the decrypted data! ")
    return output_file


def enc_decr(mystring):
  result = []
  for letter in mystring:
    if letter in my_key:
      result.append(my_key[letter])
    else:
      result.append(letter)
  return "".join(result)    
      

def read_write_file(infile,outfile,type):
  try:
    reader = open(infile,'r')
    writer = open(outfile,'w')
    for line in reader:
      try:
        my_string = enc_decr(line)
        writer.write(my_string)
        if type.lower() =='e':
          print("Your file was encrypted!")
        else:
          print("Your file was decrypted!")
      except:
        if type.lower() =='e':
          print("There was an error encrypting the file!")
        else:
          print("There was an error decrypting the file!")
    reader.close()
    writer.close()
  except:
    print("There is an issue with either the input or output file. Please check!!")

def user_option():
  return input("Would you like to decrypt another file [Y/n]").lower()
  
  
print("WELCOME TO CORM ENCRIPTION AND DECRYPTION CYPHER! ")

def main():
  while True:
    input_type=input("To encrypt a file [E] to decrypt [D] and to quit the app [Q]").lower()
    if  input_type =='q':
      break
    elif input_type =='d':
      input_file = handel_filename_input_output("d",'i')
      output_file = handel_filename_input_output("d",'o')
      read_write_file(input_file,output_file,'d')
      option=user_option()
    else:
      input_file = handel_filename_input_output("e","i")
      output_file = handel_filename_input_output("e","o")
      read_write_file(input_file,output_file,'e')
      option=user_option()
    if option !='n':
      main()
      continue
    else:
      sys.exit()
        
main()   