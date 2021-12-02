# 첫 번째로 제공한 이미지를 두 번째 이미지 위에 쌓아 합치는 툴

from PIL import Image
from datetime import datetime
import sys

try:
    if len(sys.argv) != 3:
        print('Usage: python imgMerge.py <imgfile1> <imgfile2>')
    else:
        image1 = Image.open(sys.argv[1])
        image2 = Image.open(sys.argv[2])

        image1_size = image1.size
        image2_size = image2.size

        width = image1_size[0] if (image1_size[0] >= image2_size[0]) else image2_size[0]
        height = image1_size[1] + image2_size[1]

        new_image = Image.new('RGB', (width, height), (0, 0, 0))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (0, image1_size[1]))

        t = datetime.now()
        new_image.save('merged_image_' + str(t.month) + str(t.day).zfill(2) +
                       str(t.hour) + str(t.minute) + str(t.second) + '.jpg', 'JPEG')
        print('Merge complete!')

except FileNotFoundError:
    print('No such file found!')
except Exception as e:
    print(e)
