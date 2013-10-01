rednotebook fork
----------------

The purpose of this fork is to customize rednotebook to my liking. Specifically,
I am going to explore (in mostly prioritized order):

1) replacing txt2tags with markdown.
    - will require script to convert notebooks
2) adding drag/drop support for images
    - copy to notebook directory
3) adding true todo list support
    - taskwarrior integration?
4) adding plugin infrastructure to allow scripting in templates
    - auto grab news items
    - taskwarrior integration?
5) enhance the search feature
    - https://bugs.launchpad.net/rednotebook/+bug/1161130
6) evaluate storage options
    - I like plaintext, but one file per month seems odd
5) customize rednotebook to my needs
    - vague, but will determine specifics throughout development
6) fix bugs on the launchpad tracker that affect me (will prioritize and flesh these out later)
    - https://bugs.launchpad.net/rednotebook/+bug/855443
    - https://bugs.launchpad.net/rednotebook/+bug/1024624
    - https://bugs.launchpad.net/rednotebook/+bug/1073923
    - https://bugs.launchpad.net/rednotebook/+bug/1106074
    - https://bugs.launchpad.net/rednotebook/+bug/1179254
    - https://bugs.launchpad.net/rednotebook/+bug/1012919

This list will likely evolve over the course of development. Once I have
established my roadmap a bit more, I'll likely switch over to using github's
issue tracker since this is already a bit of a mess.

Initially, I will be focusing on replacing txt2tags with markdown, as I am more
familiar with (and prefer) its syntax and it seems to be more widely used. I
already have some code to do the image drag/drop and autoretreival, but it needs
some refactoring (and likely a bit more once I switch to markdown).  

This fork is based on revision 1312 of rednotebook.

bzr branch lp:rednotebook -r 1312
