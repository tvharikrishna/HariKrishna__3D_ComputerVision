<p align="right">© 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻 𝗯𝘆 𝘁𝘃𝗵𝗮𝗿𝗶𝗸𝗿𝗶𝘀𝗵𝗻𝗮</p>
<p align="right">5 𝘮𝘪𝘯𝘶𝘵𝘦 𝘳𝘦𝘢𝘥 📚 </p> <br>

<!------ PROJECT TITLE ------>
<p align="center">
    <img src="readme_data/title.png" alt="Why we chose this project" width="1500"/>
</p> <br> <br>












<!------ WHAT ------>
<p align="center">
    <img src="readme_data/what.png" alt="Why we chose this project" width="600"/>
</p>

<p align="center"><h1>🎀 Essence of the Project</h1></p>
<p align='justify'>
The <strong>Stereo Semi-Global Block Matching (StereoSGBM)</strong> algorithm is a method used in computer vision for estimating the depth information from a pair of stereo images. This algorithm is an enhancement over the simpler block matching techniques (such as StereoBM) for stereo correspondence problems. The goal of StereoSGBM and similar algorithms is to reconstruct a 3D scene from two stereo images by finding the disparity (the difference in horizontal position) between corresponding points in the left and right images.
</p>

<p align="center">
  <a href="https://www.linkedin.com/feed/update/urn:li:activity:7127317220291952640?utm_source=share&utm_medium=member_desktop">
    <img src="https://img.shields.io/badge/My Project Video-Depth Estimation using StereoSGBM-blue" alt="Video" width="450" height="30"/>
  </a>
</p> <br> <br>
















<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="What the project accomplishes" width="600"/>
</p>

<h1 style="text-align: left;">🎯 Project Vision</h1>
<p style="text-align: justify;">
The project utilizes the StereoSGBM algorithm to enhance depth estimation, providing a significant improvement over traditional methods. By leveraging its accuracy and computational efficiency, the initiative aims to address challenges in 3D scene reconstruction, particularly in complex environments. This approach facilitates more reliable 3D modeling for applications in autonomous driving, robotics, and immersive experiences.
</p>

<h2 style="text-align: left;">💠 Advantages</h2>
<p style="text-align: justify;">
▸ <strong>Accuracy:</strong> StereoSGBM offers superior depth perception in complex settings, improving 3D reconstruction accuracy. <br><br>
▸ <strong>Robustness:</strong> It's more resilient against environmental variations, ensuring stable performance across conditions. <br><br>
▸ <strong>Flexibility:</strong> Adjustable parameters allow for tailored optimization, enhancing depth estimation for various applications. <br><br>
▸ <strong>Comprehensive Coverage:</strong> The algorithm effectively handles occlusions and textureless areas, providing a cohesive depth map. <br><br>
</p>

<br> <br> <br>













<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="How we implemented the project" width="600"/>
</p>

<h1 align="ledt">🪓 Project Implementation</h1>
<h2 style="text-align: left;">💠 Software Design & Tools </h2>
<p style="text-align: justify;">
The project is built on OpenCV for Python, utilizing the StereoSGBM algorithm to perform depth estimation from stereo images. This approach allows for the extraction of high-precision depth information, essential for 3D scene reconstruction. The implementation involves preprocessing the images, computing the disparity maps using StereoSGBM, and applying post-processing techniques like WLS filtering to enhance the quality of the depth maps. Python's flexibility and OpenCV's comprehensive library support the efficient development and testing of the depth estimation process.
</p>
<p>
  <!-- Windows Badge -->
  <img src="https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white" alt="Windows" style="height: 25px;"/> &nbsp;
  <!-- VS Code Badge -->
  <img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 25px;"/> &nbsp;
  <!-- Python Badge -->
  <img src="https://img.shields.io/badge/Python-FED843.svg?&style=flat-square&logo=python&logoColor=black" alt="Python" style="height: 25px;"/> &nbsp;
  <!-- OpenCV Badge -->
  <img src="https://img.shields.io/badge/OpenCV-%23white.svg?&style=flat-square&logo=opencv&logoColor=white" alt="OpenCV" style="height: 25px;"/>
</p> <br>

<!------ Deployment and Testing ------>
<h2 align="left">💠 Deployment and Testing </h2>
<p style="text-align: justify;">
▸ Deployment is streamlined through a Python script, enabling easy integration with various operating systems including Windows. The script processes stereo image pairs to generate depth maps, which can be visualized or further analyzed. <br><br>
▸ Testing involves running the script on a diverse set of stereo images to ensure accurate depth estimation across different scenarios. This includes images with varying levels of complexity, from simple objects to intricate scenes, verifying the algorithm's reliability and performance.
</p> <br>



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





