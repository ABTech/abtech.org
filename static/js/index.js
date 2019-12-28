//backround settings
$('body').vegas({
delay: 10000,
transition: 'fade',
timer: false,
transitionDuration: 3000,
preload: true,
slides: [
    { src: "static/img/gallery/griz-sc2016.jpg" },
    { src: "static/img/gallery/lg2016.jpg" },
    { src: "static/img/gallery/gs_sound.jpg" },
    { src: "static/img/gallery/dejj-2014.jpg" },
    { src: "static/img/gallery/ds.jpg" },
]
});

function getOpacity(scroll){
  var pageHeight = document.body.clientHeight - 50;
  var op = 2.5*(pageHeight - scroll)/pageHeight;
  console.log(op);
  if(op > 1.25) op = 2.5 - op;
  //Returns 1 if greater than 1, 0 if less than 0, the opacity otherwise
  return (op > 1)?1:((op < 0)?0.1:op+0.1);
};

var scrollElem = document.getElementsByClassName("content-shift")[0];
var contentElem = document.getElementsByClassName("index-content")[0];
var bg = document.getElementsByClassName("background-image")[0];
scrollElem.addEventListener("scroll", function() {
  for(var i = 0; i < contentElem.children.length; i++){
    var scroll = contentElem.children[i].offsetTop + contentElem.children[i].clientHeight/2 - scrollElem.scrollTop;
    console.log(i, getOpacity(scroll));
    contentElem.children[i].style.opacity = getOpacity(scroll);
  }
});
