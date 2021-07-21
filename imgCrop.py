# 이미지를 일괄적으로 잘라내주는 툴
# 사용법은 Usage 출력문을 참고하면 됨

import sys

try :
    if len(sys.argv) < 6:
       print("Usage: python imgCrop.py <x> <y> <w> <h> <img_file> [more img files]")

    from PIL import Image

    x = int(sys.argv[1])
    y = int(sys.argv[2])

    w = int(sys.argv[3])
    h = int(sys.argv[4])

    area = (x, y, x + w, y + h)
    
    for i in range(5, len(sys.argv)):
        im = Image.open(sys.argv[i])

        print(i - 4, ": ", sep='', end='')
        if w == 0:
            print("Error occured: width must be greater than 0.")
            continue
        elif (h == 0):
            print("Error occured: height must be greater than 0.")
            continue
        elif (x + w > im.size[0]) or (y + h > im.size[1]):
            print("Error occured: specified size is outside the image.")
            continue

        im2 = im.crop(area)
        dotIdx = sys.argv[i].rfind('.')

        targetStr = sys.argv[i][:dotIdx] + '_crop' + sys.argv[i][dotIdx:len(sys.argv[i])]
        im2.save(targetStr)
        print(targetStr + " Cropped!")

    print("\tJob Finished.")
except FileNotFoundError:
    print("No such file found!")
except Exception as e:
    print(e)
