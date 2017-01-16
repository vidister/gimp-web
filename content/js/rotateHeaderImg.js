/*
 * Simple Header Image Randomization
 * ---------------------------------
 *
 *  Just add objects to the `imglist` var below.
 *  If you don't have data, use an empty set "".
 *  
 *  name: Image author name/attribution
 *  title: The title of the work (if applicable)
 *  file: Path to the image (ie: /images/frontpage/headers/FILE.jpg)
 *          Try to keep the image around 2048px wide
 *          and aggressively compress to keep it under 300kb
 *          the smaller the better for load times
 *  license: cc-by-sa by default
 *          options:
 *                  cc-by
 *                  cc-by-sa
 *                  cc-by-sa-nc
 *                  cc-by-nd
 *          _Strongly_ suggest we stick to cc-by or cc-by-sa.
 */

var imglist = [
    {
        "author": "Ville Pätsi",
        "authorURL": "http://shadowdrama.net/",
        "title": "Niagara Rainbow",
        "sourceURL": "https://www.flickr.com/photos/shadowdrama/20786243805",
        "file": "/images/frontpage/headers/Niagara_Rainbow.jpg",
        "license": "cc-by-sa"
    },{
        "author": "Pat David",
        "authorURL": "https://pixls.us",
        "title": "After the Cotton",
        "sourceURL": "https://www.flickr.com/photos/patdavid/10614802615",
        "file": "/images/frontpage/headers/cotton.jpg",
        "license": "cc-by-sa"
    }
]


var imgBanner = document.getElementById('banner');
var imgAttr = document.getElementById('headerImgAttr');
var title = imgAttr.getElementsByClassName('headerTitle')[0];
var author = imgAttr.getElementsByClassName('headerAuthor')[0];
var lic = imgAttr.getElementsByClassName('headerLicense')[0];

var image = imglist[ Math.floor( Math.random() * (imglist.length) )  ];

var himage = new Image();

himage.onload = function() {
    // Loading the style as a node into the dom
    // on the head element (CSP might bork if we do it to the 
    // element directly as inline (even after load?)
    var css = "#banner {"
    css += "background-image: linear-gradient(rgba(44,52,80,0.5), rgba(44,62,80,0.5)), url('"+ image.file +"');";
    css += "background-size: cover;";
    css += "background-position: 0;";
    css += "}";

    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild( document.createTextNode( css ) );
    document.head.appendChild( style );
}

himage.src = image.file;

if( typeof( image.title ) !== undefined ){
    title.innerText = image.title;
    title.title = image.title;
}

if( typeof( image.sourceURL ) !== undefined ){
    title.href = image.sourceURL;
}

if( typeof( image.author ) !== undefined ){
    author.innerText = image.author;
}

if( typeof( image.authorURL ) !== undefined ){
    author.href = image.authorURL;
}

if( typeof( image.license ) !== undefined ){
    switch( image.license ){
        case 'cc-by':
            lic.href = "https://creativecommons.org/licenses/by/4.0/";
            lic.getElementsByClassName('cc')[0].innerText = 'cb';
            break;
        case 'cc-by-sa':
            lic.href = "https://creativecommons.org/licenses/by-sa/4.0/";
            lic.getElementsByClassName('cc')[0].innerText = 'cba';
            break;
        case 'cc-by-sa-nc':
            lic.href = "https://creativecommons.org/licenses/by-nc-sa/4.0/";
            lic.getElementsByClassName('cc')[0].innerText = 'cban';
            break;
        case 'cc-by-nd':
            lic.href = "https://creativecommons.org/licenses/by-nd/4.0/";
            lic.getElementsByClassName('cc')[0].innerText = 'cbad';
            break;
    }
}
