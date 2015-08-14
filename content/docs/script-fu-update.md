Title: Script-Fu in GIMP 2.4
Date: 2015-08-14T15:02:25-05:00
Author: Pat David


Since version 1.0 of GIMP, it has included a powerful scripting language which permits extending the program's capabilities and simplifying repetitive tasks. This scripting language, called "Script-fu", was based upon the Scheme programming language and implemented the SIOD interpreter written by George J. Carrette while he was a professor at Boston University in the late 80s.

This Script-fu interpreter based upon Carrette's SIOD has served GIMP extremely well over the last decade -- thousands of scripts have been written and shared by GIMP users -- but it is starting to show its age and therefore the GIMP development team has decided to replace it with a more modern Scheme interpreter called TinyScheme. One of the main reasons for this changeover is to support international languages and fonts, for which SIOD offered no provision. There are other benefits as well, but lack of international support was the most significant.

Though this switch has required an extensive effort on the part of GIMP developers (particularly Kevin Cozens) and some significant changes to the internals of the GIMP code, there should be very little visible change to GIMP users. GIMP's scripting extension is still called "Script-fu" and the vast majority of the scripts already available will still function using the new TinyScheme-based interpreter.

Despite the desire to keep the impact of this change to GIMP internals to a minimum, there are some differences between the SIOD-based interpreter and the TinyScheme-based Script-fu which may crop up when trying to use older scripts with GIMP 2.4 and more recent releases. What follows is a description of some of the problems which may be encountered and what steps need to be taken to correct them.

*   [Setting an undeclared variable](#unbound)  
    (<tt>Error: set!: unbound variable: x</tt>)
*   [Using the empty list in conditionals](#condempty)
*   [Accessing the first element of an empty list](#carempty)  
    (<tt>Error: car: argument 1 must be: pair</tt>)
*   [Accessing beyond the last element of a list](#cdrempty)  
    (<tt>Error: cdr: argument 1 must be: pair</tt>)
*   [Constructing a pair](#cons)  
    (<tt>Error: cons: needs 2 argument(s)</tt>)
*   [Fractional numbers must not start with a dot](#leadingdot)  
    (<tt>Error: eval: unbound variable: .</tt> )
*   [Deprecated features](#deprecated)
*   [Conclusion](#conclusion)  
    (and other differences)

## Setting an undeclared variable

By far, the most common problem that can be expected if using an older script is that it might assign a value to a variable without first declaring the variable. SIOD-based Script-fu would permit a statement such as `(set! x 4)` even if '<tt>x</tt>' had not been declared -- '<tt>x</tt>' would be defined automatically to be a global variable. The new Script-fu protects against this situation and the programmer **must** declare the variable first. The offending script would result in an error message stating, "<tt class="warn">Error: set!: unbound variable: x</tt>".

The use of global variables is generally discouraged because another function (written by a different author) may have chosen to use the same name and the two functions would interfere with each other. For this reason, the correct method of declaring '<tt>x</tt>' in the preceding example is to use the `let` or `let*` statement:

    :::scheme
    (let* ( (x 4) )
      ...
      ...
      ...
      )

## The empty list in conditionals

SIOD treated the empty list to be FALSE when it appeared in a conditional test (if, while, cond, not, =, etc) whereas the Scheme standard specifies that it should evaluate to TRUE. Programmers have been aware of this difference since the beginning and it is unlikely that scripts will be encountered which rely upon SIOD's nonstandard behavior but it is possible. A simple solution is to use the 'pair?' function to test the list. For example, replace `(while lis ... )` with `(while (pair? lis) ...)`. Alternately, `(not (null? lis))` could be used instead of `(pair? lis)`.

## Accessing the first element of an empty list

In SIOD, taking the 'car' of an empty list returned an empty list; in TinyScheme this is not permissible and will generate an error message ("<tt class="warn">Error: car: argument 1 must be: pair</tt>"). Like the case for conditionals, programmers have been aware of SIOD's nonstandard behavior and encountering this problem should be rare. Correcting such a problem, if encountered, should consist of testing whether a list is empty before accessing it.

## Accessing beyond the last element of a list

Similar to the preceding problem, SIOD would permit you to access beyond the last element in a list, returning an empty list as a result. For example, taking the 'cdr' of an empty list or the 'cddr' of a one-element list. In GIMP 2.4, Script-fu will not allow this and it will result in an error message ("<tt class="warn">Error: cdr: argument 1 must be: pair</tt>"). Again, SIOD's behavior has long been realized to be non-standard and this problem's occurance should be rare. Correcting such a problem, if encountered, should consist of more precise testing when accessing a list.

## Constructing a pair

The Scheme `cons` function expects two arguments which are combined into a pair. In SIOD, if only one argument was provided then the second argument was assumed to be an empty list. In GIMP 2.4, if the second argument is not present than an error occurs ("<tt class="warn">Error: cons: needs 2 argument(s)</tt>"). The solution, should this problem be encountered, is explicitly include an empty list as the second argument.

## Fractional numbers must not start with a dot

If you had some numbers written as '.5' instead of '0.5', then you may get the error "<tt class="warn">Error: eval: unbound variable: .</tt> ". The solution is to make sure that all numbers start with a digit and add a leading '0' if necessary. (Note: this is considered as a bug and this may be fixed in a future GIMP release.)

## Deprecated features

The following SIOD functions or constants are currently made available in TinyScheme Script-fu but may disappear in future versions.

*   `aset` - replaced by TinyScheme's `vector-set!`
*   `aref` - replaced by TinyScheme's `vector-ref`
*   `fopen` - replaced by TinyScheme's `open-input-file`
*   `mapcar` - replaced by TinyScheme's `map`
*   `nil` - replaced by TinyScheme's `'()`
*   `nreverse` - replaced by TinyScheme's `reverse`
*   `pow` - replaced by TinyScheme's `expt`
*   `prin1` - replaced by TinyScheme's `write`
*   `print` - replaced by TinyScheme's `write` (along with `newline`)
*   `strcat` - replaced by TinyScheme's `string-append`
*   `string-lessp` - replaced by TinyScheme's `string<?`
*   `symbol-bound?` - replaced by TinyScheme's `defined?`
*   `the-environment` - replaced by TinyScheme's `current-environment`
*   `*pi*` - the constant *pi* is not predefined in TinyScheme but can be defined as `(* 4 (atan 1.0))`
*   `butlast` - is not available in TinyScheme but alternate coding using `(reverse (cdr (reverse x)))` is possible
*   `cons-array` - replaced by TinyScheme's `make-vector`

## Conclusion

There are some other differences between the original Script-fu and the Script-fu of GIMP 2.4 but they should have little or no impact on existing scripts because of their rarity. These include the syntax for the `catch`/`throw` statements (which trap errors) and the `bytes-append` function (which does not seem to appear in any published Script-fu). If you encounter scripts containing such problems, please post on the GIMP developers mailing list outlining your problems.

More information about the Scheme syntax of Script-Fu can be found in the _Revised<sup>5</sup> Report on the Algorithmic Language Scheme_, also know as [R5RS](http://schemers.org/Documents/Standards/R5RS/HTML/). Tinyscheme does not support all features of R5RS, but if a precedure is available, it is supposed to behave like documented.
