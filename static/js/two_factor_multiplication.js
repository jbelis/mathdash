
function TwoFactorMultiplication() {
	var first, second;
		
	this.name = function() { return 'two_factor_multiplication_upto_9' }
	this.next = function() {
		first = Math.floor(10*Math.random());
		second = Math.floor(10*Math.random());
		return first + ' x ' + second;
	}
	
	this.display = function(problem) {
		this.question.text(problem.first + ' x ' + problem.second);
	}
	
	this.check = function(val) {
		var expected = Math.round(first * second);
		if (expected == val) {
			// right!
			return 1;
		} else if (val < 10 && expected >= 10) {
			// partial answer
			return 0;
		} else {
			return -5;
		}
	}
	
	this.reset = function() {
		return '? x ?';
	}
}

