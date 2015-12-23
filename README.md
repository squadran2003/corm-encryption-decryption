## Description:
   A python command line app that lets you encrypt and decrypt a file.
   

## Example:

```python

import sys

my_key = {
'a':'f','b':'g','c':'h','d':'i','e':'j','f':'a','g':'b','h':'c',
'i':'d','j':'e','k':'p','l':'q','m':'r','n':'s','o':'t','p':'k',
'q':'l','r':'m','s':'n','t':'o','u':'z','v':'7','w':'4','x':'3',	
'y':'2','z':'u','3':'x','2':'y','4':'w', '7':'v', 
'A':'F','B':'G','C':'H','D':'I','E':'J','F':'A','G':'B','H':'C',
'I':'D','J':'E','K':'P','L':'Q','M':'R','N':'S','O':'T','P':'K',
'Q':'L','R':'M','S':'N','T':'O','U':'Z','V':'8','W':'5','X':'0',	
'Y':'1','Z':'U','0':'X','1':'Y','5':'W','8':'V'  
}


def handel_filename_input(option):
  if option.lower() == 'e':
    input_file = input("Enter the filename of the file you want to encrypt!  ")
  else:
    input_file = input("Enter the filename of the file you want to decrypt!  ")
  return input_file

def handel_filename_output(option):  
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

print("WELCOME TO MY FILE ENCRIPTION APP! ")

def main():
  while True:
    input_type=input("To encrypt a file [E] to decrypt [D]and to quit the app [Q]").lower()
    if  input_type =='q':
      break
    elif input_type =='d':
      input_file = handel_filename_input("d")
      output_file = handel_filename_output("d")
      read_write_file(input_file,output_file,'d')
      option = input("Would you like to decrypt another file [Y/n]").lower()
    else:
      input_file = handel_filename_input("e")
      output_file = handel_filename_output("e")
      read_write_file(input_file,output_file,'e')
      option = input("Would you like to encrypt another file [Y/n]").lower()
    if option !='n':
      main()
      continue
    else:
      sys.exit()
        
main()   

```

## Motivation:
  The idea for this app came from the caesar's cypher shift cryptography. So i though let me see if i can    come up with my won encryption/ decryption key.
  
## Installation:
  To use the app simply download the zip file, place the encrypt_decrypt.py file in the same directory as the file you would like to encrypt or decrypt.
  
## Contributions:
  If you would like to add some of your own mojo to the app then email me : cormackandy@hotmail.com and  twitter : cormackandy@twitter.com
  
## Licence:
The MIT License (MIT)
