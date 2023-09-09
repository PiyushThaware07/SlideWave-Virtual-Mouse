# Imports
import cv2
import mediapipe as mp
import pyautogui


# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width , screen_height = pyautogui.size()

# click event
index_y = 0

# Capture Footage
capture = cv2.VideoCapture(0)
while True:
    _,frame = capture.read()
    # Flip frame view
    frame = cv2.flip(frame,1)
    # Getting the width of the frame
    frame_height,frame_width,_ = frame.shape
    
    
    # Detect the hand
    rbg_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands_detector.process(rbg_frame)
    hands = results.multi_hand_landmarks
    # print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)

            # Finger Action
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(x,y)
                # Thumb
                if id == 8 :
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                # Index Fingre
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = int(screen_width / frame_width * x)
                    thumb_y = int(screen_height / frame_height * y)
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print("Click")


    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1)
