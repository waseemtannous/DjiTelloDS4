from pyPS4Controller.controller import Controller


# function not in use
def sendCommandToDrone(drone, left_right, for_back, up_down, yaw):
    drone.send_rc_control(left_right, for_back, up_down, yaw)


class DS4Controller(Controller):

    def __init__(self, drone, **kwargs):
        Controller.__init__(self, **kwargs)
        self.drone = drone

        # drone velocity and parameters
        self.velocity = 100
        self.left_right, self.for_back, self.up_down, self.yaw = 0, 0, 0, 0

    # yaw right
    def on_R1_press(self):
        self.yaw = 100
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # stop yaw
    def on_R1_release(self):
        self.yaw = 0
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # yaw left
    def on_L1_press(self):
        self.yaw = -100
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # stop yaw
    def on_L1_release(self):
        self.yaw = 0
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # go forward
    def on_up_arrow_press(self):
        self.for_back = self.velocity
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # go backward
    def on_down_arrow_press(self):
        self.for_back = -self.velocity
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # go left
    def on_left_arrow_press(self):
        self.left_right = -self.velocity
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # go right
    def on_right_arrow_press(self):
        self.left_right = self.velocity
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # reset forward and backward speed
    def on_up_down_arrow_release(self):
        self.for_back = 0
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # reset left and right speed
    def on_left_right_arrow_release(self):
        self.left_right = 0
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # go down
    def on_x_press(self):
        self.up_down = -self.velocity
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # reset down speed
    def on_x_release(self):
        self.up_down = 0
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # go up
    def on_triangle_press(self):
        self.up_down = self.velocity
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # reset up speed
    def on_triangle_release(self):
        self.up_down = 0
        self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)

    # drone takes off
    def on_options_press(self):
        self.drone.takeoff()

    # drone lands
    def on_share_press(self):
        self.drone.land()

    # decrease the drone's maneuvering speed
    def on_square_press(self):
        if self.velocity == 10:
            print('Speed = ', self.velocity)
            return
        self.velocity -= 10
        print('Speed = ', self.velocity)

    # increase the drone's maneuvering speed
    def on_circle_press(self):
        if self.velocity == 100:
            print('Speed = ', self.velocity)
            return
        self.velocity += 10
        print('Speed = ', self.velocity)

    # print battery percentage
    def on_playstation_button_press(self):
        print('Battery = ', self.drone.get_battery(), '%')

    def on_L3_up(self, value):
        pass

    def on_L3_down(self, value):
        pass

    def on_L3_left(self, value):
        pass

    def on_L3_right(self, value):
        pass

    def on_L3_y_at_rest(self):
        pass

    def on_L3_x_at_rest(self):
        pass

    def on_circle_release(self):
        pass

    def on_square_release(self):
        pass

    def on_L2_press(self, value):
        pass

    def on_L2_release(self):
        pass

    def on_R2_press(self, value):
        pass

    def on_R2_release(self):
        pass

    def on_L3_press(self):
        pass

    def on_L3_release(self):
        pass

    def on_R3_up(self, value):
        pass

    def on_R3_down(self, value):
        pass

    def on_R3_left(self, value):
        pass

    def on_R3_right(self, value):
        pass

    def on_R3_y_at_rest(self):
        pass

    def on_R3_x_at_rest(self):
        pass

    def on_R3_press(self):
        pass

    def on_R3_release(self):
        pass

    def on_options_release(self):
        pass

    def on_share_release(self):
        pass

    def on_playstation_button_release(self):
        pass

# def on_L3_up(self, value):
#     print("on_L3_up: {}".format(value))
#     self.flags[0] += 1
#     if self.flags[0] % 100 != 0:
#         return
#     self.for_back = VALUE
#     self.drone.send_rc_control(0, self.for_back, 0, 0)
#
# def on_L3_down(self, value):
#     print("on_L3_down: {}".format(value))
#     self.flags[1] += 1
#     if self.flags[1] % 100 != 0:
#         return
#     self.for_back = -VALUE
#     self.drone.send_rc_control(0, self.for_back, 0, 0)
#
# def on_L3_left(self, value):
#     print("on_L3_left: {}".format(value))
#     self.flags[2] += 1
#     if self.flags[2] % 100 != 0:
#         return
#     self.left_right = -VALUE
#     self.drone.send_rc_control(self.left_right, 0, 0, 0)
#
# def on_L3_right(self, value):
#     print("on_L3_right: {}".format(value))
#     self.flags[3] += 1
#     if self.flags[3] % 100 != 0:
#         return
#     self.left_right = VALUE
#     self.drone.send_rc_control(self.left_right, 0, 0, 0)
#
# def on_L3_y_at_rest(self):
#     """L3 joystick is at rest after the joystick was moved and let go off"""
#     print("on_L3_y_at_rest")
#     self.for_back = 0
#     self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)
#
# def on_L3_x_at_rest(self):
#     """L3 joystick is at rest after the joystick was moved and let go off"""
#     print("on_L3_x_at_rest")
#     self.for_back = 0
#     self.drone.send_rc_control(self.left_right, self.for_back, self.up_down, self.yaw)
