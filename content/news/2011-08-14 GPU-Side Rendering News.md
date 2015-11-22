Title: On GPU-side Rendering and Further Development Plans
Date: 2011-08-14
Category: News
Authors: Alexandre Prokoudine

While GEGL gradually replaces GIMP's old core, it's time for us to consider long-term strategy for improving performance. The trend these days seems to be a combination of multithreading, GPU-side processing and networks. Most of that can be handled thanks to OpenCL standard by Khronos Group.

Back in 2009 we already had a Google Summer of Code project by Jerson Michael Perpetua who introduced basics of GPU-side rendering to GEGL. This year we have even more progress. Another GSoC student, Victor Oliveira, has been working on support for OpenCL in GEGL since late May. If you are interested in details, please read his latest [report](http://meudepositodeideias.wordpress.com/2011/08/08/opencl-on-gegl-results-up-to-now/).

The upcoming GIMP v2.8 isn't going to do GPU-side rendering and processing, because it's simply too late for this development cycle. The next version, v2.10, is going to feature all of our other GSoC projects this year and more API cleanup. With v3.0 we are doing the final switch to GEGL, and this is where we currently expect OpenCL support in GEGL to be mature enough to be used. For more details please refer to our [feature roadmap](http://wiki.gimp.org/index.php/Roadmap).

We aim to make GIMP a state of the art image editing tool. We know that our past approach to development of new versions didn't exactly encourage contributions that helped making it happen. This is why starting with v2.10 we are switching to a shorter development cycle. In other words, new stable versions will have less new features and will get released sooner, helping us to process queue of incoming new features much faster.

All major new features are now being developed in dedicated Git branches so that you could easily merge our latest upstream changes into your feature branches, and we then could easily review and merge your new features into upstream. If the new proposed workflow sounds appealing to you, and you are interested to contribute to the project, please let us know.

In the mean time we are preparing another development version of GIMP with quite a lot of fixes gathered over last 4 months. Stay tuned for more news.
