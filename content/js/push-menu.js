/*
 * If you thought my Python was bad
 * wait until you get a load of my js
 */

var navel = document.getElementById('navel');
var page = document.getElementById('pushPage');
var menu = document.getElementById('menu');

menu.style.visibility = 'visible';

var toggle = function(e){
    e.preventDefault();

    var page = document.getElementById('pushPage');
    var menu = document.getElementById('menu');

    if( menu.className.indexOf('show') !== -1 ){
        menu.className = "hide";
        // navel.className = "initial";
        page.removeEventListener('click', toggle, false);
        page.removeEventListener('touchstart', toggle, false);
    }else{
        menu.className = "show";
        // navel.className = "bottom";
        page.addEventListener('click', toggle, false);
        page.addEventListener('touchstart', toggle, false);
    }
}

navel.addEventListener("touchstart", toggle, false);
navel.addEventListener("click", toggle, false);


/* Scroll detection for showing/hiding navigation strip
 * on mobile
 */

var didScroll = false;
var navbar = document.getElementById('navstrip');
var navHeight = navbar.offsetHeight;
var delta = 10;
var lastScrollTop = 0;

window.onscroll = doScroll;

function doScroll(){
    /*
    if( window.innerWidth >= 1024 ){
    }else{
        didScroll = true;
    }
    */
    if( window.innerWidth < 1024) didScroll = true;
}

setInterval( function() {
    if( didScroll ) {
        didScroll = false;
        var st = window.pageYOffset;

        if(Math.abs(lastScrollTop - st) <= delta)
            return;

        console.log( st );

        // If scroll past navbar, add class .nav-up
        if ( st > lastScrollTop && st > 30){
            //scroll down
            navbar.className = navbar.className.replace('nav-down','nav-up');
			//b.backgroundPositionY = parseInt( b.backgroundPositionY ) + 4 + '%';
        }else{
            //scroll up?
            navbar.className = navbar.className.replace('nav-up','nav-down');
			//b.backgroundPositionY = parseInt( b.backgroundPositionY ) - 4 + '%';
        }
        lastScrollTop = st;
    }
}, 250);

menu.style.display = 'block';
menu.style.zIndex = '1';
