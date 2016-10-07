/*
 * platform-display.js
 *
 * Used on /downloads/ to change download display blocks
 * based on detected platform.
 *
 * Pat David, 2016
 */

    if ( platform.os.family.indexOf('Win') !== -1 && platform.os.family.indexOf('Phone') == -1 ){
        // Windows, _not_ Phone
        document.getElementById('win').style.display = 'block';
        document.getElementById('mac').style.display = 'none';
        document.getElementById('linux').style.display = 'none';
        document.getElementById('pOSTEST').innerHTML = 'Microsoft Windows.';
    }else if ( platform.os.family.indexOf('OS X') !== -1 ){
        // OS X
        document.getElementById('win').style.display = 'none';
        document.getElementById('mac').style.display = 'block';
        document.getElementById('linux').style.display = 'none';
        document.getElementById('pOSTEST').innerHTML = 'OS X.';
    }else if ( platform.os.family.indexOf('iOS') !== -1 || platform.os.family.indexOf('Android') !== -1 ){
        // iOS or Android
        document.getElementById('pOSTEST').innerHTML = platform.os.family + '.';
        var nope = "<br/><strong>This platform is not currently supported.</strong>";
        document.getElementById('pOSTEST').innerHTML += nope;
        document.getElementById('win').style.display = 'none';
        document.getElementById('mac').style.display = 'none';
        document.getElementById('linux').style.display = 'none';
    }else {
        // Everything else (assuming *nix-type)
        document.getElementById('pOSTEST').innerHTML = platform.os.family + '.';
        document.getElementById('win').style.display = 'none';
        document.getElementById('mac').style.display = 'none';
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
