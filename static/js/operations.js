/*
 * copy
 */
var Answer = {
	CONTINUE: 0,
	INCORRECT: -1,
	CORRECT: 1
}

operations['two_factor_multiplication_upto_9'].next = function(state) {
	state.first = Math.floor(10 * Math.random());
	state.second = Math.floor(10 * Math.random());
	return state.first + ' x ' + state.second;
}

operations['two_factor_multiplication_upto_9'].check = function(state, val) {
	var answer = parseInt(val);
	if (typeof answer != 'undefined' && !isNaN(answer)) {
		var expected = Math.round(state.first * state.second);
		if (expected == val) {
			// right!
			return Answer.CORRECT;
		} else if (val < 10 && expected >= 10) {
			// partial answer
			return Answer.CONTINUE;
		} else {
			return Answer.INCORRECT;
		}
	} else {
		return Answer.CONTINUE;
	}
}


operations['additions_substractions'].next = function(state) {
	state.first = Math.floor(19 * Math.random()) - 9;
	state.second = Math.floor(19 * Math.random()) - 9;
	state.sign = Math.floor(2 * Math.random()) - 1;
	return ((state.first < 0) ? '('+state.first+')' : state.first)  +
	((state.sign < 0) ? ' - ' : ' + ') +
	((state.second < 0) ? '('+state.second+')' : state.second);
}

operations['additions_substractions'].check = function(state, val) {
	var answer = parseInt(val);
	if (typeof answer != 'undefined' && !isNaN(answer)) {
		var expected = Math.round(((state.sign < 0) ? (state.first - state.second) : (state.first + state.second)));
		if (expected == val) {
			// right!
			return Answer.CORRECT;
		} else if (Math.abs(val) < 10 && Math.abs(expected) >= 10) {
			// partial answer
			return Answer.CONTINUE;
		} else {
			return Answer.INCORRECT;
		}
	} else {
		return Answer.CONTINUE;
	}
}
