from djitellopy import Tello
from Controller import DS4Controller
import cv2 as cv
import threading


def getDroneStream(drone):
    while True:
        img = drone.get_frame_read().frame
        img = cv.resize(img, (360, 240))
        cv.imshow("Drone Camera", img)
        cv.waitKey(1)


if __name__ == '__main__':
    # connect to drone
    drone = Tello()
    drone.connect()
    print('Battery = ', drone.get_battery(), '%')

    # reset all parameters and speed
    drone.for_back_velocity = 0
    drone.left_right_velocity = 0
    drone.up_down_velocity = 0
    drone.yaw_velocity = 0
    drone.speed = 0

    # start video stream
    drone.streamoff()
    drone.streamon()

    # show stream
    streamThread = threading.Thread(target=getDroneStream, args=(drone,))
    streamThread.start()

    # connect to controller
    controller = DS4Controller(drone, interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=60)
