---
layout: default
permalink: /
nav_page: home
stylesheets:
 - '/assets/css/pages/index.css'
---


<div id="bg-carousel" class="carousel slide carousel-fade w-100 h-100" data-bs-touch="false" data-bs-ride="carousel" data-bs-interval="5000">
  <div class="carousel-inner w-100 h-100">
    {% for item in site.data.index_carousel %}
    <div class="carousel-item{% if forloop.first %} active{% endif %} w-100 h-100">
      <img src="{{  item | prepend: '/assets/img/carousel/' | append: '.jpg' | realtive_url }}" class="d-block w-100 h-100" alt="{{ item }}">
    </div>
    {% endfor %}
  </div>
</div>
<div id="bg-carousel-gradient" class="d-block w-100 h-100"></div>

<div class="row justify-content-center align-items-center align-items-sm-end h-100">
    <img src="{{ '/assets/img/abtech_flybynight_white.svg' | relative_url }}" class="img-fluid d-none d-sm-block col-6 col-xl-5 text-center logo-red-shadow logo-fade-in" alt="AB Tech Logo" />
    <p class="col-sm-10 col-11 text-white text-center m-30"><strong>The Activities Board Technical Committee</strong>, commonly known as <strong class="text-nowrap">AB Tech</strong>, is the production organization charged with handling the technical production of university-sponsored events at Carnegie Mellon University. We provide high quality, professional grade entertainment production services, including sound reinforcement, lighting design, stage management, power/rigging support, and event management at heavily subsidized rates to the campus community. Our clients include student groups, university administration, and faculty. We also facilitate staging rentals, backline rentals, and more.</p>
</div>
