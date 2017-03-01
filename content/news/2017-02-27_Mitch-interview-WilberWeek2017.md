Title: An Interview with Michael Natterer, GIMP maintainer
Date: 2017-02-27
Category: News
Authors: Jehan
Status: draft
Summary: Michael Natterer gets interviewed by other GIMP developers

GIMP is [Free Software](https://www.gnu.org/philosophy/free-sw.html), but even before this, it is people: the ones who create it, the ones who create _with_ it… We don't have accurate statistics and we take pride on not gathering your data. Yet we know (through other websites that have logged partial statistics over the years) that this is a widely used piece of software, by millions of people around the world. So wouldn't it be neat to meet some of the individuals who make this project come alive?

Some people think there's a huge company behind GIMP. This is not the case.
GIMP has always been developed by a handful of random people scattered around the world. 
Most of them are volunteers and none of them work on it full-time.
As an insider myself, I've wanted to launch a series of interviews with the many awesome people I've met since I started contributing. So who better to start with than our own benevolent dictator, GIMP maintainer, and the biggest code contributor: **Michael Natterer**, aka "mitch".

This interview was held on Friday, February 3, 2017 at around 3AM in front of a fireplace and after a day of hacking at [Wilber Week](https://www.gimp.org/news/2017/01/18/wilberweek-2017-announced/).
With us were several team members, including Michael Schumacher (schumaml (S)) and Øyvind Kolås (pippin (P)), who also asked questions.

<figure>
<img src="{filename}images/mitch-interview/mitch-interview-950w.jpg" alt='Mitch, the man, the myth, the legend' width='950' height='566'>
<figcaption>
Mitch.  The man.  The myth.  The legend.<br>
The reason your commit probably got reverted.
</figcaption>
</figure>

_Jehan: Hello Mitch! In a few words, what's the close future of GIMP?_

**Mitch:** In 2.10, there is the GEGL port.
Then the GTK+3 port immediately after, which will go as fast as possible.
We don't plan many features during the GTK+3 port.

<br>
_J: What are your preferred features of 2.10?_

**M:** High bit depth, on-canvas filter previews… I don't actually remember the features of 2.8 [to compare] because I never use it.

_J: You use 2.10 instead?_

**M:** Yes.

_J: Do you use GIMP often?_

**M:** Mostly for testing what I implement, and also for making postcards I sell in my family business. That's the only thing I use it for.


## A maintainer ##

_J: How did you start hacking GIMP?_

**M:** There was this code that saved the user-assigned keyboard shortcuts for menu actions. The code had an escaping bug where you couldn't have a hyphen as an accelerator. So I wrote code for escaping the string. That was [my first GIMP
patch][firstpatch] in 1997 or 1998.

[firstpatch]: https://git.gnome.org/browse/gimp/commit/?id=2d442d4842e21c45959ed73a5d9ee3896a2ada08

<br>
_J: How did you become the maintainer?_

**M:** I killed the previous maintainer.
He is now in my cave in boxes.

<br>
_Schumaml: Have you ever met the [original authors][] (Spencer Kimball and Peter Mattis)?_

[original authors]: /about/prehistory.html

**M:** No. Has anyone?

_S: Have they ever contacted you?_

**M:** Yes, they sent me a few plugins which I pushed. Neon, photocopy and cartoon. It was around 10 years after they left the project, one of them comes to me and says _"Hey Mitch, I coded 3 plugins, here they are"_. Everything looked perfect so I just pushed them as-is, and they still exist.

These days, they've been reimplemented in GEGL, but the new versions give different results, so the old plugins are still in the menu.

<br>
_J: Why do you continue working on GIMP?_

**M:** That's a good question. *(laughs)*
I don't know. You guys, perhaps?
It can be really annoying sometimes.
Why do you guys continue?

_J: Me? It's fun._

**M:** It's fun yes but sometimes it's not fun and you do it anyway.

<figure>
<img src="{filename}images/mitch-interview/Montserrat_Pano_Gimpheros_Wilberheads.jpg" alt='GIMPers at Montserrat, España' width='950' height='343'>
<figcaption>
GIMPers at Montserrat.
</figcaption>
</figure>

<br>
_J: Where do you see GIMP 20 years from now?_

**M:** It will probably end up in a pile of bits rotting in some corner.  I may have been thinking the same thing twenty years ago, though, so you never know.


## A hacker ##

_J: What do you think of Free Software?_

**M:** It's the way to go, but you need to use the software which is available for a task, so for some tasks you have no choice but to use something that's not exactly free.

For example: *[pointing to nomis trying to make a label printer work on a GNU/Linux
distribution]* if you were using the closed-source driver for that, it would
work.

_*: (laughs)_

<br>
_J: What's your operating system, distribution, desktop…?_

**M:** Debian Unstable, GNOME 3.

_J: You often complain about all these though._

**M:** Because it's all shit.
Just because you have the least shitty [software] doesn't mean it's not all shit.
Like autotools. They are shit, but it's the best shit we have.
There is no software that isn't shit, except perhaps the most simple of software which does one task.

<br>
_J: What's your development environment or text editor of choice?_

**M:** Terminal & emacs.

<br>
_J: How do you like to hack?_

**M:** It depends. Sometimes I need silence and sometimes a crowded room.

<br>
_J: You are your own boss in a shop. But we see commits from you all the time. Are you hacking in your bookstore when you get free time and don't have to take care of your employees or customers?_

**M:** Sometimes, but very rarely. I'm mostly hacking in the evenings, or I commit something during the daytime that I worked on the night before until 2AM.
If I think _"I better go to sleep before I push this"_, then I'll wait until the next day when I'm awake to check it once more before I do.

But I don't have time to do 5-hour long patches during working hours.

_J: You don't sleep?_

**M:** I don't really sleep, no.

<br>
_S: What channels do you use to communicate on behalf or in the project?_

**M:** [IRC, and IRC.](https://xkcd.com/1782/)

<br>
_pippin: What was the first computer you programmed?_

**M:** It was a Schneider CPC, a variation of the Amstrad. At 15 or 16?

<br>
_S: How did you write your first hello world?_

**M:** In BASIC of course. My programming languages were BASIC, Assembly, Pascal, Modula-2, C, in that weird order. :) Plus some others at university nobody cares about. :)

