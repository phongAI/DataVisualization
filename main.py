import matplotlib.pyplot as plt
import os
threshold = 0.8
dataFolder = "../Dataset/PetImages"
#imgFormat = ['.bmp','.jpg','.jpeg','.png','.bmp']

def getNumsPerClass(folderPath):
    if os.path.exists(folderPath):
        classNames = []
        samples = []
        """Add class to classNames"""
        for subFolder in sorted(os.listdir(folderPath)):
            subFolderPath = os.path.join(folderPath,subFolder)
            if os.path.isdir(subFolderPath):
                classNames.append(subFolder)

        """Add amount of data to array"""
        for className in classNames:
            classPath = os.path.join(folderPath,className)
            samples.append(len(os.listdir(classPath)))

        """Check data imbalanced"""
        maxVolume = max(samples)
        for (className,sampleClass) in zip(classNames,samples):
            if sampleClass < int(threshold*maxVolume):
                print(f"Class:{className} with {sampleClass} images is imbalanced!")

        return classNames,samples
    else:
        raise Exception("Folder is not existed!")

def main():
    """Get class information"""
    className,samples = getNumsPerClass(dataFolder)

    if len(className)>0:
        """Visualize data"""
        plt.barh(className,samples)
        #Show total image per bar
        for index, value in enumerate(samples):
            plt.text(value, index,str(value))

        #Show label
        plt.title("Images per class")
        plt.xlabel("Class Name")
        plt.ylabel("Total Images")
        plt.show()



if __name__ == "__main__":
    main()