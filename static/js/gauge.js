(function($) {
  $.fn.accordion = function(options) {
    // Add plugin code here
  };
})(jQuery);

$(document).ready(function() {
	
	
	$("#gauge").wijlineargauge({

		width : 50,
		height : 400,
		orientation : "vertical",
		xAxisLocation : 0.02,
		xAxisLength : 0.95,
		value : 65,
		labels : {
			style : {
				fill : "#1E395B",
				"font-size" : 10,
				"font-weight" : "300"
			}
		},
		tickMajor : {
			position : "inside",
			offset : -12,
			factor : 2,
			style : {
				fill : "#000",
				stroke : "none",
				opacity : 0.2
			}
		},
		tickMinor : {
			position : "inside",
			offset : -12,
			visible : true,
			style : {
				fill : "#000",
				stroke : "none",
				opacity : 0.2
			}
		},
		animation : {
			enabled : false
		},
		pointer : {
			visible : true,
			shape : "tri",
			length : 0.5,
			width : 4,
			style : {
				fill : "#000",
				stroke : "#434343",
				"stroke-width" : 0.5,
				opacity : 0.8
			}
		},
		face : {
			style : {
				fill : "180-#e4e4e4-#c0c0c0",
				stroke : "#8d8d8d",
				"stroke-width" : 0.5
			}
		},
		ranges : [ {
			startValue : 0,
			endValue : 50,
			startDistance : 0.75,
			endDistance : 0.75,
			startWidth : 0.15,
			endWidth : 0.15,
			style : {
				fill : "180-#CC00CC-#AA00AA",
				stroke : "none"
			}
		} ]
	});
	$("#btn").button().toggle(function() {
		$("#gauge").wijlineargauge("option", "ranges", [ {
			startValue : 0,
			endValue : 98.6,
			startDistance : 0.75,
			endDistance : 0.75,
			startWidth : 0.15,
			endWidth : 0.15,
			style : {
				fill : "180-#FF0000-#CC0000",
				stroke : "none"
			}
		} ]).wijlineargauge("redraw");
	}, function() {
		$("#gauge").wijlineargauge("option", "ranges", [ {
			startValue : 0,
			endValue : 10,
			startDistance : 0.75,
			endDistance : 0.75,
			startWidth : 0.15,
			endWidth : 0.15,
			style : {
				fill : "180-#0099FF-#0066CC",
				stroke : "none"
			}
		} ]).wijlineargauge("redraw");
	})
});
