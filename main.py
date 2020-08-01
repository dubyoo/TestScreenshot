from helper import *
import my_thread
import threading

if __name__ == '__main__':
    hwnd_list = get_window_handlers()
    dump_windows_information(hwnd_list)
    lock = threading.Lock()
    for hwnd in hwnd_list:
        # pos = (IMG_XUAN_SHANG[0], IMG_XUAN_SHANG[1])
        # pos_end = (IMG_XUAN_SHANG[2], IMG_XUAN_SHANG[3])
        # img_file = './img/OVERFLOW.bmp'
        # img_src = screen_shot(hwnd)
        # show_img(img_src)
        # maxVal, maxLoc = find_image(hwnd, img_file)
        # print(maxVal, maxLoc)
        # pass
        thread = my_thread.MyThread(hwnd, lock)
        thread.start()
