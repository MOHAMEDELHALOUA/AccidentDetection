import cv2
import requests

# Replace this URL with your video stream URL
stream_url = "http://192.168.1.5:8081/video"

def main():
    # Open a connection to the video stream
    video_capture = cv2.VideoCapture(stream_url)
    
    if not video_capture.isOpened():
        print("Error: Unable to open video stream")
        return
    
    print("Press 'q' to quit the video display")
    
    while True:
        # Read a frame from the stream
        ret, frame = video_capture.read()
            
        if not ret:
            print("Failed to capture frame. Stream might have ended.")
            break
        img = cv2.resize(frame, (1024,712))    
        # Display the frame
        cv2.imshow("Video Stream", img)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video stream and close the OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
