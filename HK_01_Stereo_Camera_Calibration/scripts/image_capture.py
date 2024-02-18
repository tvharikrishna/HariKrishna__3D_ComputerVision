import cv2
import os

def capture_image():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    # Initialize image count
    image_count = 1

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Wait for 'c' key to capture image
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Define path to save the image
            path = r"C:\Users\T V Hari Krishna\Desktop\Computer Vision\Data\image_captures\stereo_cam_captures\right_cam"
            if not os.path.exists(path):
                os.makedirs(path)
            
            # Generate filename with sequence
            filename = os.path.join(path, f"right_cam_{image_count}.jpg")

            # Save the captured image
            cv2.imwrite(filename, frame)
            print(f"Image saved: {filename}")

            # Increment image count
            image_count += 1

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_image()
