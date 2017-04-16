Title: An Interview with Michael Schumacher, GIMP administrator
Date: 2017-04-19
Category: News
Authors: Jehan
Status: draft
Summary: Michael Schumacher gets interviewed by other GIMP developers

*This is the second of a series of interviews of various people surrounding GIMP development and community. See also the [interview of Mitch, GIMP maintainer](https://www.gimp.org/news/2017/03/01/an-interview-with-michael-natterer-gimp-maintainer/)*

GIMP is not only made by hard-core developers. The team also encourages less technical-enclined contributors. Michael Schumacher, *aka* Schumaml, is a good example of such a core contributor, as he had a very important impact over more than 10 years. Mostly known as the project administrator, nowadays he takes care of everything but coding: administrative tasks, management…

Furthermore Schumaml was recently named the maintainer of the 2.8 branch, the stable version of GIMP which only receives bugfixes, showing that it does not require a technically-focused mind to occupy important roles successfully.

This interview was held on Saturday, February 4, 2017, at about 00:27 AM in front of a fireplace and after a day of hacking at Wilber Week. With us were several team members, including Debarshi Ray (Rishi (R)), Øyvind Kolås (pippin (P)) and Simon Budig (Nomis (N)) who also asked questions.

<figure>
<img src="{filename}images/schumaml-interview/schumaml-interview-950w.jpg" alt='Schumaml, the tie-bearing GIMP office manager' width='950' height='566'>
<figcaption>
Schumaml, the tie-bearing GIMP office manager.
</figcaption>
</figure>

Jehan: Hello Michael. You are GIMP administrator, at least that's what everybody says.

Schumaml: That's what everybody says, yes.

J: How would you describe your contribution to the GIMP project?

S: I don't do much coding. It's just that so many people — from my perspective — do coding on GIMP already and have a better grasp of source code, how it is made up. So I don't think I can contribute much in that regard. So I try to do administrative stuff like handling the monetary aspect of the project like telling GNOME that we need money for events like Wilber Week, for LGM reimbursements…
<br/>
I also care about the bug reports we have. I try to have them categorized, have a proper status, make sure that they get replies, that we don't leave a bug report untended for a long time.
<br/>
And also I have administrative priviledges on GIMP web server, on mailing lists, and… what else. Do I forget anything? That's about it, yeah.

So I've been called the tie-bearing GIMP office manager. I even got a t-shirt with a printed tie because I've actually been in one meeting, at Libre Graphics Meeting wearing a shirt and a tie.

J: How long have you contributed?

S: I think I started somewhere between 2001 and 2004. The first contributions were probably getting GIMP buildable on MSYS, the minimal GNU build system on the Windows platform. Because I was annoyed that there were only GIMP builds for releases and not for every commit in between.

J: Was it like nightly builds?

S: No it was not like nightly builds. I just wanted to be able to have a current build **for** the Windows platform and also made **on** the Windows platform so that I could build on my Windows system I was using at the time. Yes just be able to follow GIMP development more closely than for example a build someone made for a development release.

J: So you mostly use GIMP on Windows?

S: Back more than 10 years ago, I did use Windows exclusively. So basically back then I had done the porting of GIMP to the Windows platform.

J: Do you use GIMP?

S: I use GIMP. Not as much as many other people but I use it to test many things of GIMP itself. I use it to edit photos I make. I don't publish many of them because when I'm editing them, I print them or I use them for some documentation work so it goes to a customer. I even use it on Windows still. But now my main platform is Linux.

J: What kind of job do you do?

S: I'm working for a company that used to be a part of Siemens. It's been carved out. It's still partially owned by Siemens. And we are selling communication systems. Nowadays this stuff is called "Communication Enabled Business Processes". Like everything which has to do with communication. Calling someone or texting someone or exchanging chats or whatever. And we are providing the software, the service and
the consulting.

J: Why do you contribute to GIMP?

S: It started with pure selfishness like being able to have the most current GIMP available to me. I believe in Free Software. I believe software should be available for everyone for every purpose. GIMP is a Free Software project. Around the time I got hooked up on GIMP, I got hooked up on Wikipedia which does the same to knowledge. So I kind of feel like — yeah well — I'm contributing to something that helps a lot of people all over the world. I think that's a good thing. And GIMP happens to be the project that was my first major project I contributed to at all. And I like it. It's kind of in-line with what I specialized at university. Like image synthesis, image manipulation, whatever. Kind of seem like a logical extension.

Rishi: What do you think of Michael Schumacher?

S: (laughs) The formula one driver?

R: Yeah.

S: First thing, you know about his current condition, like probably still in the coma or a vegetable. Surely I hope that he will get better. He probably won't make it to his former self but at least to a state that he can live his remaining life in a somewhat decent way.
He got famous when I was in the so-called German gymnasium, like I was in school. So it was a bit of an annoyance. I got the same nickname "Schumy" as he did. I didn't follow his career too closely but of course every time he won a race, I knew about it because I would be
congratulated at school.

pippin: Have you ever made use of sharing the name?

S: No I haven't. It got me an interview opportunity with a locale radio station because they were calling all people who beared the name "Michael Schumacher" and they were asking them "How hard does this affect your personal life? Has it ever affected you?". And I almost once had an appointment canceled because someone thought I was mocking him.

I've never used it, I've never abused it. And nowadays, or after the end of his professional racing career, it basically didn't matter anymore.

P: Any controversial theme you wish to be asked?

S: Like the fact that I would like to kill spammers?

Nomis: Not very controversial.

J: What do you want to see in GIMP?

S: Feature-wise, I'm quite OK with what GIMP is right now. I have to admit that some of the current stuff in GIMP development version is still above my head like I have no real concept yet of the difference of compositing and blending. Learning that it was 2 different things was quite useful. I hope that we can get the documentation of GIMP up-to-speed in time.  

I'm more concerned about the project management. As in how do we decide what new feature go in GIMP, how do we decide how they get into GIMP, how do we decide what GIMP development will look like, for instance post-2.10. Because you see it yourself, right now, our release cycles are much too long. Even the fact that we have actual release cycles is probably bad, because if you look at things like Twitter or whatever, they are constantly releasing. Like they just push new features out to the people and there is a constant review "this is working, this is not working".  So you are surprised by "ouh this does not work. Why have they changed it?".

But yeah the project is still a bit old-fashion in regard to releases. So we are trailing current development models. "Development models" is the term I use because I'm not even really familiar how you call this. I'm intrigued by the idea of having stable branches that can actually receive new features. I'm not quite sure if I want 2.10 constantly evolving. I would prefer to have 2.12. That's details.

J: How do you see GIMP in 20 years?

S: First thing in 20 years, I'll be 60 (laughs). So I'm not even sure how I see myself at that point. Well let's be selfish. I very much would like to see myself still part of the project in 20 years. I would still like to be able to see it as an image manipulation program. One of the major Free Software ones. And I have no idea at all how it will look like (laughs) because there is so much that can change. Especially even in the user interaction. How people interact with software might actually be the defining factor for how applications will look in 20 years.

J: What's **the** feature you are really waiting for?

S: The feature I'm really waiting for. It's not a feature of painting or image manipulation. It's about organization. This thing we want to do, plugin or ressource registry 2.0. Like properly built. Like really managed. Like not the hand-duplicate of an existing plugin. This thing we talked so much about, have so many great ideas, but always seem to lack the time to do it. This is the feature I would like to see.  

J: Do you contribute under the influence?

S: Yeah have a look at the 2.8.20 NEWS file, at the typos, which I did totally not notice. So now I prefer to not contribute under influence.  

J: Indeed you are now the maintainer of the 2.8 branch, or at least the releaser. If not mistaken, you took care of 2.8.18 and 2.8.20 releases. What can you say about this?

S: TODO: add answer!

J: This was a good interview.

S: Thank you for doing it.

J: And thank you for answering.

<small>Images in this post are courtesy of antenne and used by permission (<a class='cc' href='https://creativecommons.org/licenses/by-sa/4.0/' title='Creative Commons Attribution-ShareAlike 4.0 International'>cba</a>).</small>
