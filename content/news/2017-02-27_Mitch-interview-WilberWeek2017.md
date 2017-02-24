Title: Interview of Michael Natterer, GIMP maintainer, during WilberWeek 2017
Date: 2017-02-27
Category: News
Authors: Jehan
Slug: interview-michael-natterer-wilberweek-2017
Summary: Michael Natterer gets interviewed by other GIMP developers

GIMP is [Free Software](https://www.gnu.org/philosophy/free-sw.html), but even before this, it is people: the ones who create it, the ones who create _with_ it… We don't have accurate statistics and we take pride on not gathering your data. Yet we know (because there are various other websites who have logged partial statistics over the years) that this is a widely used piece of software, by millions of people around the world. So wouldn't it be neat to meet some of the individuals who make this project come alive?

Some people expect a huge company behind GIMP. This is not the case. GIMP has always been developed by a random bunch of people scattered around the world (just a handful at a time), most of them volunteers, and none full-time.
As an insider myself, I've wanted to launch a series of interviews with the many awesome people I've met since I started contributing. So who better to start with than our own benevolent dictator, GIMP maintainer, also the biggest code contributor: **Michael Natterer**, aka "mitch".

This interview was held on Friday, February 3, 2017, at around 3AM, after a day of hacking at [Wilber Week](https://www.gimp.org/news/2017/01/18/wilberweek-2017-announced/), next to the fire place.
Next to us were several team members, amongst which Michael Schumacher (schumaml (S)) and Øyvind Kolås (pippin (P)) also asked questions.

<figure>
<img src="{filename}images/mitch-interview/mitch-interview-950w.jpg" alt='Mitch, the man, the myth, the legend'>
<figcaption>
Mitch.  The man.  The myth.  The legend.<br>
The reason your commit probably got reverted.
</figcaption>
</figure>

_Jehan: Hello Mitch! In a few words, what's the close future of GIMP?_

**Mitch:** In 2.10, there is the GEGL port, then the GTK+3 port immediately after, which will go as fast as possible. We don't plan many features there, just the GTK+3 port.

_J: What are your preferred features of 2.10?_

**M:** High bit depth, on-canvas filter previews… I don't actually remember the features of 2.8 because I never use it.

_J: You use 2.10 instead?_

**M:** Yes.

_J: And you use GIMP often?_

**M:** Mostly for trying what I implement, and also for making postcards I sell in my family business. That's the only thing I use it for. I mean… whenever I have to manipulate a pixel image, and not being an artist.


## A maintainer ##

_J: How did you start hacking GIMP?_

**M:** There is this code that saves the user-assigned keyboard shortcuts for menu actions. That code had an escaping bug that you couldn't have a hyphen as an accelerator. So I wrote code for escaping the string. That was [my first GIMP
patch][firstpatch] in… 1997 or 1998.

[firstpatch]: https://git.gnome.org/browse/gimp/commit/?id=2d442d4842e21c45959ed73a5d9ee3896a2ada08

_J: How did you become the maintainer?_

**M:** I killed the previous maintainer.
He is now in my cave in boxes.

_Schumaml: Have you ever met the [original authors][] (Spencer Kimball and Peter Mattis)?_

[original authors]: /about/prehistory.html

**M:** No. Has anyone?

_S: Have they ever contacted you?_

**M:** Yes, they sent me a few plugins which I pushed. Neon, photocopy and cartoon. It's like 10 years later, one of them comes and says _"hey Mitch, I coded 3 plugins, here they are"_. Everything looks perfect, so I just pushed them as-is and they still exist.

The GEGL version gives different results, though. So that's why we still have
them in the menu.

_J: Why do you continue working on GIMP?_

**M:** that's a good question. *(laughs)*
   I don't know. You guys, perhaps?
   Because it's annoying sometimes.
   Why do you continue?

<figure>
<img src="{filename}images/mitch-interview/Montserrat_Pano_Gimpheros_Wilberheads.jpg" alt='GIMPers at Montserrat, Espana'>
<figcaption>
GIMPers at Montserrat.
</figcaption>
</figure>

_J: Me? It's fun._

**M:** It's fun yeah. But only if it's fun. Sometimes it's not fun but you do it
anyway.

_J: How do you see GIMP 20 years from now?_

**M:** It will probably end up in a pile of bits rotting in some corner. But 20 years ago, I was probably thinking the same. So you never know.



## A hacker ##

_J: What do you think of Free Software?_

**M:** It's the way to go. I mean, everybody uses the software which is
available, so… for some tasks, you use what is available. If it's not Free, you
have no choice but to use it.

For example: *[showing nomis trying to make a label printer work on a GNU/Linux
distribution]* if you were using the closed-source driver of that, it would
work.

_*: (laughs)_

_J: What's your operating system, distribution, desktop…_

**M:** Debian Unstable, GNOME 3.

_J: You often complain about all these though._

**M:** Because it's all shit. Because you have the least shitty doesn't mean
it's not all shit. Like autotools. They are shit but it's the best shit there
is. Of course it could be much better. There is no software that isn't shit. I
mean except perhaps the most simple of all software, which does that one task.

_J: What's your development environment or text editor of choice?_

**M:** Terminal & emacs.

_J: How do you like to hack?_

**M:** Depends. Sometimes I need silence, sometimes a crowded city.

_J: You are your own boss in a bookstore. But we see commits from you all the time. So are you hacking in your bookstore when you get free times and don't have to take care of your employees or customers?_

**M:** No. Sometimes, but very rarely. It's mostly in the evenings. Or I commit
something during the daytime, after 5 minutes of looking at it awake after doing
it the night before at 2AM. I think _"I better go to sleep before I
push this"_. Then I push it on the next day. But I don't have time to do 
5-hour long patches during working hours.

_J: You don't sleep?_

**M:** I don't really sleep, no.

_S: What channels do you use to communicate on behalf or in the project?_

**M:** [IRC. And IRC.](https://xkcd.com/1782/)

_pippin: What was the first computer you programmed?_

**M:** It was a Schneider CPC, a variation of the Amstrad.
   At 15 or 16?

_S: How did you write your first hello world?_

**M:** In Basic of course. My programming languages were basic, assembler, pascal, modula2, C, in that weird order. :) Plus some others at university nobody cares about. :)

