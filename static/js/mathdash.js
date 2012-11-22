
$(document).ready(function() {
	if (ctx.user) {
		$(".authenticated").each(function() {
			$(this).show();
		});
	} else {
		$(".guest").each(function() {
			$(this).show();
		});
	}
});

function confirm_login() {
}

function gettext(text) {
	return __strings[text] || text;
}