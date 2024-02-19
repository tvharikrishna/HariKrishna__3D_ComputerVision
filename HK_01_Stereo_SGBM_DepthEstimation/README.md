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
We use the StereoSGBM algorithm for depth estimation despite the availability of various methods in OpenCV due to its balance between accuracy and computational efficiency for semi-global matching. Unlike simpler algorithms like StereoBM, which only consider local information leading to less accurate depth maps, StereoSGBM incorporates semi-global constraints, significantly improving the quality of the depth estimation, especially in complex scenes with occlusions, repetitive patterns, and varying textures.
</p>

<h2 style="text-align: left;">💠 Advantages</h2>
<p style="text-align: justify;">
▸ <strong>Accuracy:</strong> StereoSGBM tends to produce more accurate and reliable depth information compared to simpler methods like StereoBM, especially in environments with repetitive patterns, occlusions, and varying textures. <br>
▸ <strong>Robustness:</strong> It is more robust to noise and lighting variations due to its semi-global optimization approach. <br>
▸ <strong>Flexibility:</strong> The algorithm offers parameters that can be tuned for different scenarios or requirements, such as the range of disparities, block size for matching, and several parameters controlling the semi-global matching process.
</p>
 
<br> <br> <br>













<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="How we implemented the project" width="600"/>
</p>

<p align="center"><h1>🪓Project Implementation</h1></p>

<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸💠💠💠💠
The project is developed using the Robot Operating System (ROS), facilitating complex simulations and trajectory analysis. The mathematical foundation and kinematic behavior of the bicycle model are visualized through Matplotlib, with Python scripting at the core of the development. RViz provides real-time visualization of the robot model and trajectory, enhancing the analysis and debugging process.
</p>
<p>
  <!-- Ubuntu Badge -->
  <img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 25px;"/> &nbsp;
  <!-- Linux Badge -->
  <img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 25px;"/> &nbsp;
  <!-- VS Code Badge -->
  <img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 25px;"/> &nbsp;
  <!-- ROS Badge -->
  <img src="https://img.shields.io/badge/ROS-22314E.svg?&style=flat-square&logo=ros&logoColor=white" alt="ROS" style="height: 25px;"/> &nbsp;
  <!-- Python Badge -->
  <img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=python&logoColor=white" alt="Python" style="height: 25px;"/> &nbsp;
  <!-- Matplotlib Badge -->
  <img src="https://img.shields.io/badge/Matplotlib-FFD43B.svg?&style=flat-square&logo=python&logoColor=blue" alt="Matplotlib" style="height: 25px;"/> &nbsp;
</p> <br>

<!------ Deployment and Testing ------>
<p align="center"><h2>💠 Deployment and Testing </h2></p>
<p align='justify'>
▸ The deployment of the Bicycle Kinematic Model was conducted within a simulated environment using ROS, ensuring a controlled testing. I deployed the model on a standard Ubuntu system, with simulations facilitated by Matplotlib for trajectory visualization. The process included continuous integration practices to check for code integrity and automated tests to validate kinematic equations against predetermined inputs.
</p>

<p align='justify'>
▸ Testing consisted of a series of controlled simulations designed to challenge the model's capabilities in trajectory planning and response. Scenarios included navigating circular paths, sharp turns, and S-shaped trajectories, each requiring precise control of steering angles and velocity. The model's performance was gauged by its ability to maintain the intended path with minimal deviation and its response time to dynamic commands.
</p> <br>

<!------ Observation 1 ------>
<p align="center">
    <img src="readme_data/project_obs_1.png" alt="Why we chose this project" width="1500"/>
</p> <br>

<!------ Observation 2 ------>
<p align="center">
    <img src="readme_data/project_obs_2.png" alt="Why we chose this project" width="1500"/>
</p> <br>

<!------ Observation 3 ------>
<p align="center">
    <img src="readme_data/project_obs_3.png" alt="Why we chose this project" width="1500"/>
</p> <br>

<!------ Result and Analysis ------>
<p align="center"><h2>💠 Results & Analysis </h2></p>

<p align='justify'>
▸ The Bicycle Kinematic Model's testing confirmed theoretical predictions with real-world behavior. Control sequences manipulated velocity and turning rate, with resulting positions and distances traveled quantifying model accuracy.
</p>

<p align='justify'>
▸ A test with <code>control sequence [1, 0.1, 5]</code> showed the model navigating from the origin to <code>(-2.5586, 5.1742)</code>, covering <code>5.77 units</code>. This aligns with predictions from kinematic equations, illustrating the model's precision.
</p>

<p align='justify'>
▸ Complex maneuvers like sharp turns and direction reversals were executed with high fidelity, as seen with sequences like <code>[1, 0.7, 7]</code> and <code>[-0.1, 0.8]</code>, validating the model's responsiveness to input variations.
</p>

<p align='justify'>
▸ The practical validation of the kinematic equations has established their high accuracy and reliability. Each computational step, from velocity computation to positional adjustments, adhered to theoretical expectations with precision. This thorough analysis has not only fortified the Bicycle Kinematic Model's theoretical foundations but has also illuminated its practical efficacy.
</p>

<!------ Observation 4 ------>
<p align="center">
    <img src="readme_data/project_obs_4.png" alt="Why we chose this project" width="1500"/>
</p> <hr>

<!------ Smile More :) ------>
<p align="center">
    <img src="readme_data/HKAD_quote.png" alt="Alt text for your image" width="1500"/>
</p>




















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





