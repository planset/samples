
        function requestFullscreen(ele){
            if (ele.requestFullscreen) {
                ele.requestFullscreen();
            }
            else if (ele.webkitRequestFullscreen) {
                ele.webkitRequestFullscreen();
            }
            else if (ele.msRequestFullscreen) {
                ele.msRequestFullscreen();
            }
            else if (ele.mozRequestFullScreen) {
                ele.mozRequestFullScreen();
            }
        }
        
        function exitFullscreen(){
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
            else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            }
            else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            }
            else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } 
        }
				
		function toggleFullscreen(ele){
			 if (!document.fullscreenElement &&    // alternative standard method
			  !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement ) {  // current working methods
				requestFullscreen(ele);
			  }else{
				  exitFullscreen();
			  }
		}
        
        $(function(){
            var ele = document.getElementById('screen');
            toggleFullscreen(ele);
        });
        