<br>
_J: Do you code under the influence?_

**M:** Always! That's the only way to code.

<figure>
<a href='https://xkcd.com/323/' title='Apple uses automated schnapps IVs.'>
<img src='{filename}images/ballmer_peak.png' alt='XKCD Ballmer Peak' width='652' height='592'>
</a>
<figcaption>
Obligatory <a href='https://xkcd.com/323/' title='Apple uses automated schnapps IVs.'>XKCD</a>, by Randall Munroe (<a href='http://creativecommons.org/licenses/by-nc/2.5/' title='Creative Commons Attribution-NonCommercial 2.5 License'>Creative Commons By-NC 2.5</a>).
</figcaption>
</figure>


## GIMP: present ##

_J: So all software is shit, but in the list of shitty software, is GIMP not so bad?_

**M:** I hope so, but of course it's shitty.
We're just a handful of volunteers doing what companies with hundreds of (paid) people do.

_J: But sometimes we do things not so bad, right?_

**M:** Yes, but there is nobody to make sure of it.
It's not often that someone spends the time and effort to make a plugin perfect.
Sometimes it happens, but usually it gets dumped on us and that's it.
Ten years later, we look at the code again and say _"oh my god, this is complete garbage"_.
Very rarely do people maintain their code long term and we cannot seriously expect that to happen with everyone being a volunteer here.


<br>
_S: Is there something you'd like to do much more in the project, apart from coding?_

**M:** In the project? No, coding is fun. I'm happy that I don't have to do that much administrative work.

<br>
_S: When will 2.10 be released?_

**M:** Oh go away! The answer is _"go away!"_. Read my lips: **"go away"**. When it's ready.

_S: Do you expect it to be this year?_

**M:** Yes of course.

_J: So we have a promise!_

