#!/usr/bin/env python3
# coding=utf-8

import queue

from . import robot_modules
from .logger import Logger
from .robot_connection import  RobotConnection
from .robot_msg_push import RobotMsgPush
from .robot_video_stream import RobotVideoStream


class Robot(object):
    def __init__(self, ip='192.168.2.1'):
        self.connection = RobotConnection(ip)
        self.connect = self.connection.start
        self.send_msg = self.connection.send_msg

        # modules
        self.basic_ctrl = robot_modules.BasicCtrl(self)
        self.chassis = robot_modules.Chassis(self)
        self.gimbal = robot_modules.Gimbal(self)
        self.blaster = robot_modules.Blaster(self)

        # NOTE robot_modules必须在push前申明，因为push会对modules的属性进行更新
        self.video = RobotVideoStream(self)
        self.push = RobotMsgPush(self)

        self.log = Logger('RMEP(main)')