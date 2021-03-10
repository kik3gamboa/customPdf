# import libraries 
from pdfrw import PdfReader, PdfWriter   
import io 
import sys

def addMetadata(fileName, metadada):
    f = open("example/test.txt", "r")    
    metajson = f.read()    
    
    props = PdfReader(fileName)
    props.Info.poweredBy = 'RTX'
    props.Info.verifiableCredential = metajson

    PdfWriter("out/edited.pdf", trailer=props).write()

    return  ("\n\n----------------------------------------------------\n" +
            "The edited PDF is in the route: outFiles/edited.pdf\n" +
            "----------------------------------------------------\n\n")