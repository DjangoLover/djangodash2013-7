$(function ()                                 
{
	var methods     =   _main.methods,
	functions   =   _main.functions;
	$.each(functions,function(key,val){ this() });
	$('.colorbox').colorbox();
});

_main = {
	option: {},
	functions: {
		toogleBlock: function (){
			$('#toogleBlock').each(function(){
				$(this).click(function(){
					$('#'+$(this).attr('rel')).slideToggle()
					return false;
				});
			});
		},
		mosaic: function(){
			function request(){

				$.getJSON( "/is_mosaic_ready/?"+Math.round(new Date().getTime() / 1000), function( data ){
					if(data.url){
						$('.buttonMosaic, .whiteBlock iframe').remove();
						$('#mosaic').html('<a href="'+data.url+'" class="colorbox"><img src="'+data.url+'" /></a>');
						clearInterval(interval);
					}
				});
			}
			interval = setInterval(function(){request()}, 1000);
		},
		celebrity: function(){
			$('a.avatarMin').live( "click",function(){
				var name 		=	$(this).find('.name').text(),
					img			=	$(this).find('img').attr('src'),
					age			=	$(this).find('.age').text(),
					description	=	$(this).find('.description').text();

				$('.information h2').text(name);
				$('.information p.age').text(age);
				$('.information p.description').text(description);
				$('.information .avatarMin img').attr('src',img);
				return false;
			});

            function request2(){
				$(this).addClass('loading');
				$.getJSON( "/parse_api/famous?"+Math.round(new Date().getTime() / 1000), function( data ){
					var output = '';

					$.each(data,function(key,p){
                        if(key == 0){
                            $('.information h2').text(p.name);
                            $('.information p.age').text(p.age);
                            $('.information p.description').text(p.description);
                            $('.information .avatarMin img').attr('src', p.src);
                        }else{
                            output += '<a href="#" class="avatarMin"><img src="'+p.src+'"><div class="hide"><div class="name">'+p.name+'</div><div class="age">Age: '+p.age+'</div><div class="description">'+p.description+'</div></div></a>';
                        }

					});
					$('#celebrity').html(output);



				}).done(function() {
					$('#more').removeClass('loading');
                    clearInterval(interval2);
				})
				return false;
			}
			$('#more').click(function(){request2()});
            interval2 = setInterval(function(){request2()}, 1000);
		}

	}
}