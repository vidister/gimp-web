Title: Downloads
Date: 2015-08-14T14:18:56-05:00
Author: Pat David
Status: hidden

<style scoped>
table {
    max-width: 35rem;
    margin: 1rem auto;
}
td, th {
    padding: 0 1rem;
}

.download-mirror{
    word-wrap: break-word;
}

@media ( max-width: 40rem ){
    .download-mirror dd {
        margin-left: 0.5rem;
    }
}

.os {
    display: none;
}

#pOSTEST {
    font-style: italic;
}

.show_links {
    color: #497bad;
    cursor: pointer;
}

.win-button {
    display: inline-block;
    border: solid 1px #666;
    background-color: #f57900;
    margin: 0.5rem 0;
    border-radius: 10px;
    box-shadow: 1px 1px 2px;
    text-align: center;
    /* max-width: 300px;
    */
    font-family: Questrial;
    font-weight: 400;
    width: 49%;
}

#win-torrent, #osx-torrent {
    background-color: #008080;
}

.win-button a {
    color: white;
    font-weight: bold;
    display: inline-block;
    padding: 1rem;
}

#letmeknow { display: none; }
</style>

<noscript>
<style scoped>
.os { display: block; }
#others { display: none; }
#letmeknow { display: none; }
#pOSTEST { display: block; }
</style>
</noscript>

<figure>
<img src="downloadsplash-aryeom.jpg" alt="Download Splash Image courtesy of Areyom" />
</figure>

## Current Stable Version
The current stable release of GIMP is **2.8.16** (2015-11-21).

<div class="OSTEST" markdown="1">
We think your OS is 
<span id="pOSTEST">
Well, we don't actually know.  
Either Javascript is disabled, or I am not working quite right...  
So I am showing you all the options.  
That should cover it.
</span>  
<small id='letmeknow'>If this is wrong, please let Pat David (patdavid@gmail.com) know.
Please include the string returned above, and what your actual OS is.
Thank you!
</small>

<p id='others'>
Show downloads for 
<span class="show_links" id='os_linux'>GNU/Linux</span>&nbsp;| 
<span class="show_links" id='os_mac'>OS&nbsp;X</span>&nbsp;| 
<span class="show_links" id='os_win'>Microsoft&nbsp;Windows</span>&nbsp;| 
<span class="show_links" id='os_all'>All</span>
</p>

</div>

<div id='linux' class="os linux" markdown='1'>
## GIMP for Unix-like systems

It's very likely your Unix-like system such as a GNU/Linux distribution already comes with a GIMP package. It is a preferred method of installing GIMP, as the distribution maintainers take care of all the dependencies and bug fix updates. Please note that many distros decide to pin a specific version of GIMP to their releases.

### Debian, Mint, Ubuntu

