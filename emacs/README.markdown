Installation and use
====================

To use the emacs commands, [create a Fluidinfo
account](https://fluidinfo.com/accounts/new/) and put your username and
password into the top of `shared-clipboard.el`.

You'll need to [install fluiddb.el](https://github.com/hdurer/fluiddb.el).

Either do a `M-x load-library RET shared-clipboard` or evaluate the
`shared-clipboard.el` buffer and you'll have the following new emacs
commands:

 - `M-x insert-clipboard`
 - `M-x set-clipboard`
 - `M-x clear-clipboard`

which do the obvious things.  Note that there is very little error
checking. E.g., if you don't have a region set when you run `M-x
set-clipboard` you'll probably get an error.

Apologies, this was just a quick hack. Improvements happily accepted.

