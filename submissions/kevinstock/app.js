$(document).ready(function() {
	
	$('.preview').click(function() {
		if ($('#imageContainer').css('display') == 'none') {
			var image = ($(this).attr('src'));
			$('<img src="' + image + '" alt="Race Logo or Results Image" />').appendTo('#image');
			$('#imageContainer').show('slow');
		}
	});
	
	$('#imageContainer').click(function() {
		$('#image').empty();
		$('#imageContainer').hide();		
	})

})