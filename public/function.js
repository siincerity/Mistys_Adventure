var one = "#0808d8", //title
		two = "#44a039", //marta
		three = "#ba04ce", //wyn
		four = "#f70e02", //mohammad
		five = "#ef6300", //ariel
    six = '#f7aaf4'; // Michael



$(window).on("scroll touchmove", function() {
		if ($(document).scrollTop() >= $("#welcome").position().top) {
				$('body').css('background', $("#welcome").attr("data-color"));
		};
		if ($(document).scrollTop() > $("#turtle").position().top) {
				$('body').css('background', $("#turtle").attr("data-color"))
		};
		if ($(document).scrollTop() > $("#clam_shell").position().top) {
 
				$('body').css('background', $("#clam_shell").attr("data-color"))
		};
		if ($(document).scrollTop() > $("#shark").position().top) {
 
				$('body').css('background', $("#shark").attr("data-color"))
		};
		if ($(document).scrollTop() >= $("#starfish").position().top) {
				$('body').css('background', $("#starfish").attr("data-color"))
		};
    if ($(document).scrollTop() >= $("#coral").position().top) {
      $('body').css('background', $("#coral").attr("data-color"))
    };
});

