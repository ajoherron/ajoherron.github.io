---
title: "Predicting Sentiment of Tweet Replies"
excerpt: "For my final project in my Natural Language Processing course, I chose to reproduce a study that sought to predict the aggregate sentiment of a given tweet's replies (as positive, neutral, or negative). I used both a Bi-LSTM and a CNN model for this task. Overall, I was able to come within 2% of the top published results, with the Bi-LSTM slightly outperfomring the CNN on a hand-labeled test set. <br/>
<img src='/images/twitter_project.JPG' alt='Twitter Project' width='600' height='600'>"
collection: portfolio
---

<!-- <!DOCTYPE html> -->

<html>
<head>
  <style>
    .click-to-zoom {
      position: relative;
      width: 1000px; /* Set the initial width */
      transition: width 0.3s ease;
      cursor: pointer;
    }

    .click-to-zoom img {
      width: 100%;
      height: auto;
    }
  </style>
</head>
<body>

<div class="click-to-zoom" onclick="toggleZoom(this)">
  <img src="{{ "/images/Group_10_Capstone_Poster.jpg" | relative_url }}" alt="Capstone Project Poster">
</div>

<script>
  function toggleZoom(element) {
    if (element.style.width === '100%') {
      element.style.width = '1500px'; /* Set the expanded width */
    } else {
      element.style.width = '100%';
    }
  }
</script>

</body>
</html>


<!-- <style>
  .zoom-container {
    overflow: hidden;
    width: 1000px; /* Set the width of the zoom container */
    height: 1000px; /* Set the height of the zoom container */
  }

  .zoom-image {
    width: 100%;
    height: 100%;
    transition: transform 0.3s;
  }

  .zoom-container:hover .zoom-image {
    transform: scale(1.5); /* Zoom in by 50% on hover */
    transform-origin: center center; /* Zoom from the center */
  }
</style>

<script>
  const container = document.querySelector('.zoom-container');
  const image = document.querySelector('.zoom-image');

  container.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const offsetX = e.clientX - rect.left;
    const offsetY = e.clientY - rect.top;
    const percentX = offsetX / container.offsetWidth;
    const percentY = offsetY / container.offsetHeight;
    
    image.style.transformOrigin = `${percentX * 100}% ${percentY * 100}%`;
  });
</script>


<div class="zoom-container">
  <img src="{{ "/images/Group_10_Capstone_Poster.jpg" | relative_url }}" alt="Capstone Project Poster" class="zoom-image">
</div> -->

<!-- Zoomed image

<style>
  .centered-image {
    display: block;
    margin: 0 auto;
    max-width: 100%; /* Ensure the image doesn't exceed the viewport width */
    transition: transform 0.3s; /* Add smooth transition for zoom effect */
  }

  .centered-image:hover {
    transform: scale(1.7); /* Zoom in by 20% on hover */
  }
</style>

<img src="{{ "/images/Group_10_Capstone_Poster.jpg" | relative_url }}" alt="Capstone Project Poster" width="1000" height="1000" class="centered-image"> -->

<!-- Regular image -->

<!-- <img src="{{ "/images/NLP_Twitter_Project_Poster.jpg" | relative_url }}" alt="Twitter Project Poster" width="1250" height="1250" class="centered-image"> -->
