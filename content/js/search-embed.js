/*
 * search-embed.js
 *
 * This should be included at the end of every page
 * that we want to include search functionality on.
 *
 * Pat David, 2016
 */

var searchForm = document.getElementById('search-form');
var tipue_input = document.getElementById('tipue_search_input');
while( searchForm.firstChild ){
    searchForm.removeChild( searchForm.firstChild );
}
tipue_input.placeholder = "Search GIMP.org";
searchForm.appendChild( tipue_input );
searchForm.action = "/search.html";