_*: (laughs)_


## GIMP: future ##

_S: There was this thing that the UI should use Python and the core should use C._

**M:** Python for the user interface. Horrible! Why?

_S: This is something we had discussed._

**M:** Yes but in the past people wanted to use JavaScript. The year before they wanted to use Java, the year before they wanted to use this, and the year after they want to use that. Now they're all gone.

Everyone who ever said _"I want to use this or that"_, and _"It's all shit, let's use JavaScript"_, none of them are still in the project, so…

_S: So you don't see any big changes regarding GIMP in the near future?_

**M:** In the near future definitely not because we need to get some releases out.
Unless, of course, there is a well-done patch that doesn't need weeks of discussion and back-and-forth negotiations on how things _should_ be done.

About using other languages: why not? There is Rust. There is maybe simpler stuff for doing user interfaces, but making such decisions for a codebase the size of GIMP is not something we can decide based on _"the latest hot stuff"_.


<br>
_S: Anything else you want to change?_

**M:** Yes a lot of stuff as long as _**I**_ don't have to do all the changes, because I really have enough things to do already *(laughs)*.

All contributors need to realize that if they do something really well, they will be in charge of that part.

_J: That's a very good point._

**M:** If you do it right, then you'll be in charge of the part you are doing right.
It always works like that.

_S: They don't need a blessing from you, right?_

**M:** I don't do blessings. *(laughs)*

<br>
_J: GTK+ comes from GIMP. What do you think of GTK+ now?_

**M:** They lost their minds, but they are also doing really good work. I don't really understand some of their decisions.

On the other hand, look at the mails we get. People say exactly the same about GIMP: _"Have the GIMP devs lost their minds?!?"_. I was involved with GTK+ for a long time and people thought that I had lost my mind, which was (and is) probably true. Bottom line is that **all is fine between GTK+ and GIMP**, I just reserve the right to complain for myself.

<br>
_S: So we will release GIMP 3 with GTK+3 or 4?_

**M:** They just branched for GTK+ 4.x, so that's not going to happen overnight.

_P: It won't hurt to suddenly have GIMP 4 instead of 3._

**M:** No it wouldn't. If they are done in a few weeks, we'd go for GIMP 4 right away. So why not. That would be cool. *(laughs)* Or GIMP 5!

_J: GIMP 10?_

**M:** GIMP X!

## Various rants ##

_S: If you happen to be in a conversation with people talking about GIMP, but they don't know that you are involved, do you come out as the GIMP principal developer?_

**M:** Only if they start talking utter bullshit, or if things simply need clarification. It has happened, of course. A guy wanted to convert me to GIMP once and I had to tell him: yeah you don't need to. It was in a non-hacker situation.

<br>
_J: Who is Wilber?_

**M:** Nobody knows. Wilber is a GIMP.

<br>
_S: What special device would you like to see GIMP on?_

**M:** This cool Microsoft thing ([Surface Studio PC](https://youtu.be/BzMLA8YIgG0)) where they have this hyped video online, and it looks super slick with touch and everything.
It's an ad like Apple used to do in the past and now Microsoft does it, which is a bit weird.
The official Microsoft YouTube video makes you want to have one of these things.

<br>
_S: What advice you would like to give to someone who would want to contribute?
   What to do and what not to do?_

**M:** Listen to advice and be persistent.

Don't give up because somebody says _"this patch isn't quite right"_, most of the time it won't be. My first commit to GIMP was reverted immediately.

_S: I think you also reverted my first._

**M:** Yes, that's kind of a tradition. Everybody fucks up on their first commit and it gets reverted. That's a good standard.

_S: So do not be afraid of errors?_

**M:** Yes exactly. Unless they jeopardize the fate of humanity or something. That's unlikely.

<br>
_*: Thanks for the interview._

**M:** You are welcome!

<figure>
<img src="{filename}images/mitch-interview/mitch-coding.jpg" alt='Mitch at work' width='650' height='650'>
</figure>

<small>Images in this post are courtesy of [antenne](http://antenne.springborn.net/) and used by permission.</small>
