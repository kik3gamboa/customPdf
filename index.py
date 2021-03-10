from decodeQR import getVerifiableCredential
from setCustomProperties import addMetadata

end = 0
while end < 1:
    print('Hi, please type your option: \n\n' +
        '  a). Get Verificable Credential from PDF \n' +
        '  b). Add metadata to one PDF \n'+
        '  c). Finish \n')
    
    op = str(input())
    if op == "a":
        print('Please type the route PDF file to get Verificable Credential (example/test.pdf)')
        pdf = str(input())
        print("Verifiable Credential: ", getVerifiableCredential(pdf))
    if op == "b":
        print('Please type the route PDF file to add metadata (example/test.pdf)')
        pdf = str(input())
        print('Please type the metadata to add (example/test.txt)')
        metadata = str(input())
        print(addMetadata(pdf, metadata))
    if op == "c":        
        print('Good bye....')
        end = 1