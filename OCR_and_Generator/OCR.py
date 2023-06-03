import cv2
import pytesseract
import os


def saveCharacters(text, height, width, characters, image):
    for x in range(len(text)):
        text[x] = text[x].split()

    for i in range(len(text) - 1):
        a = text[i]
        x, y, w, h = int(a[1]), int(a[2]), int(a[3]), int(a[4])
        crop = image[height - h:height - y, x:w]
        name = "OCR_and_Generator/Characters/" + a[0] + ".jpg"

        #cv2.imwrite("OCR_and_Generator/char_" + a[0] + ".jpg", crop)  # for the app

        if a[0] in characters:
            #print("Is this " + a[0].upper() + "? (Press Enter if YES.\nIf NO, type the correct letter and press ENTER\nIf unrecognizable, type a space and press ENTER): ")
            #cv2.imshow('Image', crop)
            #cv2.waitKey(0)
            #que = input()

            '''
            f = open("data.txt", "r")
            que = f.readline()
            if que == "NULL":  # correct
                cv2.imwrite(name, crop)
            elif que == "!":  # unrecognized
                pass
            else:  # update
                cv2.imwrite("OCR_and_Generator/Characters/" + que + ".jpg", crop)
            
            f.close()
            os.remove("OCR_and_Generator/data.txt")
            '''

            cv2.imwrite("OCR_and_Generator/Characters/" + a[0] + ".jpg", crop)


def run(files):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR/tesseract.exe'

    #/------------------------------------- UPPERCASE ------------------------------------
    print("a")
    image = cv2.imread("OCR_and_Generator/Images/" + files[0])
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('image', image)
    #cv2.waitKey(0)

    print("b")
    config = '--oem 3 --psm %d' % 4
    string = pytesseract.image_to_string(image, config=config, lang='eng')
    print(string)

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    height, width = image.shape
    text = pytesseract.image_to_boxes(image, config=config, lang='eng').split('\n')
    saveCharacters(text, height, width, uppercase, image)
    print("c")
    #/------------------------------------- LOWERCASE ------------------------------------

    image = cv2.imread("OCR_and_Generator/Images/" + files[1])
    image = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('image', image)
    #cv2.waitKey(0)

    config = '--oem 3 --psm %d' % 7
    string = pytesseract.image_to_string(image, config=config, lang='eng')
    print(string)

    lowercase = "abcdefghijklmnopqrstuvwxyz"

    height, width = image.shape
    text = pytesseract.image_to_boxes(image, config=config, lang='eng').split('\n')
    saveCharacters(text, height, width, lowercase, image)

    #/------------------------------------- NUMBERS ------------------------------------

    image = cv2.imread("OCR_and_Generator/Images/" + files[2])
    image = cv2.resize(image, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('image', image)
    #cv2.waitKey(0)

    config = '--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789'
    string = pytesseract.image_to_string(image, config=config, lang='eng')
    print(string)

    numbers = "0123456789"

    height, width = image.shape
    text = pytesseract.image_to_boxes(image, config=config, lang='eng').split('\n')
    saveCharacters(text, height, width, numbers, image)



if __name__ == "__main__":
    pass

