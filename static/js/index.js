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

// Delete after 8/25/2017

// Create banner at top of page
var banner_html =
	'<div id="banner">' +
		'<p>' +
			'Join us for our annual AB Tech information session on August 25, 2017.' +
			'Click <a href="https://www.facebook.com/events/282813772201065/?                                    acontext=%7B%22ref%22%3A%22106%22%2C%22action_history%22%3A%22null%22%7D" target="blank_">here</a> for details.' +
		'</p>' +
	'</div>';
$('body').prepend(banner_html);

// Shift navbar to underneath banner
var navbar = $('.navbar:eq(0)');
navbar.css('position','absolute');
navbar.css('top',$('#banner').css('height'));

// End delete
