import cv2
import mediapipe as mp
import os

# مقداردهی اولیه MediaPipe برای ردیابی دست‌ها
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# تابع برای شات داون سیستم
def shutdown_system():
    print("System shutting down...")
    os.system("shutdown /s /t 1")  # برای ویندوز
    # برای لینوکس از دستور زیر استفاده کنید
    # os.system("sudo shutdown now")

# تابع برای تشخیص حالت ضربدر
def detect_cross_hands(landmarks):
    if landmarks:
        # استخراج موقعیت کف دست و نوک انگشت‌ها
        wrist = landmarks[0]
        index_finger_tip = landmarks[8]
        pinky_finger_tip = landmarks[20]

        # بررسی اینکه آیا نوک انگشتان از عرض دست مخالف عبور کرده‌اند
        if (index_finger_tip.x < wrist.x < pinky_finger_tip.x or
            pinky_finger_tip.x < wrist.x < index_finger_tip.x):
            return True
    return False

# خواندن ویدیو از وب‌کم
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # تبدیل فریم به فرمت RGB برای MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    # رسم دست‌ها
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # بررسی حالت ضربدر
            if detect_cross_hands(hand_landmarks.landmark):
                shutdown_system()
                break

    cv2.imshow('Hand Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
