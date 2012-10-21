

State = {
		STOPPED : 0,
		RUNNING : 1,
		PAUSED : 2
}

var error_penalty = 3;

var state = State.STOPPED;
var score = 0;
var count_answered = 0;
var count_answered_correct = 0;

var time_left = 120;
var timer;
var problem;

var lang;
if (navigator.userLanguage) // Explorer
  lang = navigator.userLanguage;
else if (navigator.language) // FF
  lang = navigator.language;
else
  lang = "en";


function Problem(element) {
	this.name = element.attr('id');
	var state = {};
	var el = element;
	var op = operations[this.name];
	
	this.next = function() { return op.next(state); }
	this.check = function(val) { return op.check(state, val); }
	this.reset = function() { return op.defaultDisplay; }
	this.title = function() { return op.title[lang] || op.title['en']; }
	this.description = function() { return op.description[lang] || op.description['en']; }
	this.deactivate = function() { el.removeClass('active'); }
	this.activate = function() { el.addClass('active'); }
	
	this.activate();
}

$(document).ready(function() {

	$(".gamechoice").each(function() {
		if ($(this).hasClass('active')) {
			problem = new Problem($(this));
		}
		$(this).click(function() {
			var fn = window[$(this).attr('id')]; 
			if (problem.name != fn) {
				problem.deactivate();
				
				problem = new Problem($(this));
				reset();
			}
		});
	});
	
	reset();

	$(this).keyup(function(event) {
		if (event.which == 32) {
				switch(state) {
				case State.RUNNING : 
					pause();
					break;

				case State.STOPPED : 
				case State.PAUSED : 
					resume();
					break;
				}				
		}
	});

	$("#answer").keyup(function() {
		if (state == State.RUNNING) {
			var answer = problem.check($('#answer').val());
			switch (answer) {
			case Answer.CORRECT:
				count_answered_correct++;
			case Answer.INCORRECT:
				count_answered++;
				setStatus(answer);
				update_score(answer);
				$("#question").text(problem.next());
				$('#answer').val('');
				break;
			}
		}
	});

	$("#start").click(function() {
		switch(state) {
		case State.STOPPED : 
			start();
			break;

		case State.RUNNING : 
			pause();
			break;

		case State.PAUSED : 
			resume();
			break;

		default : 
			error("invalid state: " + state);

		}

	});
	
	$("#stop").click(function() {
		if (state != State.STOPPED) {
			stop();
		}
	});

	reset();
	
});

function update_score(answer) {
	score += (answer == Answer.CORRECT) ? 1 : (-error_penalty);
	if (score < 0) score = 0;
	$("#score").text(score);
}

function start() {
	if (!ctx.user) {
		bootbox.confirm("You're not signed-in.  Mathdash will no record your points", 
				"Just practice", 
				"Sign-in now and record my points", 
				function(result) {
		    if (result) {
		        window.open(ctx.login_url);
		    } else {
		    	reset();
		    	resume();
		    }
		});
	} else {
    	reset();
    	resume();
	}
}

function pause() {
	$("#answer").attr('disabled', 'disabled');
	clearInterval(timer);

	// change symbol
	$("#start").removeClass("pause");
	$("#start").addClass("play");
	state = State.PAUSED;
	
	$("#paused").show();
}

function setStatus(answer) {
	switch(answer) {
	case Answer.CONTINUE:
		$($(".mathdash-status")[0]).removeClass('good'); 
		$($(".mathdash-status")[0]).removeClass('oops'); 
		break;
	case Answer.CORRECT:
		$($(".mathdash-status")[0]).addClass('good'); 
		$($(".mathdash-status")[0]).removeClass('oops'); 
		break;
	case Answer.INCORRECT:
		$($(".mathdash-status")[0]).removeClass('good'); 
		$($(".mathdash-status")[0]).addClass('oops'); 
		break;
	}
}

function resume() {
	if (time_left <= 0) {
		finish();
		return;
	}
	
	// load new problem
	$("#question").text(problem.next());
	
	// change button
	$("#start").removeClass("play");
	$("#start").addClass("pause");

	// start timer
	timer = setInterval(function() {
		time_left--;
		if (time_left <= 0) {
			finish();
			return;
		} else {
			$("#time_left").text(time_left);
		}
	}, 1000);

	$("#time_left").text(time_left);
	$("#answer").val('');
	$("#answer").attr('disabled', false).focus();
	state = State.RUNNING;
	$("#paused").hide();
	
}

function finish() {
	if (timer) {
		clearInterval(timer);
		timer = null;
	}
	state = State.STOPPED;
	$("#answer").attr('disabled', 'disabled');
	$("#start").removeClass("pause");
	$("#start").addClass("play");
	
	var result_data = {
		game: problem.name,
		completed: 1,
		score: score,
		count_answer: count_answered,
		count_answer_correct: count_answered_correct,
		duration: 120 - time_left
	}
	display_results(result_data);
	
	send_results(result_data);		
	
	$("#paused").hide();

}

function send_results(result_data) {
	if (ctx.user) {
		$.ajax({
			url : 'result',
			data : result_data,
			type : 'POST',
			error : function(response, errorType, reason) {
				//alert("error");
			},
			success : function(data, textStatus, jqXHR) {
				//alert("success");
			}
		});
	} else {
		// show an alert to the fact that if you were logged-in I could save it
	}
}

function display_results(data) {
	$("#time_spent").text(data.duration);
	$("#questions_total").text(data.count_answer);
	$("#questions_correct").text(data.count_answer_correct);
	$("#mathdash-running").hide(); 
	if (data.completed) {
		$("#mathdash-goodwork").show();
		$("#mathdash-emoticon").addClass('positive');
	} else {
		$("#mathdash-gaveup").show();
		$("#mathdash-emoticon").addClass('negative');
	}
	$("#mathdash-results").show();
}

function stop() {
	if (timer) {
		clearInterval(timer);
		timer = null;
	}
	state = State.STOPPED;
	$("#answer").attr('disabled', 'disabled');
	$("#start").removeClass("pause");
	$("#start").addClass("play");
	
	// report results
	var result_data = {
		game : problem.name,
		completed : 0,
		score : score,
		count_answer : count_answered,
		count_answer_correct : count_answered_correct,
		duration : 120 - time_left
	}
	display_results(result_data);
	//send_results(result_data);
	
	$("#paused").hide();
}

// reset all user interface elements in preparation of a new challenge.
function reset() {
	
	// kill timer if still running
	if (timer) {
		clearInterval(timer);
		timer = null;
	}

	// reset and show time
	time_left = 120;
	$("#time_left").text(time_left);
	$("#mathdash-running").show(); 
	$("#mathdash-goodwork").hide(); 
	$("#mathdash-gaveup").hide(); 
	$("#mathdash-results").hide();
	$("#mathdash-emoticon").removeClass('positive')
	$("#mathdash-emoticon").removeClass('negative')
	
	// reset score
	$("#score").text('0');
	score = 0;
	
	// reset problem
	count_answered = 0;
	count_answered_correct = 0;
	$('#question').text(problem.reset());
	setStatus(Answer.NONE);
	
	$("#paused").hide();
}


