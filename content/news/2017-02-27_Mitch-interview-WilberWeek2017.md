Title: Interview of Michael Natterer, GIMP maintainer, during WilberWeek 2017
Date: 2017-02-27
Category: News
Authors: Jehan
Slug: interview-michael-natterer-wilberweek-2017
Summary: Michael Natterer gets interviewed by other GIMP developers

GIMP is [Free Software](https://www.gnu.org/philosophy/free-sw.html), but even before this, it is people: the ones who make it, the ones who create with it… We don't have accurate statistics and we take pride on not gathering your data. Yet we know for a fact (because there are various other websites who made partial statistics over the years) that this is a widely used piece of software, by millions of people around the world. So wouldn't it be neat to meet some of the individuals who make this project alive?

Some people expect a huge company behind. This is not the case. GIMP has always be developed by a random bunch of people scattered around the world, most of them volunteers.
As an insider myself, I've wanted to launch a serie of interviews with the many awesome people I met since I started contributing. So who better to start with than our own benevolent dictator, GIMP maintainer: **Michael Natterer**, alias "mitch".

This interview was held on Friday, February 3, 2017, at around 3AM, after a day of hacking at [Wilber Week](https://www.gimp.org/news/2017/01/18/wilberweek-2017-announced/), next to the fire place.
Next to us were also present several team members, amongst which Schumaml (S) and Pippin (P) also asked questions.

Jehan: Hello Mitch! In a few words, what's the close future of GIMP?

Mitch: In 2.10, there is the GEGL port, then the GTK+3 port immediately after, which
will go as fast as possible. We don't plan much features there, just the GTK+3 port.

Jehan: What are your preferred features of 2.10?

Mitch: High bit depth, on-canvas filter previews… I don't actually remember the
features of 2.8 because I never use it.

J: You use 2.10 instead?

M: Yes.

J: And you use GIMP often?

M: Mostly for trying what I implement, and also for making postcards I sell in my
family business. That's the only thing I use it for. I mean… whenever I have to
manipulate a pixel image, and not being an artist.

## A maintainer ##

J: How did you start hacking GIMP?

M: There is this code that saves the user-assigned keyboard shortcuts for menu
actions. And that code had an escaping bug that you couldn't have an hyphen as
an accelerator. So I made code for escaping the string. That was my first GIMP
patch in… 1997 or 1998.

J: How did you become the maintainer?

M: I killed the previous maintainer.
He is now in my cave in boxes.

Schumaml: Have you ever met the original authors (Spencer Kimball and Peter Mattis)?

M: No. Has anyone?

S: Have they ever contacted you?

M: Yes they sent me a few plugins which I pushed. But it's like 10 years ago, or
so. Neon, photocopy and cartoon. It's like, 10 years later, one of them come
and is like "hey Mitch, I coded 3 plugins, here they are". Everything looks
perfect, so I just pushed them as-is and they still exist.

But the GEGL version gives different results. So that's why we still have
them in the menu.

J: Why do you continue working on GIMP?

M: that's a good question. (laugh)
   I don't know. You guys, perhaps?
   Because it's annoying sometimes.
   Why do you continue?

J: Me? It's fun.

M: It's fun yeah. But only if it's fun. Sometimes it's not fun but you do it
anyway. So do you.

J: How do you see GIMP in 20 years from now?

M: It will probably end up in a pile of bits roting in some corner. But 20 years
ago, I was probably thinking the same. So you never know.

## A hacker ##

J: What do you think of Free Software?

M: It's the way to go. But I mean, everybody uses the software which is
available, so… for some tasks, you use what is available. If it's not Free, you
have no choice but using the other one.

For example: [showing nomis trying to make a label printer work on a GNU/Linux
distribution] if you would be using the closed-source driver of that, it would
work.

*: (laughs)

J: What's your operating system, distribution, desktop…

M: Debian Unstable, GNOME 3.

J: You often complain about all these though.

M: Because it's all shit. Only because you have the least shitty doesn't mean
it's not all shit. Like autotools. They are shit but it's the best shit there
is. Of course it could be much better. There is no software that is not shit. I
mean except perhaps the most simple of all software, which does that one task.

J: What's your development environment or text editor of choice?

M: Terminal & emacs.

J: How do you like to hack?

M: Depends. Sometimes I need silence, sometimes a crowded city.

J: You are your own boss in a bookstore. But we see commits from you all the
time. So are you hacking in your bookstore when you get free times and don't have to take care of
your employees or customers?

M: No. Sometimes. But really rarely. It's mostly in the evenings. Or I commit
something during daytime, like after 5 minutes looking at it awake after doing
it the night before at 2 O'clock. Then I think "I better go to sleep before I
push this". Then I push it on the next day. But I don't have time to do like
5-hour long patches during worktime.

J: You don't sleep?

M: I don't really sleep, no.

S: What channels do you use to communicate on behalf or in the project?

M: [IRC. And IRC.](https://xkcd.com/1782/)

Pippin: What was the first computer you programmed?

M: It was a Schneider CPC, a variation of the Armstrad.
   At 15 or 16?

S: How did you write your first hello world?

M: In Basic of course.
   My programming languages were basic, assembler, pascal, modula2, C, in that weird order :)
   Plus some others at university nobody cares about :)

J: Do you code under the influence?

M: Always! That's the only way to code.

## GIMP: present ##

J: All software are shit, but in the shitty software list, is GIMP a not too
shitty one?

M: I hope so. But it's of course shitty. Just like a handful of people doing
what other companies do like with 100 people. It can only be really weird in
many places.

J: But we do something sometimes not too bad, right?

M: Yes, we do something sometimes not too bad. But there is nobody who makes
sure of it. There is nobody who puts like 2 months into a plugin to make it
perfect. It happens, but then they dump it on us and that's it. And 10 years
later, we see it and "oh my god, this is complete garbage".

S: Is there something you'd like to do much more in the project, apart coding?

M: In the project? No. Coding is fun. Other things are not so fun if it comes to
software. So I'm happy that somebody does the office work.

S: When will 2.10 be released?

M: Oh go away! The answer is "go away!". Read my lips: "go away". When it's
ready.

S: Do you expect it to be this year.

M: Yes of course.

J: So we have a promise!

*: (laughs)

## GIMP: future ##

S: There was this thing that the UI should use Python and the core should use C.

M: Python for the user interface. Horrible! Why?

S: This is something we had discussed.

M: Yeah but in the past, people wanted to use javascript, the year before they
wanted to use Java, the year before they wanted to use this, and the year after
they want to use that, and the next year they want to use that. And they are all
gone, everybody who ever said "I want to use this or that, and it's all shit,
let's use javascript". None of them is still in the project, so… it gets boring.

S: So you don't see any big changes regarding GIMP in the near future?

M: In the near future definitely not, because we have to get some releases out.
Using other languages? Why not? There is Rust. There is… maybe simpler stuff for
doing UI stuff. But if that's actually working… I mean: look at this javascript
mess. Is that really better? Just because it's easier? Easier just means that
more clueless people can write code. And they are clueless enough already. So it
doesn't make it better by making it easier. Arrogant but true.

S: Anything else you want to change?

M: Yes a lot of stuff if I don't have to change them because I really have
enough things to do (laughs).
So you go organize it better.
You can be maintainer of whatever subpart, please. Please. Take away the work
from me. The contributors need to realize that if you do something really well,
they will be in charge of the part they do well. Nobody realizes that.

J: That's a very good point.

M: If they do it right, then they'll be in charge of the part they are doing
right. It always works like that.

S: They do not need a blessing from you, right?

M: I don't do blessings. (laughs)

J: GTK+ comes from GIMP. What do you think of GTK now?

M: They lost their mind but they are also doing really good work. Some of the
decisions, you cannot understand. Because… is GIMP the only application left in
the GTK world? Everything else is *apps* and buttons and touch. Is there any other
complex GTK application? Like complex-complex-complex like GIMP?

S: So we will release GIMP 3 with GTK+3 or 4?

M: If we go further, we go further, but they just branched to GTK+4 anyway.
That's not going to happen overnight.

P: It won't harm to suddenly have GIMP 4 instead of 3.

M: Yeah no, if they are done in a few weeks, we'd go for GIMP 4 right away. So
why not. That would be cool. (laughs) Or GIMP 5!

J: GIMP 10?

M: GIMP X!

## Various rants ##

S: If you happen to be in a conversation with people talking about GIMP, but do not
know that you are involved, do you come out as GIMP principal developer.

M: Only if they start talking utter-bullshit. It has happened before of course.
   A guy wanted to convert me to GIMP once and I had to tell him: yeah you don't need
   to. In a non-computer situation, like in private.

J: Who is Wilber?

M: Nobody knows. Wilber is a GIMP.

S: What special device would you like to see GIMP on.

M: This cool Microsoft thing ([Surface Studio PC](https://youtu.be/BzMLA8YIgG0)) where they have this video online. It looks like
super slick, with touch and everything. Videos like Apple used to do, now it's
long gone. Now Microsoft does that. Isn't that sad?
The official Microsoft youtube video makes you want to have one of these things.

S: What advice you would like to give to someone who would want to contribute?
   What to do and what not to do?

M: Listen to advices and be persistent.
   Don't give up because someone says "this patch isn't quite right". Because
   it's most often not quite right. My first commit to GIMP was reverted
   immediately.

S: I think you also reverted my first.

M: Yes, that's kind of a tradition. Everybody fucks up on their first commit and
gets reverted. That's good standard.

S: So do not be afraid of errors?

M: Yes exactly. Unless they jeopardize the fate of humanity or something. That's unlikely.

*: Thanks for the interview.

M: You are welcome.
