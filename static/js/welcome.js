jQuery(document).ready( 
function($){ 
$("img").lazyload({ 
placeholder : "{{STATIC_URL}}img/grey.jpg", 
effect      : "fadeIn" 
}); 
}); 