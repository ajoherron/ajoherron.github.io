---
title: "Predicting Sentiment of Tweet Replies"
excerpt: "For my final project in my Natural Language Processing course, I chose to reproduce a study that sought to predict the aggregate sentiment of a given tweet's replies (as positive, neutral, or negative). I used both a Bi-LSTM and a CNN model for this task. Overall, I was able to come within 2% of the top published results, with the Bi-LSTM slightly outperfomring the CNN on a hand-labeled test set. <br/>
<img src='/images/twitter_project.JPG' alt='Twitter Project' width='600' height='600'>"
collection: portfolio
---

(Click to expand)


<html>
<head>
  <style>
    .click-to-zoom img {
      width: 100%;
      height: auto;
      cursor: pointer;
      transition: transform 0.3s;
    }

    .click-to-zoom img:hover {
      transform: scale(1.8); /* Zoom in by 20% on hover */
    }
  </style>
</head>
<body>

<div class="click-to-zoom">
  <a href="{{ "/images/NLP_Twitter_Project_Poster.jpg" | relative_url }}" target="_blank">
    <img src="{{ "/images/NLP_Twitter_Project_Poster.jpg" | relative_url }}" alt="Capstone Project Poster">
  </a>
</div>

</body>
</html>



<!-- 
<html>
<head>
  <style>
    .click-to-zoom {
      position: relative;
      width: 750px; /* Set the initial width */
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
      element.style.width = '1400px'; /* Set the expanded width */
    } else {
      element.style.width = '100%';
    }
  }
</script>

</body>
</html> -->
