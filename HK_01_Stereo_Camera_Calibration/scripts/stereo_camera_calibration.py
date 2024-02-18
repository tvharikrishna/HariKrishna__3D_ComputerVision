import numpy as np
import cv2
import glob
import os

def stereo_calibration():
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # correct object points to match a 9x6 grid (adjust the size according to your chessboard)
    objp = np.zeros((6*9,3), np.float32)
    objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

    # Update the paths according to your folder structure
    paths = [
        'C:\\Users\\T V Hari Krishna\\Desktop\\Computer Vision\\Data\\image_data\\stereo_calibration_data\\left_camera\\L*.jpg',
        'C:\\Users\\T V Hari Krishna\\Desktop\\Computer Vision\\Data\\image_data\\stereo_calibration_data\\right_camera\\R*.jpg'
    ]

    # Prepare to store overall output
    overall_output_str = ""

    for path in paths:
        objpoints = [] 
        imgpoints = [] 

        images = glob.glob(path)

        for fname in images:
            image = cv2.imread(fname)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            ret, corners = cv2.findChessboardCorners(gray_image, (9, 6), None)

            if ret == True:
                objpoints.append(objp)
                corners2 = cv2.cornerSubPix(gray_image, corners, (11, 11), (-1, -1), criteria)
                imgpoints.append(corners2)
                
                # Get camera side (Left/Right) for window name
                camera_side = "Left Camera Calibration" if "left_camera" in path else "Right Camera Calibration"

                # Draw and display the corners with dynamic window name
                cv2.drawChessboardCorners(image, (9,6), corners2, ret)
                cv2.imshow(camera_side, image)
                cv2.waitKey(500)  # Increase this time or use cv2.waitKey(0) to wait for a key press
        
        cv2.destroyAllWindows()

        # Perform camera calibration to get camera matrix
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_image.shape[::-1], None, None)
        
        # Get camera side (Left/Right) for output string
        camera_side = "LEFT" if "left_camera" in path else "RIGHT"

        # Create formatted output string
        output_str = f"{camera_side} CAMERA DATA\n\n"
        output_str += f"1. ret ===>\n{ret}\n\n"
        output_str += f"2. {camera_side} Camera matrix ===>\n\nIntrinsic matrix =\n{mtx}\n"
        output_str += f"> focal length in x (fx) = {mtx[0,0]}\n"
        output_str += f"> focal length in y (fy) = {mtx[1,1]}\n"
        output_str += f"> optical center (cx) = {mtx[0,2]}\n"
        output_str += f"> optical center (cy) = {mtx[1,2]}\n\n"
        
        output_str += f"3. Distortion coefficients array ===> [k1, k2, p1, p2, k3]\n\n{dist}\n\n"
        output_str += f"a. Radial distortion coefficients ==>\n"
        output_str += f"k1 = {dist[0][0]}\n"
        output_str += f"k2 = {dist[0][1]}\n"
        output_str += f"k3 = {dist[0][4]}\n\n"
        output_str += f"b. Tangential distortion ==>\n"
        output_str += f"p1 = {dist[0][2]}\n"
        output_str += f"p2 = {dist[0][3]}\n\n"

        overall_output_str += output_str
        overall_output_str += "-------------------------------------------------------\n"

    # Save overall output to a single text file
    output_dir = "C:\\Users\\T V Hari Krishna\\Desktop\\Computer Vision\\Data\\camera_data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, "stereo_calibration_data.txt")
    with open(output_path, 'w') as f:
        f.write(overall_output_str)

if __name__ == '__main__':
    stereo_calibration()