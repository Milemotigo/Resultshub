from PIL import Image

class ImageResizeMixin:
    '''serialize image to appropriate size'''
    def resizeImage(self, imagePath, width, height, saveImageTo):

        with Image.open(imagePath) as img:
            img.resize((width, height))

            img.save(saveImageTo)
