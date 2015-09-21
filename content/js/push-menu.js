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
        page.removeEventListener('click', toggle, false);
        page.removeEventListener('touchstart', toggle, false);
    }else{
        menu.className = "show";
        page.addEventListener('click', toggle, false);
        page.addEventListener('touchstart', toggle, false);
    }
}

navel.addEventListener("touchstart", toggle, false);
navel.addEventListener("click", toggle, false);
