# coding: utf8
import cv2 as cv

if __name__ == '__main__':
    # 替换字符列表
    ascii_char = list(r"#8XOHLTI)i=+;:,.  ")
    char_len = len(ascii_char)
    # 加载视频
    cap = cv.VideoCapture('test.mp4')
    while True:
        # 读取视频每一帧
        hasFrame, frame = cap.read()
        if not hasFrame:
            break
        # 视频长宽
        frameWidth = frame.shape[0]
        frameHeight = frame.shape[1]
        # 转灰度图
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 缩小图片并调整长宽比
        img_resize = cv.resize(img_gray, (int(frameWidth / 3), int(frameHeight / 18)))
        text = ''
        # 遍历图片中的像素
        for row in img_resize:
            for pixel in row:
                # 根据像素值，选取对应的字符
                text += ascii_char[int(pixel / 256 * char_len)]
            text += '\n'
        with open("./v-out.txt", "a") as data1:
            data1.write(text)
