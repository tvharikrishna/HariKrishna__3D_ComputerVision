<!------ PROJECT TITLE ------>
<p align="center">
    <img src="readme_data/project_title.png" alt="Why we chose this project" width="1500"/>
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
  <a href="https://www.youtube.com/watch?v=9Vck05bHM4c">
    <img src="https://img.shields.io/badge/My Project Video-SGBM Stereo Depth Estimation-blue" alt="Video" width="450" height="40"/>
  </a>
</p> <hr> <br> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="What the project accomplishes" width="600"/>
</p>

<h1 style="text-align: left;">🎯 Project Vision</h1>
<p style="text-align: justify;">
The project utilizes the StereoSGBM algorithm to enhance depth estimation, providing significant improvements over traditional methods. By leveraging its accuracy and computational efficiency, the initiative aims to address challenges in 3D scene reconstruction. StereoSGBM offers superior depth perception in complex settings, improving 3D reconstruction accuracy. It is more resilient against environmental variations, ensuring stable performance across conditions. Its adjustable parameters allow for tailored optimization, enhancing depth estimation for various applications. Additionally, the algorithm effectively handles occlusions and textureless areas, providing a cohesive depth map for reliable 3D modeling in autonomous driving, robotics, and immersive experiences.
</p> 

<hr> <br> <br>

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="How we implemented the project" width="600"/>
</p>

<h1 align="ledt">🪓 Project Implementation</h1>
<h2 style="text-align: left;">💠 Software Design & Tools </h2>
<p style="text-align: justify;">
The project is built on OpenCV for Python, utilizing the StereoSGBM algorithm to perform depth estimation from stereo images. This approach allows for the extraction of high-precision depth information, essential for 3D scene reconstruction. The implementation involves preprocessing the images, computing the disparity maps using StereoSGBM, and applying post-processing techniques like WLS filtering to enhance the quality. Python's flexibility and OpenCV's comprehensive library support the efficient development and testing of the depth estimation process.
</p>
<p>
<img src="https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white" alt="Windows" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Python-FED843.svg?&style=flat-square&logo=python&logoColor=black" alt="Python" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/OpenCV-%23white.svg?&style=flat-square&logo=opencv&logoColor=white" alt="OpenCV" style="height: 25px;"/>
</p> <br>

<!------ Technical Terms ------>
<p align="center"><h2>💠 Project Technical Terms & Concepts </h2></p>
<h3>▸ What is Depth in Computer Vision?</h3>
<p align='justify'>
In computer vision, depth refers to the distance between any point in a scene and the camera at a given position. Depth information is crucial for understanding the three-dimensional structure of the environment. It allows computer vision systems to not only detect objects but also to ascertain their size, shape, and spatial relationships with other objects in the scene.
</p> <br> 

<h3>▸ What is Stereo Vision?</h3>
<p align='justify'>
Stereo vision is a form of depth perception which, in computer vision, involves capturing two slightly offset photographs to create 3D images. The process mimics human binocular vision, where the slight differences in images seen by each eye provide the perception of depth. This technique is used extensively in applications ranging from robotic navigation to augmented reality, providing a richer perception of the environment.
</p> <br> 

<h3>▸ What is Epipolar Geometry?</h3>
<p align='justify'>
Epipolar geometry is a fundamental concept in stereo vision involving the geometric relationship between two views captured by stereo cameras. It describes the way that points from one camera view relate to lines (epilines) in the other view, constrained to lie along corresponding epilines. Understanding epipolar geometry is crucial for algorithms like StereoSGBM, as it helps to simplify the problem of finding corresponding points between the two views by reducing the search space to one dimension along these lines.
</p> <br> 

<!------ Deployment------>
<h2 align="left">💠 Deployment & Testing</h2>
<p align="center">
    <img src="readme_data/blockdiagram.png" alt="Why we chose this project" width="1500"/>
