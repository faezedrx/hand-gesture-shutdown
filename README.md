# Hand Gesture Shutdown System

This project detects hand gestures, specifically a "cross-hands" gesture, using **OpenCV** and **MediaPipe**. When the system detects this gesture, it automatically shuts down the computer.

## Features
- Uses the **MediaPipe Hands** model to track hand landmarks in real-time.
- Detects when hands are crossed (i.e., fingers cross the wrist).
- Shuts down the system when the cross-hands gesture is recognized.
- Works with a live webcam feed.

## How It Works
1. Captures video feed using your webcam.
2. Uses **MediaPipe Hands** to detect and track hand landmarks.
3. Detects if the hands are crossed (based on the position of the wrist and fingertips).
4. If the hands are crossed, the system shuts down immediately.

### Shutdown Command:
- **Windows**: The system uses the `os.system("shutdown /s /t 1")` command.
- **Linux**: The command `os.system("sudo shutdown now")` is commented but can be used by uncommenting for Linux systems.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/faezedrx/hand-gesture-shutdown.git
   cd hand-gesture-shutdown
   ```
2. Install the required dependencies:
  ```bash
  pip install opencv-python mediapipe
  ```

## Usage
1. Run the Python script:
   
  ```bash
  python hand_shutdown.py
  ```
2. The webcam feed will open. Show your hands to the camera.
3. When the hands are crossed, the system will automatically shut down.
   
**Press q to exit the program manually without shutting down the system.**

## Requirements
- Python 3.x
- OpenCV
- MediaPipe

## Notes
- Make sure you have the necessary permissions for shutting down the system, especially on Linux systems where `sudo` is required.
- Adjust the webcam angle for better hand gesture detection if needed.

## Future Improvements
- Add more hand gestures for different actions.
- Implement a confirmation dialog before shutdown.
- Improve gesture detection accuracy.

