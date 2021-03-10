# import libraries 
import fitz 
import io 
import sys
from PIL import Image
from pyzbar.pyzbar import decode

def getVerifiableCredential(fileName):  
    
    # open the file 
    pdf_file = fitz.open(fileName) 
    idQr = 0
    verifiableCredential = '' 
    # iterate over PDF pages
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.getImageList()
        
        # Number of images found
        for image_index, img in enumerate(page.getImageList(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes        
            base_image = pdf_file.extractImage(xref)        
            image_bytes = base_image["image"]        
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))     
            width, height = image.size           
            if width >= 400 and height >= 400:            
                #for save image
                #image.save(open(f"../out/image_{idQr}.{image_ext}", "wb"))
                result = decode(image)
                x = str(result).split(f"Decoded(data=b'[{idQr}/3]:")
                y = x[1].split("'")
                verifiableCredential += y[0]
                idQr += 1

        #Return verifiableCredential
        return  (f"\n\n--------------------------------------------------------------------------------------------------------\n" +
                verifiableCredential + "\n"+
                "--------------------------------------------------------------------------------------------------------\n\n")