_J: Do you code under the influence?_

**M:** Always! That's the only way to code.

<figure>
<a href='https://xkcd.com/323/' title='Apple uses automated schnapps IVs.'><img src='{filename}images/ballmer_peak.png' alt='XKCD Ballmer Peak'></a>
<figcaption>
Obligatory <a href='https://xkcd.com/323/' title='Apple uses automated schnapps IVs.'>XKCD</a>, by Randall Munroe (<a href='http://creativecommons.org/licenses/by-nc/2.5/' title='Creative Commons Attribution-NonCommercial 2.5 License'>Creative Commons By-NC 2.5</a>).
</figcaption>
</figure>


## GIMP: present ##

_J: All software are shit, but in the shitty software list, is GIMP a not too shitty one?_

**M:** I hope so. But of course it's shitty. Just a handful of people doing
what other companies do with 100 people. It can only be really weird in
many places.

_J: But sometimes we do things not so bad, right?_

**M:** Yes, we sometimes do things not so bad. But there is nobody who makes
sure of it. There is nobody who puts like 2 months into a plugin to make it
perfect. It happens, but then they dump it on us and that's it. And 10 years
later, we see it and _"oh my god, this is complete garbage"_.

_S: Is there something you'd like to do much more in the project, apart from coding?_

**M:** In the project? No. Coding is fun. Other things are not so fun if it comes to software. So I'm happy that somebody does the office work.

_S: When will 2.10 be released?_

**M:** Oh go away! The answer is _"go away!"_. Read my lips: **"go away"**. When it's ready.

_S: Do you expect it to be this year._

