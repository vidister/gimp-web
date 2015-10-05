Title: How To Set Your Tile Cache
Date: 2004
Modified: 2015-10-05T10:19:55-05:00
Author: Pat David


## or Tile Cache Recommendations

_**Quick summary** for those who do not want to read all this: if your system has good swapping behavior (like most GNU/Linux systems) and if you have enough virtual memory (swap), then set the tile cache size as high as possible. If not, then set it to about 80% of the available RAM on your system. If you are not satisfied with this quick advice, then keep on reading..._

Image processing can require a lot of memory. GIMP uses the operating system services to handle memory, up to a given point, past which it uses its own system so it does not eat all system memory resources. This system consists in sending old data to files in the disk. The decision point is what Tile Cache determines, the limit of operating system resources to use, and is measured in Bytes (or multiples, like MegaBytes). It does not include GIMP's own memory, just the space required for the image data.

A low value means that GIMP sends data really quickly to disk, not making real use of the avaliable RAM and making the disks work without real reason. A too high value, and the other applications start to have less system resources forcing them to swap space, which is making the disks work too, or maybe some will even get killed or start to malfunction due lack of RAM.

### How to choose a number for Tile Cache?

There are some ways to decide what value to use as Tile Cache, as well as some tricks:

*   Forget about this and hope the default works. It worked when computers had few RAM and people just tried to make small images with GIMP while running one or two applications each time. If you want something easy and only use GIMP to make screenshoots and some logos, probably the best solution.
*   Ask someone to do it for you, which in the case of a computer serving multiple users at the same time can be a good idea, that way the administrator and other users do not get mad at you for abusing the machine, nor you get a badly underperfoming GIMP. If it is your machine and a single user at a given time, it could mean money, or drinks, as price for the service. ;]
*   Start changing the value a bit each time and check that it goes faster and faster with each increase, but the systems does not complain about lack of memory. Be forewarned that sometimes lack of memory ends with some applications being killed to make space for the others.
*   Do some simple maths and calculate a viable value. Maybe you will have to tune it later, but maybe you have to tune it anyway with the other previous methods. At least you know what is happening and can get the best from your computer.

### What number to use for Tile Cache?

Let's guess you prefer the last option, and get a nice value to start with. First, you need to get some data about your computer. This data is the RAM installed, the operating system's swap space avaliable and a general idea about the speed of the disks that store the operating system's swap and the directory used for GIMP's swap. You do not need to do disk tests, nor check the RPM of them, the thing is to see which one seems clearly faster or slower or all similar. Remember you can change GIMP's swap directory in <Toolbox> -> File -> Preferences -> Folders -> Swap Dir.

Next thing to do is to see how much resources you require for other apps you want to run at the same time than GIMP. So start all your tools and do some work with them, except GIMP of course, and check the usage. You can use applications like free or top, depends in what OS and what environment you use. The numbers you want is the memory left, including file cache. Modern UNIX keep a really small area free, to be able to keep big file and buffer caches. GNU/Linux's free does the maths for you, check the column that says "free", and the line "-/+ buffers/cache". Note down also the free swap.

Now time for decisions and simple maths. Basically the concept is to decide if you want to base all Tile Cache in free RAM, or free RAM plus operating system free swap:

1.  Do you change applications a lot? Or keep working in GIMP for a long time? If you stay long times in GIMP, you can consider free RAM plus free swap as avaliable, or not, you have to check following points. If unsure about that times being long or not, check next steps too. If you are sure you switch all the apps every few time, only count free RAM and just go to final decision, no more things to check.
2.  Does operating system swap live in the same physical disk than GIMP swap? If so, use RAM and swap, as this way you will try to keep disk access over a fixed, compact, area for more time. Otherwise check next.
3.  The disk that holds the swap is faster or same speed than the disk that holds GIMP's swap? If slower, take only free RAM, if faster or similar, use free RAM and swap. This way we avoid a slow disk when there is a fast one doing nothing.
4.  You got a number, be it just the free RAM or the free RAM plus the free OS swap. Reduce it a bit, to be on the safe side, and that is the Tile Cache you could use as a good start.

As you can see, all is about checking the free resources, and decide if the OS swap is worth using or will cause more problems than help.

### Tuning the value and other helpful changes.

There are some reason you want to adjust the value. The basic one is changing your computer usage pattern, or changing hardware. That could mean you assumptions about how you use your computer, or the speed of it, are not longer valid. That would require a reevaluation of the previous steps, which can drive you to a similar value or a completly new value.

Other reason to change the value is because you detect it goes too slowly inside GIMP but changing to other applications is fast, which probably means tile size is too low. Or maybe you get complaints from other applications about not having enough memory, so probably better lower tile size if it is not already really small.

If you decided to use only RAM and it goes slow, you could try increasing the value a bit, but never to use also all the free swap. If the case is the contrary, using both RAM and swap, and you have problems about lack of resources, decrease it.

More tricks are to put the Swap Dir in a very fast disk, or in a different disk than the rest of things. Spreading the operating system swap over multiple disks is also a good way to speed up things, in general. And of course, maybe you have to buy more RAM or stop using lots of programs at the same time, you can not expect to edit a poster in a computer with 16MB and be fast.

On a side note: you can make your title or status bar show the memory usage (if not already doing so). That is the simplest way to keep an eye on how much memory you are using per image, and thus see what is the typical usage you get or if a image is just an exception and not worth the hassle of changing values.

### Some info about GIMP memory usage.

You can check what memory requirements your images have in advance. The bigger the images and the number of undos, the more resources you need. This is another way to choose a number, but it is only good if you always work in the same kind of images, and thus the real requirements do not vary. It is also good to know if you will require more RAM and/or disk space so you can go shopping for hardware with a better idea of what you need (lots of RAM vs not so much RAM and better get a faster CPU, for example).

First is the memory for the pixel data. Each layer requires layer width * layer height * 3 bytes for RGB background without alpha or * 4 for RGB layers with alpha.

Then GIMP needs to store the selection mask, which is a width * height of the total image. Next, the composed image, which is what you see in your screen, requires image width * height * 5,33\. The fractional part is because, starting with GIMP 2.4, the composed image is kept in several sizes. You can combine these two values as image width * height * 6,33.

Last, there is some overhead GIMP needs to know where pixels are stored, so round the number up or add a 5-10% to be in safe side. For medium and big images, what really counts is the pixel related memory.

