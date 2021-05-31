#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def listener(data):
    br = CvBridge()

    rospy.loginfo("receiving video frame")
    current_frame = br.imgmsg_to_cv2(data)
    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)

def receive_message():
    rospy.init_node('cam_sub_py', anonymous=True)
    rospy.Subscriber('video_frames', Image, listener)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
  receive_message()
