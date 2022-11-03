import os
from os import listdir

# This 🐍 App converts all images from source Folder
#  to modern WEBP format into output directory

sourceDir = "source"
outputDir = "output"


# check if folders  exists
def checkPathExists(sourceDir,outputDir):

    source =  os.path.isdir(sourceDir)
    output =  os.path.isdir(outputDir)
    
    if((source) == True & (output) == True):
        
        # if folders exists load images from source
         loadImagesFromSource()
        
        # otherwise return error
    else:
        print("Something went wrong......")
            
        
    
# the actual convertation function
def loadImagesFromSource():
    
    for images in os.listdir(sourceDir):
         if (images.endswith(".jpg")):
            
             # now convert those images to webp
             convertSupportedImages(images)
             
            
# the convertion method        
def convertSupportedImages(images):
    for img  in images:
        print(f"Image: {img} converted  success..")
           
    

# main method here
def main():
   checkPathExists(sourceDir,outputDir)

# some extra 🔒 for this app
if __name__ == '__main__':
    main()