**M:** Yes of course.

_J: So we have a promise!_

_*: (laughs)_



## GIMP: future ##

_S: There was this thing that the UI should use Python and the core should use C._

**M:** Python for the user interface. Horrible! Why?

_S: This is something we had discussed._

**M:** Yeah but in the past, people wanted to use javascript, the year before they wanted to use Java, the year before they wanted to use this, and the year after they want to use that, and the next year they want to use that. And they are all gone. Everybody who ever said _"I want to use this or that, and it's all shit, let's use javascript"_. None of them are still in the project, so… it gets boring.

_S: So you don't see any big changes regarding GIMP in the near future?_

**M:** In the near future definitely not, because we have to get some releases out.

Using other languages? Why not? There is Rust. There is… maybe simpler stuff for
doing UI. If that's actually working… I mean, look at this javascript
mess. Is that really better? Just because it's easier? Easier just means that
more clueless people can write code, and they are clueless enough already. So it
doesn't make it better by making it easier. Arrogant but true.

_S: Anything else you want to change?_

**M:** Yes a lot of stuff if _I_ don't have to change them because I really have
enough things to do *(laughs)*.

So you go organize it better.

You can be maintainer of whatever subpart, please. Please. Take away the work
from me. The contributors need to realize that if you do something really well,
they will be in charge of the part they do well. Nobody realizes that.

_J: That's a very good point._

**M:** If they do it right, then they'll be in charge of the part they are doing
right. It always works like that.

_S: They don't need a blessing from you, right?_

**M:** I don't do blessings. *(laughs)*

_J: GTK+ comes from GIMP. What do you think of GTK now?_

**M:** They lost their mind but they are also doing really good work. Some of the decisions, you can't understand. Because… is GIMP the only application left in the GTK world? Everything else is *apps* and buttons and touch. Is there any other complex GTK application? Complex-complex-complex like GIMP?

_S: So we will release GIMP 3 with GTK+3 or 4?_

**M:** If we go further, we go further. They just branched to GTK+4 anyway.
That's not going to happen overnight.

_P: It won't harm to suddenly have GIMP 4 instead of 3._

**M:** Yeah no, if they are done in a few weeks, we'd go for GIMP 4 right away. So why not. That would be cool. (laughs) Or GIMP 5!

_J: GIMP 10?_

**M:** GIMP X!

## Various rants ##

_S: If you happen to be in a conversation with people talking about GIMP, but they don't know that you are involved, do you come out as the GIMP principal developer._

**M:** Only if they start talking utter bullshit. It has happened before, of course. A guy wanted to convert me to GIMP once and I had to tell him: yeah you don't need to. In a non-computer situation, like in private.

_J: Who is Wilber?_

**M:** Nobody knows. Wilber is a GIMP.

_S: What special device would you like to see GIMP on._

**M:** This cool Microsoft thing ([Surface Studio PC](https://youtu.be/BzMLA8YIgG0)) where they have this video online. It looks super slick, with touch and everything. Videos like Apple used to do, now it's long gone. Now Microsoft does that. Isn't that sad?

The official Microsoft youtube video makes you want to have one of these things.

_S: What advice you would like to give to someone who would want to contribute?
   What to do and what not to do?_

**M:** Listen to advice and be persistent.

Don't give up because someone says _"this patch isn't quite right"_. Because it's most often not quite right. My first commit to GIMP was reverted immediately.

_S: I think you also reverted my first._

**M:** Yes, that's kind of a tradition. Everybody fucks up on their first commit and gets reverted. That's good standard.

_S: So do not be afraid of errors?_

**M:** Yes exactly. Unless they jeopardize the fate of humanity or something. That's unlikely.

_*: Thanks for the interview._

**M:** You are welcome!

<figure>
<img src="{filename}images/mitch-interview/mitch-coding.jpg" alt='Mitch at work'>
</figure>

<small>Images in this post are courtesy of [antenne](http://antenne.springborn.net/) and used by permission.</small>
