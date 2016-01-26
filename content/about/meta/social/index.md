Title: Social Aggregator Testing
Date: 2015-07-29T14:40:35-05:00
Modified: 2015-08-27T12:06:35-05:00
Author: Pat David
Summary: A social aggregator experiment
lang: en

I'll be testing some stuff here.
This page is not guaranteed to work.  At all.
Poke patdavid if there's a problem.

Here are links to the GIMP accounts on each social network:

* [Google+][]
* [Facebook][] 
* [Twitter][]

[Google+]: https://plus.google.com/+gimp/posts 
[Facebook]: https://www.facebook.com/gimpofficial/
[Twitter]: https://twitter.com/@gimp_official

Here are the services that I currently have working:

* [Facebook (Posts _by_ GIMP)](#FBOut)  
    <small>Because FB hates me, apparently _shares_ made by the page
    don't show up here (sharing content from others).  I'm investigating...</small>
* [Facebook (Posts _to_ GIMP)](#FBTagged)
* [Twitter (Posts _by_ GIMP)](#TwitterOut)
* [Twitter (Posts _mentioning_ GIMP)](#TwitterMentions)

<div id='FBOut' markdown=1>
## Facebook (GIMP Posts)
</div>

<hr/>

<div id='FBTagged' markdown=1>
## Facebook (GIMP Tagged)
</div>

<hr/>

<div id='TwitterOut' markdown=1>
## Twitter (GIMP Posts)
</div>

<hr/>

<div id='TwitterMentions' markdown=1>
## Twitter (GIMP Mentions)
</div>

<style>
#FBOut figure,
#FBTagged figure {
    max-width: 34rem;
    max-width: 50%;
}
.FBData, .TData {
    margin-bottom: 3rem;
    font-size: 0.85rem;
}
.FBData img, .TData img {
    max-width: 50%;
}
.FBDate, .TDate {
    display: block;
    margin: 0 auto;
    max-width: 34rem;
    border-bottom: dashed 1px #ccc;
    margin-bottom: 0.5rem;
}
.FBMore, .TMore {
    text-align: right;
    max-width: 34rem;
    margin: 0 auto;
    font-size: 0.75rem;
    margin-top: -1rem;
}
#FBTagged, #TwitterMentions {
    background-color: #f7f7f7;
}
</style>

<script type='text/javascript'>
function doFB(rsp, type){
    console.log( rsp );
    console.log( type );

    for( var i = 0; i < rsp.data.length; i++ ){
        var thisPost = rsp.data[i];

        var post = document.createElement('div');
        post.className = 'FBData';

        if( thisPost.updated_time ){
            var d = new Date( thisPost.updated_time );
            var fblink = document.createElement('a');

            fblink.href = "https://www.facebook.com/permalink.php?story_fbid=";
            fblink.href += thisPost.id.split('_')[1] + "&id=";
            fblink.href += thisPost.id.split('_')[0];
            
            var dated = document.createElement('span');
            dated.className = 'FBDate';

            if( type == 'posts' ){
                fblink.innerHTML = "FB Post ";
            }else if(type == 'tagged' ){
                //fblink.innerHTML = "FB Tagged ";
            }

            fblink.innerHTML += d.getFullYear() +'-'+ ("0" + (d.getMonth() + 1)).slice(-2) +'-';
            fblink.innerHTML += ("0" + d.getDate()).slice(-2);

            if( type == 'tagged' && thisPost.from ){
                fblink.innerHTML += " by "+ thisPost.from.name;
                fblink.innerHTML += " <i class='fa fa-facebook-official' style='float:right;font-size:1.25rem;'></i>";
            }else if( type == 'posts' ){
                fblink.innerHTML += " <i class='fa fa-facebook-official' style='float:right;font-size:1.25rem;'></i>";
            }

            dated.appendChild( fblink );
            post.appendChild( dated );

        }

        if( thisPost.message ){
            var msg = document.createElement('p');
            msg.innerHTML = thisPost.message.replace(/(?:\r\n|\r|\n)/g, '<br />');
            post.appendChild( msg );
        }else if( thisPost.story ){
            var msg = document.createElement('p');
            msg.innerHTML = thisPost.story;
            post.appendChild( msg );
        }

        if( thisPost.full_picture ){
            var fig = document.createElement('figure');
            var pic = document.createElement('img');

            pic.src = thisPost.full_picture;

            if( thisPost.type == 'link' && thisPost.name && thisPost.link ){
                var thislink = document.createElement('a');
                thislink.href = thisPost.link;
                thislink.appendChild( pic );
                fig.appendChild( thislink );
                post.appendChild( fig );
            }else{
                fig.appendChild( pic );
                post.appendChild( fig );
            }
        }

        if( thisPost.type == 'link' && thisPost.name && thisPost.link ){
            var sharelink = document.createElement('p');
            var linker = document.createElement('a');
            linker.href = thisPost.link;
            linker.innerHTML = thisPost.name;

            sharelink.appendChild( linker );
            post.appendChild( sharelink );
                
        }

        if( fblink ){
            var readmore = document.createElement('div');
            readmore.className = 'FBMore readmore';
            var morelink = document.createElement('a');
            morelink.href = fblink.href;
            morelink.innerHTML = 'Read More &rarr;';
            readmore.appendChild( morelink );
            post.appendChild( readmore );
        }


        if( type == 'posts' ){
            document.getElementById('FBOut').appendChild( post );
        }else if( type == 'tagged' ){
            document.getElementById('FBTagged').appendChild( post );
        }
    }
}

function doFBPosts( rsp ){
    doFB(rsp, 'posts');
}

function doFBTagged( rsp ){
    doFB(rsp, 'tagged');
}

function doTwitter( rsp, type ){
    console.log( rsp );
    console.log( type );

    for( var i = 0; i < rsp.statuses.length; i++ ){

    var thisPost = rsp.statuses[i];
    var post = document.createElement('div');
    post.className = 'TData';

    if( thisPost.created_at ){
        var d = new Date( thisPost.created_at );
        var link = document.createElement('a');

        link.href='https://twitter.com/GIMP_Official/status/' + thisPost.id_str;

        var dated = document.createElement('span');
        dated.className = 'TDate';
        link.innerHTML = "";
        link.innerHTML += d.getFullYear() +'-'+ ("0" + (d.getMonth() + 1)).slice(-2) +'-';
        link.innerHTML += ("0" + d.getDate()).slice(-2);
        link.innerHTML += " by ";

        if( thisPost.user.name !== thisPost.user.screen_name ){ 
            link.innerHTML += thisPost.user.name +' ';
        }

        if( thisPost.user.screen_name !== 'GIMP_Official' ){
            link.innerHTML += "<span style='color: #666;'>@"+ thisPost.user.screen_name +"</span>";
        }

        link.innerHTML += " <i class='fa fa-twitter' style='float:right;font-size:1.25rem;'></i>";

        dated.appendChild( link );
        post.appendChild( dated );

    }

    if( thisPost.text ){
        var msg = document.createElement('p');
        msg.innerHTML = thisPost.text.replace(/(?:\r\n|\r|\n)/g, '<br />');

        if( thisPost.entities.media ){
            for( var j = 0; j < thisPost.entities.media.length; j++ ){
                var thisMedia = thisPost.entities.media[j];
                if( thisMedia.type == 'photo' ){
                    msg.innerHTML += "<br><img src='" + thisMedia.media_url_https + "' alt='Twitter Image'>";
                }
            }
        }

        post.appendChild( msg );

    }
    

    if( type == 'posts' ){
        document.getElementById('TwitterOut').appendChild( post );
    }else if( type == 'mentions' ){
        document.getElementById('TwitterMentions').appendChild( post );
    }
    
    }
}

function doTwitterPosts( rsp ){
    doTwitter( rsp, 'posts' );
}

function doTwitterMentions( rsp ){
    doTwitter( rsp, 'mentions' );
}


</script>

<!--
Thanks to twitter I had to host a bridge on pixls.us to query the information using curl.
This _could_ be re-written to use Python and possibly host on pentagon, but this should
be fine for right now.
-->
<script async src="https://pixls.us/gt/fb.php?callback=doFBPosts"></script>
<script async src="https://pixls.us/gt/fbtagged.php?callback=doFBTagged"></script>

<script async src="https://pixls.us/gt/gt.php?callback=doTwitterPosts"></script>
<script async src="https://pixls.us/gt/gtto.php?callback=doTwitterMentions"></script>