</p> 
<p style="text-align: justify;">
▸ Initialization of camera parameters, such as focal length and baseline, is crucial for achieving accurate depth estimation, setting the foundation for precise 3D scene reconstruction.<br><br>
▸ Configuration of StereoSGBM and WLS filter parameters is tailored to enhance disparity computation, with the WLS filter significantly improving the quality by reducing noise and preserving edge details, thus ensuring a more accurate depth perception.<br><br>
▸ Preprocessing involves converting input images to grayscale, enhancing the StereoSGBM algorithm's ability to compute disparities effectively, leading to more reliable depth estimation results.<br><br>
▸ Computation of the disparity map using StereoSGBM, followed by refinement with the WLS filter, showcases the algorithm's ability to generate high-quality depth maps. This process benefits from WLS filtering by achieving clearer, more detailed disparity maps, crucial for nuanced depth analysis.<br><br>
▸ Depth map extraction and normalization are performed using camera parameters, allowing for the visualization of the scene's 3D structure in a way that highlights depth variations clearly and accurately.<br><br>
▸ The option to save and display processed images facilitates the direct examination of the algorithm's output, providing a visual confirmation of the disparity and depth map quality, essential for validating the depth estimation process.
</p> <br>

<!------ Testing------>
<h2 align="left">💠 Result and Analysis </h2>
<p style="text-align: justify;">
▸ The testing phase involves running the script on a set of stereo images to evaluate the accuracy of depth estimation across various scenes. This includes examining the quality of the disparity and depth maps for consistency and detail. <br> <br>
▸ Performance and robustness are assessed by applying the algorithm to images with varying levels of complexity and texture, ensuring that the depth estimation is reliable under different conditions.
</p> <br>

<h2 align="left">💠 Input Image (data)</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="readme_data/img1.png" alt="Left Stereo Image" width="500"/><br />
      <img src="https://img.shields.io/badge/-Left%20Image-%23D00000?style=for-the-badge" alt="Left Image Badge"/>
    </td>
    <td align="center">
      <img src="readme_data/img2.png" alt="Right Stereo Image" width="500"/><br />
      <img src="https://img.shields.io/badge/-Right%20Image-%23D00000?style=for-the-badge" alt="Right Image Badge"/>
    </td>
  </tr>
</table> <br>

<h2 align="left">💠 Output Image (generated_images)</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="readme_data/disparitymap.png" alt="Disparity Map" width="500"/><br />
      <img src="https://img.shields.io/badge/-Disparity_Map-%23000000?style=for-the-badge" alt="Disparity Map Badge"/>
    </td>
    <td align="center">
      <img src="readme_data/depthmap.png" alt="Depth Map" width="500"/><br />
      <img src="https://img.shields.io/badge/-Depth_Map-%23000000?style=for-the-badge" alt="Depth Map Badge"/>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <img src="readme_data/depthmap_color.png" alt="Depth Map Color" width="500"/><br />
      <img src="https://img.shields.io/badge/-Depth_Map_Color-%23000000?style=for-the-badge" alt="Depth Map Color Badge"/>
    </td>
  </tr>
</table> <br>

<!------ HOW TO USE MY CODE ------>
<h2 align="left">💠 How to use my code?</h2>
<p>The provided Python script leverages the StereoSGBM algorithm for advanced, sophisticated depth estimation from stereo images. To effectively utilize this powerful code and explore its full potential, follow these outlined steps carefully.</p>
<ol>
  <li>Ensure OpenCV and NumPy are installed in your Python environment for image processing and numerical operations.</li>
  <li>Clone the repository to access the Python script.</li>
  <li>Navigate to and open <code>SGBM_Stereo_DepthEstimation.py</code> in your preferred code editor.</li>
  <li>Configure <code>Left_Image_Path</code> and <code>Right_Image_Path</code> within the script to point to your specific stereo image pair.</li>
  <li>Adjust StereoSGBM and WLS filter parameters as needed to optimize disparity map quality for your images.</li>
  <li>Execute the script to generate and optionally save or display the disparity map and depth map, exploring the 3D structure of the scene.</li>
</ol>

<p>This procedure enables you to harness the script for precise 3D scene reconstruction using stereo image pairs, showcasing the depth estimation capabilities of the StereoSGBM algorithm enhanced by WLS filtering.</p> <hr> <br> <br>

<!------ END ------>
<p align="center">
    <img src="readme_data/HKCV_quote.png" alt="quote" width="1500"/>
</p>
