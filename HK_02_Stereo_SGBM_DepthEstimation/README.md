# Stereo Depth Estimation using Semi-Global Block Matching (SGBM) Algorithm

<p align="center">
  <img src="project title.png" alt="StereoSGBM Example" width="1500"/>
</p>


The StereoSGBM algorithm, an advanced form of block matching, calculates disparities in stereo images more accurately and robustly than StereoBM, enabling the reconstruction of detailed 3D scenes from stereo pairs.

---------------------------------------------

## What is Stereo SGBM?
Stereo Semi-Global Block Matching (StereoSGBM) is an advanced algorithm for estimating the depth of a scene from a pair of stereo images. It calculates disparities between corresponding points to reconstruct the scene in 3D.

<p align="center">
  <img src="SGBM_BlockDiagram.png" alt="StereoSGBM Example" width="1500"/>
</p>

---------------------------------------------

## How it is better than Stereo BM?
StereoSGBM provides more accurate and detailed depth estimation compared to Stereo Block Matching (StereoBM), especially in textured and complex scenes. It implements a more sophisticated block matching technique that takes into account global image features and smoothness constraints.

---------------------------------------------

## Input Image (data)

<table>
  <tr>
    <td align="center">
      <img src="data/img1.png" alt="Left Stereo Image" width="500"/><br />
      <img src="https://img.shields.io/badge/-Left%20Image-%23D00000?style=for-the-badge" alt="Left Image Badge"/>
    </td>
    <td align="center">
      <img src="data/img2.png" alt="Right Stereo Image" width="500"/><br />
      <img src="https://img.shields.io/badge/-Right%20Image-%23D00000?style=for-the-badge" alt="Right Image Badge"/>
    </td>
  </tr>
</table>


---------------------------------------------

## Output Image (generated_images)

<table>
  <tr>
    <td align="center">
      <img src="generated_images/Disparity_Map.png" alt="Disparity Map" width="500"/><br />
      <img src="https://img.shields.io/badge/-Disparity_Map-%23000000?style=for-the-badge" alt="Disparity Map Badge"/>
    </td>
    <td align="center">
      <img src="generated_images/Depth_Map.png" alt="Depth Map" width="500"/><br />
      <img src="https://img.shields.io/badge/-Depth_Map-%23000000?style=for-the-badge" alt="Depth Map Badge"/>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2"> <!-- This will span the cell across two columns for the single wide image -->
      <img src="generated_images/Depth_Map_Color.png" alt="Depth Map Color" width="500"/><br />
      <img src="https://img.shields.io/badge/-Depth_Map_Color-%23000000?style=for-the-badge" alt="Depth Map Color Badge"/>
    </td>
  </tr>
</table>



---------------------------------------------

## How to use my code?
The provided Python script utilizes the StereoSGBM algorithm to perform depth estimation. To use this code:

1. Ensure you have OpenCV and NumPy installed in your Python environment.
2. Clone my repository.
3. Open `OpenCV_Stereo_SGBM_Depth_Estimation.py`
4. Set the `Left_Image_Path` and `Right_Image_Path` variables to point to your stereo image pair.
5. Run the script to `Save` or `Display` the generated maps.