Ubuntu, Mint, or Debian users can run `apt-get install gimp` to install GIMP. Ubuntu users may also install GIMP from [Software Centre](https://apps.ubuntu.com/cat/applications/gimp/), this includes recent GIMP versions from PPAs.

### openSUSE

SUSE users can install GIMP by running `yast -i gimp` or `zypper in gimp`, depending on the distribution version.

### Fedora

Similarly to the above, Fedora users can install GIMP by running `dnf install gimp`.

### Gentoo

Gentoo users can install GIMP by running `emerge gimp` for the latest stable version.

### Arch

Arch Linux users can install GIMP by running `pacman -S gimp`.

### Mageia 

Mageia Linux users can install GIMP by running `urpmi gimp`.

### BSD

GIMP is also available for the BSD family of systems such as FreeBSD and OpenBSD.

### Solaris

GIMP can run on Solaris.
</div>


<div id='mac' class="os mac" markdown="1">

## GIMP for Mac OS X

<span class='win-button' id='osx-torrent'>
<a href="http://download.gimp.org/pub/gimp/v2.8/osx/gimp-2.8.14.dmg.torrent">
    Download GIMP&nbsp;2.8.14<br/>
    via BitTorrent
</a>
</span>
<span class='win-button'>
<a href="http://download.gimp.org/pub/gimp/v2.8/osx/gimp-2.8.14.dmg">
    Download GIMP&nbsp;2.8.14<br/>
    directly
</a>
</span>

Since the 2.8.2 version, GIMP runs on OSX natively. No X11 environment is required.

### Native builds

Currently there are two main installers: a stock build by Sven Claussner and a custom build from Simone Karin Lehmann.

A GIMP 2.8 DMG installer by Sven Claussner (linked above) is a stock GIMP build without any add-ons. It works on OS X 10.6 Snow Leopard and later. Just open the downloaded DMG and drag and drop GIMP into your "Applications" folder.

The MD5 hash sum for `gimp-2.8.14.dmg` is:
<kbd>3392eb2cfe67258e7a3f8fc8807f00c0</kbd>.

A build by [Simone Karin Lehmann](http://gimp.lisanet.de/), with some extra plug-ins and changes:

* [Download GIMP 2.8 from lisanet.de](http://gimp.lisanet.de/Website/Download.html)



### Older Downloads
Previous installers for OSX can be found here: [download.gimp.org](//download.gimp.org/pub/gimp/v2.8/osx/).



### Macports
A (easy?) way to compile and install GIMP and other great [Free software](http://www.gnu.org/philosophy/free-sw.html) on your Mac is by using [Macports](http://www.macports.org/). The installer allows you to choose from a large directory of packages. To install gimp using Macports, you simply do `sudo port install gimp` once you have Macports installed.

Disclaimer: we have not investigated if it's feasible to build GIMP 2.8 from Macports. The [GIMP port file](https://trac.macports.org/browser/trunk/dports/graphics/gimp/Portfile) mentions 2.8.10, and appears to be maintained, however.

* [Download Macports](http://macports.org/)



### Homebrew
Homebrew is similar to Macports and provides packages (aka formulas) to install, either by compiling them from source or by using pre-made binaries. While there appears to be no formula for GIMP itself, there are reports that all dependencies are available. This may help to build GIMP from source.

* [Download Homebrew](http://brew.sh/)



### Fink
Fink is a package repository that offer mostly precompiled binaries. It provides the apt-get command known to e.g. Debian and Ubuntu users, and installing GIMP is as easy as `sudo apt-get install gimp` once you have installed the [Fink installer](http://www.finkproject.org/download/index.php).  
If there's no binary package, then `fink install gimp` will compile GIMP from source.

Disclaimer: we haven't been able to determine if it is possible to install or build GIMP 2.8 from Fink. GIMP 2.6.12 appears to be the most recent [GIMP package](http://pdb.finkproject.org/pdb/browse.php?summary=gimp) that is [offered there](http://pdb.finkproject.org/pdb/package.php/gimp2).

* [Download Fink](http://www.finkproject.org/)

</div>


<div id='win' class="os win" markdown="1">
## GIMP for Windows

<span class='win-button' id='win-torrent'>
<a href="//download.gimp.org/pub/gimp/v2.8/windows/gimp-2.8.16-setup.exe.torrent" title="Download GIMP via BitTorrent" id="win-torrent-link">
    Download GIMP&nbsp;2.8.16<br/>
    via BitTorrent
</a>  
</span>
<span class='win-button'>
<a href="//download.gimp.org/pub/gimp/v2.8/windows/gimp-2.8.16-setup.exe" title="Download GIMP via HTTP" id='win-download-link' >
    Download GIMP&nbsp;2.8.16<br/>
    directly
</a>
</span>
<br/>
These links download the official GIMP installer for Windows. 
The installer contains both 32-bit and 64-bit versions of GIMP, and will automatically use the appropriate one.

BitTorrent is a peer-to-peer file sharing system. It works by downloading GIMP from a distributed network of BitTorrent users, and may improve download speed dramatically. 
Choosing this option will download the torrent file for the GIMP installer. 
You may need to install a torrent client to make use of this file. <a href="//en.wikipedia.org/wiki/BitTorrent" title="BitTorrent on Wikipedia">Learn more...</a>

### MD5 Hash Sum
The MD5 hash sum for `gimp-2.8.16-setup.exe` is: <kbd>a2095f250fd3a776757ccddc477312d0</kbd>.

### Older Downloads
Previous installers for Windows can be found here: [download.gimp.org](//download.gimp.org/pub/gimp/v2.8/windows/).

### GIMP User Manual

*   [Chinese Simplified](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-zh_CN-setup.exe) (24.3 MB)
*   [Catalan](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-ca-setup.exe) (24.2 MB)
*   [Danish](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-da-setup.exe) (24.2 MB)
*   [Dutch](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-nl-setup.exe) (24.3 MB)
*   [English](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-en-setup.exe) (24.2 MB)
*   [English (United Kingdom)](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-en_GB-setup.exe) (24.2 MB)
*   [French](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-fr-setup.exe) (25.7 MB)
*   [German](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-de-setup.exe) (28.0 MB)
*   [Italian](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-it-setup.exe) (30.2 MB)
*   [Japanese](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-ja-setup.exe) (23.6 MB)
*   [Korean](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-ko-setup.exe) (24.9 MB)
*   [Norwegian Nynorsk](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-nn-setup.exe) (20.9 MB)
*   [Russian](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-ru-setup.exe) (24.9 MB)
*   [Slovenian](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-sl-setup.exe) (24.3 MB)
*   [Spanish](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-es-setup.exe) (24.9 MB)
*   [Swedish](//download.gimp.org/pub/gimp/help/windows/2.8/2.8.1/gimp-help-2-2.8.1-sv-setup.exe) (24.7 MB)
</div>

---

<div id='source'  markdown="1">
## Source for version 2.8 (Stable)

GIMP releases available from gimp.org and its [mirrors](#mirrors) contain the source code and have to be compiled in order to be installed on your system.

For instructions, how to build GIMP from source code, please see [this page](/source/).

GIMP 2.8.16 is now available at [http://download.gimp.org/pub/gimp/v2.8/](//download.gimp.org/pub/gimp/v2.8/). You may want to read the [Release Notes for GIMP 2.8](/release-notes/gimp-2.8.html).

To allow you to check the integrity of the tarballs, here are the MD5 sums of the latest releases:

**gimp-2.8.16.tar.bz2**  
<kbd>30e0a1b7c18b0e3415f4ac54567252ac</kbd>

**gimp-2.8.14.tar.bz2**  
<kbd>233c948203383fa078434cc3f8f925cb</kbd>

**gimp-2.8.12.tar.bz2**  
<kbd>47fefa240c38cfb1016b57ad6324378d</kbd>

**gimp-2.8.10.tar.bz2**  
<kbd>84c964aab7044489af69f7319bb59b47</kbd>

**gimp-2.8.8.tar.bz2**  
<kbd>ef2547c3514a1096931637bd6250635a</kbd>

**gimp-2.8.6.tar.bz2**  
<kbd>12b3fdf33d1f07ae79b412a9e38b9693</kbd>

**gimp-2.8.4.tar.bz2**  
<kbd>392592e8755d046317878d226145900f</kbd>

**gimp-2.8.2.tar.bz2**  
<kbd>b542138820ca3a41cbd63fc331907955</kbd>

**gimp-2.8.0.tar.bz2**  
<kbd>28997d14055f15db063eb92e1c8a7ebb</kbd>


GIMP help files are available at [http://download.gimp.org/pub/gimp/help/](//download.gimp.org/pub/gimp/help/).

Please consider using one of the mirrors listed below.

## Development snapshots

There are no releases of the 2.9 development version yet.

Nightly builds for Windows are available at [darkrefraction.com](http://nightly.darkrefraction.com/gimp/). This is unstable software, please use it at your own risk.

A detailed list of changes in the development branch is available in [git](https://git.gnome.org/cgit/gimp/plain/NEWS).

</div>

<div id='mirrors'  markdown="1">
## FTP and Web Mirrors

Due to our server move in April (physical to virtual, into an environment that doesn't allow FTP access), we lost all existing mirrors. But we are now able to offer rsync access to download.gimp.org

If you are running one of the existing GIMP mirrors, or want to create a new one, please [contact us](/webmasters.html) to get your rsync credentials.

<dl class="download-mirror">
<dt>Brazil</dt>
<dd><a href="http://mirror.nbtelecom.com.br/gimp/">http://mirror.nbtelecom.com.br/gimp/</a> (web access)</dd>
<dd><a href="rsync://mirror.nbtelecom.com.br::gimp">rsync://mirror.nbtelecom.com.br::gimp</a> (rsync access)</dd>
<dt>Germany</dt>
<dd><a href="http://de-mirror.gimper.net/pub/gimp/">http://de-mirror.gimper.net/pub/gimp/</a> (web access)</dd>
<dd><a href="ftp://artfiles.org/gimp.org/gimp/">ftp://artfiles.org/gimp.org/gimp/</a></dd>
<dd><a href="http://artfiles.org/gimp.org/gimp/">http://artfiles.org/gimp.org/gimp/</a> (web access)</dd>
<dd><a href="ftp://ftp.fau.de/gimp/gimp/">ftp://ftp.fau.de/gimp/gimp/</a></dd>
<dd><a href="https://ftp.fau.de/gimp/gimp/">https://ftp.fau.de/gimp/gimp/</a> (web access)</dd>
<dd><a href="rsync://ftp.fau.de/gimp/">rsync://ftp.fau.de/gimp/</a> (rsync access)</dd>
<dt>Japan</dt>
<dd><a href="ftp://mirrors.go-parts.com/gimp/">ftp://mirrors.go-parts.com/gimp/</a></dd>
<dd><a href="http://mirrors.go-parts.com/gimp/">http://mirrors.go-parts.com/gimp/</a> (web access)</dd>
<dd><a href="rsync://mirrors.go-parts.com/mirrors/gimp/">rsync://mirrors.go-parts.com/mirrors/gimp/</a> (rsync access)</dd>
<dt>Russia</dt>
<dd><a href="ftp://mirrors-ru.go-parts.com/gimp/gimp/">ftp://mirrors-ru.go-parts.com/gimp/gimp/</a></dd>
<dd><a href="http://go-parts.com/mirrors-ru/gimp/gimp/">http://go-parts.com/mirrors-ru/gimp/gimp/</a> (web access)</dd>
<dd><a href="rsync://mirrors-ru.go-parts.com/mirrors/gimp/">rsync://mirrors-ru.go-parts.com/mirrors/gimp/</a> (rsync access)</dd>
<dt>South Africa</dt>
<dd><a href="http://gimp.afri.cc/pub/gimp/">http://gimp.afri.cc/pub/gimp/</a> (web access)</dd>
<dt>United Kingdom</dt>
<dd><a href="ftp://ftp.mirrorservice.org/sites/ftp.gimp.org/pub/gimp/">ftp://ftp.mirrorservice.org/sites/ftp.gimp.org/pub/gimp/</a></dd>
<dd><a href="http://www.mirrorservice.org/sites/ftp.gimp.org/pub/gimp/">http://www.mirrorservice.org/sites/ftp.gimp.org/pub/gimp/</a> (web access)</dd>
<dd><a href="rsync://rsync.mirrorservice.org/ftp.gimp.org/pub/gimp/">rsync://rsync.mirrorservice.org/ftp.gimp.org/pub/gimp/</a> (rsync access)</dd>
<dd><a href="ftp://mirrors-uk.go-parts.com/gimp/">ftp://mirrors-uk.go-parts.com/gimp/</a></dd>
<dd><a href="http://mirrors-uk.go-parts.com/gimp/">http://mirrors-uk.go-parts.com/gimp/</a> (web access)</dd>
<dd><a href="rsync://mirrors-uk.go-parts.com/mirrors/gimp/">rsync://mirrors-uk.go-parts.com/mirrors/gimp/</a> (rsync access)</dd>
<dt>United States</dt>
<dd><a href="http://gimp.galaxyverge.com/">http://gimp.galaxyverge.com/</a> (web access)</dd>
<dd><a href="http://gimper.net/downloads/pub/gimp/">http://gimper.net/downloads/pub/gimp/</a> (web access)</dd>
<dd><a href="http://mirror.hessmo.com/gimp/">http://mirror.hessmo.com/gimp/</a> (web access)</dd>
<dd><a href="http://gimp.mirrors.hoobly.com/pub/gimp/">http://gimp.mirrors.hoobly.com/pub/gimp/</a> (web access)</dd>
<dd><a href="ftp://mirrors-usa.go-parts.com/gimp/gimp/">ftp://mirrors-usa.go-parts.com/gimp/gimp/</a></dd>
<dd><a href="http://go-parts.com/mirrors-usa/gimp/gimp/">http://go-parts.com/mirrors-usa/gimp/gimp/</a> (web access)</dd>
<dd><a href="rsync://mirrors-usa.go-parts.com/mirrors/gimp/">rsync://mirrors-usa.go-parts.com/mirrors/gimp/</a> (rsync access)</dd>
</dl>


</div>

<script src="/js/platform.js"></script>

<script>

if ( platform.os.family.indexOf('Win') !== -1 && platform.os.family.indexOf('Phone') == -1 ){
    document.getElementById('win').style.display = 'block';
    document.getElementById('pOSTEST').innerHTML = 'Microsoft Windows.';
}else if ( platform.os.family.indexOf('OS X') !== -1 ){
    document.getElementById('mac').style.display = 'block';
    document.getElementById('pOSTEST').innerHTML = 'OS X.';
}else if ( platform.os.family.indexOf('iOS') !== -1 || platform.os.family.indexOf('Android') !== -1 ){
    document.getElementById('pOSTEST').innerHTML = platform.os.family + '.';
    var nope = "<br/><strong>This platform is not currently supported.</strong>";
    document.getElementById('pOSTEST').innerHTML += nope;
}else {
    document.getElementById('pOSTEST').innerHTML = platform.os.family + '.';
    document.getElementById('linux').style.display = 'block';
}

function render( os ){
    switch( this.id ) {
        case 'os_linux':
            document.getElementById('linux').style.display = 'block';
            document.getElementById('win').style.display = 'none';
            document.getElementById('mac').style.display = 'none';
            break;
        case 'os_win':
            document.getElementById('linux').style.display = 'none';
            document.getElementById('win').style.display = 'block';
            document.getElementById('mac').style.display = 'none';
            break;
        case 'os_mac':
            document.getElementById('linux').style.display = 'none';
            document.getElementById('win').style.display = 'none';
            document.getElementById('mac').style.display = 'block';
            break;
        default:
            document.getElementById('linux').style.display = 'block';
            document.getElementById('win').style.display = 'block';
            document.getElementById('mac').style.display = 'block';
            break;
    }
    return false;
}

document.getElementById('os_all').addEventListener("click", render );
document.getElementById('os_linux').addEventListener("click", render );
document.getElementById('os_win').addEventListener("click", render );
document.getElementById('os_mac').addEventListener("click", render );
</script>
