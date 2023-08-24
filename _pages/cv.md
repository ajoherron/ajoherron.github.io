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
  .item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .icon {
    margin-right: 10px;
    width: 100px; /* Adjust this size as needed */
    height: auto;
  }

  .list {
    margin-left: 75px; /* Adjust the indentation as needed */
  }
</style>

Education
======

<div class="item">
  <img class="icon" src="/images/nyu_seal.png" alt="NYU Seal">
  M.S. in Data Science, New York University, 2023
</div>

<div class="item">
  <img class="icon" src="/images/columbia_seal.png" alt="Columbia Seal">
  B.S. in Applied Physics, Columbia University, 2020
</div>

<ul class="list">
  <li>Heavyweight Rowing Team (elected Captain)</li>
  <li>Minor in History</li>
</ul>

Work experience
======

* **Scientific Programmer @ the NASA Goddard Institute for Space Studies** (July 2023 - Now)

* **Research Engineering Intern @ Nuance Communications / Microsoft** (Summer 2022)

* **Remote Sensing Analyst @ Earthshot Labs** (Feb - Apr 2021)

* **Research Intern @ the NASA Goddard Institute for Space Studies** (Summer 2020)

* **Solar Physics Consultant @ Autonomous Solar Barge Propulsion Network LLC** (Apr 2020 - Feb 2021)

* **Research Intern @ the Lamont-Doherty Earth Observatory** (Summer 2019)

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

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
