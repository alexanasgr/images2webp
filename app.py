import os.path

# This App converts all images from source Folder
#  to modern WEBP format into output directory

thefolders = ["source","output"]


# check if folders  exists
def checkPathExists(folders):
    
    for folder in folders:
        if(os.path.isdir(folder)):
            convertImages()
     
# the actual convertation function
def convertImages():
    print("Now converting images.....")    

# main method here
def main():
   checkPathExists(thefolders)

# some extra 🔒 for this app
if __name__ == '__main__':
    main()