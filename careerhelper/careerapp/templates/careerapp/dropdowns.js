function socUrl(code) {
	return '/dropdown/' + code + '/'
}

var major = '';
var minor = '';
var broad = '';

$('#jobselector').cascadingDropdown({
	usePost: false,
	selectBoxes: [
	{
		selector: '.majorgroup',
		source: '/dropdown/majorgroups/',
		onChange: function(event, value, requiredValues, requirementsMet) {
			major = value;
		}
	},
	{
		selector: '.minorgroup',
		paramName: 'minorgroup',
		requires: ['.majorgroup']
		source: function(request, response) {
			$.getJSON(socUrl(major), request, function(data) {
				var selectOnlyOption = data.length <= 1;
				response($.map(data, function(item, index) {
					return {
						label: item,
						value: index,
						selected: selectOnlyOption
					};
				}));
			});
		},
		onChange: function(event, value, requiredValues, requirementsMet) {
			minor = value;
		}
	},
	{
		selector: '.broadgroup',
		paramName: 'broadgroup',
		requires: ['.majorgroup', '.minorgroup'],
		source: function(request, response) {
			$.getJSON(socUrl(minor), request, function(data) {
				var selectOnlyOption = data.length <= 1;
				response($.map(data, function(item, index) {
					return {
						label: item,
						value: index,
						selected: selectOnlyOption
					};
				}));
			});
		},
		onChange: function(event, value, requiredValues, requirementsMet) {
			broad = value;
		}
	},
	{
		selector: '.job',
		paramName: 'job',
		requires: ['.majorgroup', '.minorgroup'],
		source: function(request, response) {
			$.getJSON(socUrl(broad), request, function(data) {
				var selectOnlyOption = data.length <= 1;
				response($.map(data, function(item, index) {
					return {
						label: item,
						value: index
					};
				}));
			});
		}
	}
}
}



