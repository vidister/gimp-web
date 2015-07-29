//images

function roundCorners () {
	$("#linkbar").corner("12px bottom");
	$("#menu").corner("14px bl");
	$("#title").corner("12px top")
}

function mangleforIE() {
	//alert("ohno!");
}

function mangleforOpera() {
  var link = document.createElement('link');
  link.type = 'text/css';
  link.rel = 'stylesheet';
  link.href = '/style/opera.css';
  $('head').append(link);

  //if there's no splash, add padding. yes it's so eeky.
  if (!$('div.splash').text()) {
    $("#menu").css("margin","0 0 1em 1em");
  }
}

//provide download page depending on OS
function renderDownload(platform) {

    platforms = {
	"oslinux"   : "GNU/Linux",
	"osmac"     : "OS X",
	"oswindows" : "Microsoft Windows",
	"osall"     : "All",
    };

    // decide which platform to show
    if (platform == undefined) {
	platform    = "os" + $.browser.OS.toLowerCase();
    }

    if ( ! $("#os").length ) {
	$("#downloads").html("<div id=\"moreos\"></div>\n<div id=\"os\"></div>\n<hr />\n<div id=\"source\"></div>\n");
	$("#moreos").html("Our site thinks that you are using: " + platforms[platform] + "</br>" +
			  "Show downloads for <a href=\"javascript:renderDownload('oslinux');\">"   + platforms['oslinux']   + "</a>" +
                                          " | <a href=\"javascript:renderDownload('osmac');\">"     + platforms['osmac']     + "</a>" +
                                          " | <a href=\"javascript:renderDownload('oswindows');\">" + platforms['oswindows'] + "</a>" +
                                          " | <a href=\"javascript:renderDownload('osall');\">"     + platforms['osall']     + "</a>");

	// always have all the divs
	$("#os").html("<div id=\"oslinux\"></div>\n<div id=\"osmac\"></div>\n<div id=\"oswindows\"></div>\n");
    }

    // load contents if necessary
    if ( $("#oslinux").is(':empty') ) {
	$("#oslinux").load("Linux.html");
    }

    if ( $("#osmac").is(':empty') ) {
	$("#osmac").load("Mac.html");
    }

    if ( $("#oswindows").is(':empty') ) {
	$("#oswindows").load("Windows.html");
    }

    if (platform == "osall") {
	$("#oslinux").show();
	$("#osmac").show();
	$("#oswindows").show();
    }
    else
    {
	$('#os').children().each(function() {
	    if ($(this).attr('id') != platform) {
		$(this).hide();
	    } else {
		$(this).show();
	    };
	});


    }

    if ( $("#source").is(':empty') ) {
	$("#source").load("source.html"); //sources for all
    }
}

var usertyped = ""; //for the easteregg

function easterEgg(key) {
	var keychar = String.fromCharCode(key.charCode);
	usertyped += keychar;
	if (usertyped.indexOf("eek")!=-1) {
		var splash = "<img id=\"eek\" style=\"width: 300px; height: 400px; ";
		splash += "display: block; position: fixed;";
		splash += "top: 50%; left: 50%; margin: -200px 0 0 -150px;\"";
		splash += " src=\"/about/splash/images/eek.png\" alt=\"eeeeek!\" />";
		$("body").append(splash);
		$("#eek").click( function () {
			$(this).fadeOut()
		});
		usertyped = "";
	}
	if (key.keyCode==27) {
		$("#eek").fadeOut();
	}
}



$(document).ready(function() {
	$("#menu").hide().fadeIn(2000);
	roundCorners();
	if($.browser.msie) {
		mangleforIE();
  }
	$(document).keypress(function (key) {
		easterEgg(key);
	});
});
