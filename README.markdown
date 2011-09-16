Shared Clipboard
================

The shared clipboard does what it says on the label. Use it to share a
clipboard between applications you're using on different devices, or
between different people. For example, you might use Dragon Dictate on a
Mac to compose some text, and then yank it into your editor running on a
Linux machine for final editing. Or, highlight some text in your browser so
someone you're talking to on Skpye can immediately yank it into a Gmail
message.

The idea for sharing a clipboard in this way came from [Hilary
Mason](http://www.hilarymason.com/).  Thanks Hilary!

This Github repository holds a collection of small utilities that can store
selected text into a user's clipboard tag in
[Fluidinfo](http://fluidinfo.com/), retrieve that text and insert it, or
clear the clipboard tag (i.e., remove it from Fluidinfo).

To use one or more of the utilities (at least if you want to *store* things
to a clipboard), you will need a Fluidinfo account ([sign-up
here](https://fluidinfo.com/accounts/new/)).

Note that by default *all clipboards tags are publicly readable* (this is
easily changed - see below).

Available utilities
-------------------

We currently have code for:

 - Command line.
 - Chrome-based browsers ([Chromium](http://www.chromium.org/Home) and [Chrome](http://www.google.com/chrome)).
 - The [Emacs](http://www.gnu.org/software/emacs/) text editor.
 - [Python](http://python.org).

Adding to the collection
------------------------

If you're interested to contribute code for another application, please
feel free to fork this project and send a Pull Request.

Any Fluidinfo-aware application can participate.  The only thing an
application needs do is to follow the tagging convention. I.e., use the
same tag that all the other applications are using.  This will create a
broadening set of applications and users that are able to exchange
clipboards with one another.

If you have questions about how best to use Fluidinfo, please join us in
`#fluidinfo` on `irc.freenode.net` to ask questions.  There are lots of
Fluidinfo client libraries that should make it simple to add support for
your favorite application to the collection. Check out the [Fluidinfo
developer information](http://fluidinfo.com/developers/documentation) for
details.

The Fluidinfo clipboard tag
---------------------------

The Fluidinfo tag currently used (by convention) by the utilities in this
collection is `username/clipboard`.

Unless you set its permissions otherwise, the tag will be publicly
readable. We might want to move to having two tags, e.g.,
`public-clipboard` and `private-clipboard` though this would require UI
changes in the various utilities.
