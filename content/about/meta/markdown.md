Title: Markdown Cheatsheet
Date: 2015-08-10T15:41:15-05:00
Modified: 2015-08-11T11:43:00-05:00
Author: Pat David

This is a simple cheatsheet for writing in [Markdown].
For a more complete reference, the Python-Markdown package refers one to the [Markdown Syntax] from John Gruber.

[TOC]

## Paragraphs and Line Breaks

Paragraphs are one or more consecutive lines of text, separated by one or more blank lines.
A blank link will indicate a new paragraph to begin.

If a hard `<br />` is desired, simply end the line with two or more spaces.
The next line will still be in the same `<p>` element, but will be hard-wrapped.

The above paragraphs look like this in plain Markdown:

    Paragraphs are one or more consecutive lines of text, 
    separated by one or more blank lines.
    A blank link will indicate a new paragraph to begin.

    If a hard `<br />` is desired, 
    simply end the line with two or more spaces.
    The next line will still be in the same `<p>` element, 
    but will be hard-wrapped.


## Headers

Markdown uses two styles to denote headers.

Setext-style headers use "underlines" with equal signs (for first-level headers), and dashes (for second level):

    This is an H1
    =============
    
    This is an H2
    -------------

Atx-style headers use from 1-6 hash characters at the start of the line,
corresponding to header levels 1-6:

    # This is an H1
    ## This is an H2
    #### This is an H4



## Blockquotes

Blockquotes use a familiar email-style ">" character for quoting:

    > This is a blockquote with some information. If you
    > think this needs to be quoted.

> This is a blockquote with some information. If you
> think this needs to be quoted.

Alternatively you can be lazy and only use the ">" character before the first line of a hard-wrapped paragraph:

    > This is a blockquote with some information.  If you
    think this needs to be quoted, here it is.

> This is a blockquote with some information.  If you
think this needs to be quoted, here it is.


    > This is a blockquote with some information.  If you
    think this needs to be quoted, here it is. Here is 
    a nested quote inside this blockquote:
    > > A nested quote inside a previosu blockquote!

> This is a blockquote with some information.  If you
think this needs to be quoted, here it is. Here is 
a nested quote inside this blockquote:
> > A nested quote inside a previous blockquote!

    > Blockquotes can also have **Markdown** elements
    inside them that *will* get parsed.

    > ### A Header 3
    For all to see.

> Blockquotes can also have **Markdown** elements
inside them that **will** get parsed.

> ### A Header 3
For all to see.



## Lists

Ordered and unordered lists are supported.

Unordered lists use asterisks, pluses, and/or hyphens -- interchangeably -- as markers:

    * Red
    * Green
    + Blue

* Red
* Green
+ Blue

Ordered lists use numbers followed by periods:

    1. One Fish
    2. Two Fish
    3. Red Fish
    5. Blue Fish

1. One Fish
2. Two Fish
3. Red Fish
5. Blue Fish

**Notice** that the actual numbers are not used in creation of the list!
The last element in our example is not a typo - it is a number "5", not 4.

There can be multiple paragraphs in a list item.
Each subsequent paragraph needs to be indented by either 4 spaces or one tab:

    1. This is a first list item.

        I should probably make this a little neater in the next item.
        I'll try to make sure things look a little nicer as an example.

    2.  This is a second list item
        Just added some extra whitespace in front of this to make it neater
        in the source example.

1. This is a first list item.

    I should probably make this a little neater in the next item.
    I'll try to make sure things look a little nicer as an example.

2.  This is a second list item
    Just added some extra whitespace in front of this to make it neater
    in the source example.



## Code Blocks

Code blocks will present the text exactly as shown and will automatically convert objects to their corresponding html entity.
To create a code block, simply indent every line of the block by 4 spaces or one tab:

    This would be a normal pargraph in a document.

        This is indented by 4 spaces and would show up as code.
        This second line would still be part of that code block.

This would be a normal paragraph in a document.

    This is indented by 4 spaces and would show up as code.
    This second line would still be part of that code block.

With the Python-Markdown extensions, you can also include an explicit declaration of the type of code for highlighting.
Begin the code block with three colons followed by the language to highlight as:

        :::html
        <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />

Which will yield:

    :::html
    <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />



## Horizontal Rule

A horizontal rule tag `<hr />` can be inserted by simply using three or more hyphens, asterisks, or underscores on a line by themselves:

    * * *
    ***
    *********
    - - -
    ---
    _________

Any of those will insert the horizontal rule at that location:

---


## Links

Markdown offers two styles of links: *inline* and *reference*.

The link text is enclosed by [square brackets].

Inline links use parenthesis immediately after the closing square bracket to contain the link URL, and an optional title:

    This will [link to pixls.us](https://pixls.us "A Link to pixls.us").

This will [link to pixls.us](https://pixls.us "A Link to pixls.us").

You can use relative paths while on the same site:

    A link back to the [Meta page](/about/meta/).
    A link back to the [Meta page](../meta/).

A link back to the [Meta page](/about/meta/).  
A link back to the [Meta page](../meta/).

Reference-style links use a second set of square brackets with a self-chosen label to identify the link:

    This is another link to [pixls][1]

Then anywhere in the document you can define the link label on it's own line:
    
    [1]: https://pixls.us "An Optional Title for the Link"

Link definition names can contain any numbers, letters, spaces, or punctuation and are not case-sensitive:

    [link text][a]
    [link text][A]

are equivalent links.

There is also an *implicit link name* shortcut that lets you use the link text itself as the identifier.
Use a second set of empty square brackets after the initial link text:

    [Google][]

Where the link can then be identified elsewhere as:

    [Google]: http://www.google.com

[Google]: http://www.google.com
[1]: https://pixls.us



## Emphasis

Asterisks (\*) and underscores (\_) are used as indicators of emphasis.
Text wrapped in on asterisk or underscore will be wrapped with an HTML `<em>` element.
Double asterisks or underscores will be wrapped with an HTML `<strong>` tag:

    *single asterisk*
    _single underscore_
    **double asterisks**
    __double underscores__

outputs:

    <em>single asterisk</em>
    <em>single underscore</em>
    <strong>double asterisks**
    <strong>double underscores</strong>

or:

*single asterisk*  
_single underscore_  
**double asterisks**  
__double underscores__  

## Code

An inline span of code uses the backtick quote (\`) to offset it from surrounding text.

    You can use the `printf()` function.

produces:

You can use the `printf()` function.



## Automatic Links

A shortcut for creating links to URLs and email addresses can be used where the address is wrapped in angle brackets:

    <https://pixls.us>

Which will be turned into an html link of the address text:

    <a href="https://pixls.us">https://pixls.us</a>

<https://pixls.us>


[Markdown]:http://daringfireball.net/projects/markdown/ 
[Markdown Syntax]: http://daringfireball.net/projects/markdown/syntax
