---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
  .education-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .education-icon {
    margin-right: 10px;
    width: 100px; /* Adjust this size as needed */
    height: auto;
  }

  .education-list {
    margin-left: 75px; /* Adjust the indentation as needed */
  }

  /* .work-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .work-icon {
    margin-right: 10px;
    width: 60px; 
    height: auto;
  }

  .work-list {
    margin-left: 50px; 
  } */

  .work-list {
    list-style-type: none;
    padding: 0;
    margin-left: 50px; /* Adjust the indentation as needed */
  }

  .work-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    line-height: 3; /* Adjust the line height as needed */
  }

  .work-icon {
    margin-right: 10px;
    height: 100px;
    width: auto;
  }

</style>

Education
======

<div class="education-item">
  <img class="education-icon" src="/images/nyu_seal.png" alt="NYU Seal">
  M.S. in Data Science, New York University, 2023
</div>

<div class="education-item">
  <img class="education-icon" src="/images/columbia_seal.png" alt="Columbia Seal">
  B.S. in Applied Physics, Columbia University, 2020
</div>

<ul class="education-list">
  <li>Heavyweight Rowing Team (elected Captain)</li>
  <li>Minor in History</li>
</ul>

Work experience
======

<!-- <div class="work-item">
  <img class="work-icon" src="/images/nasa_meatball.png" alt="NASA Meatball">
  Scientific Programmer @ the NASA Goddard Institute for Space Studies (July 2023 - Present)
</div>

<div class="work-item">
  <img class="work-icon" src="/images/nuance_microsoft.webp" alt="Nuance + Microsoft">
  Research Engineering Intern @ Nuance Communications / Microsoft (Summer 2022)
</div>

<div class="work-item">
  <img class="work-icon" src="/images/earthshot_labs.jpeg" alt="Earthshot Lab">
  Remote Sensing Analyst @ Earthshot Labs(Feb - Apr 2021)
</div>

<div class="work-item">
  <img class="work-icon" src="/images/nasa_meatball.png" alt="NASA Meatball">
  Research Intern @ the NASA Goddard Institute for Space Studies (Summer 2020)
</div>

<div class="work-item">
  <img class="work-icon" src="/images/asbpn.jpg" alt="ASBPN">
  Solar Physics Consultant @ Autonomous Solar Barge Propulsion Network LLC (Apr 2020 - Feb 2021)
</div>

<div class="work-item">
  <img class="work-icon" src="/images/lamont_doherty.jpeg" alt="LDEO">
  Research Intern @ the Lamont-Doherty Earth Observatory** (Summer 2019)
</div> -->

<ul class="work-list">
  <li class="work-item">
    <img class="work-icon" src="/images/nasa_meatball.png" alt="NASA Meatball">
    Scientific Programmer @ the NASA Goddard Institute for Space Studies (July 2023 - Present)
  </li>
  <li class="work-item">
    <img class="work-icon" src="/images/nuance_microsoft.webp" alt="Nuance + Microsoft">
    Research Engineering Intern @ Nuance Communications / Microsoft (Summer 2022)
  </li>
  <li class="work-item">
    <img class="work-icon" src="/images/earthshot_labs.jpeg" alt="Earthshot Lab">
    Remote Sensing Analyst @ Earthshot Labs (Feb - Apr 2021)
  </li>
  <li class="work-item">
    <img class="work-icon" src="/images/nasa_meatball.png" alt="NASA Meatball">
    Research Intern @ the NASA Goddard Institute for Space Studies (Summer 2020)
  </li>
  <li class="work-item">
    <img class="work-icon" src="/images/asbpn.jpg" alt="ASBPN">
    Solar Physics Consultant @ Autonomous Solar Barge Propulsion Network LLC (Apr 2020 - Feb 2021)
  </li>
  <li class="work-item">
    <img class="work-icon" src="/images/lamont_doherty.jpeg" alt="LDEO">
    Research Intern @ the Lamont-Doherty Earth Observatory (Summer 2019)
  </li>
</ul>

* Non-technical
  * I've worked as a rowing coach (summer 2015/2016, spring 2018)
  * My first job was in a restaurant, running tables, doing deliveries, and expediting food (summer 2014)
  
Technical Skills
======
* Python (primary language)
  * Pandas
  * NumPy
  * Scikit-learn
  * PyTorch
  * PySpark
  * Dask 
  * pytest
* MATLAB
* Git
* Linux
* High performance cloud computing
  * Azure
  * AWS

Publications (every single one of them!)
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
