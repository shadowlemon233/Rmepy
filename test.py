import rmepy
from time import sleep

rm = rmepy.Robot(ip='127.0.0.1')
rm.connect()
rm.push.start()
# rm.video.start()
rm.basic_ctrl.enter_sdk_mode()
rm.basic_ctrl.set_robot_mode(2)
rm.chassis.set_vel(0.0, 1.0, 10.0)
sleep(100)
# rm.chassis.set_vel(0.0, 0.0, 0.0)
# print(rm.chassis.get_postion())
# print(rm.chassis.get_all_speed())

# rm.push.start()
# rm.gimbal.set_push(atti_freq=5)
# sleep(0.5)
# while 1:
#     print(rm.gimbal.pitch, rm.gimbal.yaw)
#     print(rm.chassis.pitch, rm.chassis.roll, rm.chassis.yaw)
#     sleep(1)

# sleep(1)
# rm.video.display()