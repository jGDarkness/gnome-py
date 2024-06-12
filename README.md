# GNOME Hidden Settings Editor

### Why?

I recently moved to Linux as my daily driver, because I was tired of Microsoft invading every
part of my computing life. Especially now that Recall is a thing. I also wanted to better support
the FOSS community. I really like GNOME, however, there are a few settings that are very hard to
get to, let alone change, without downloading extensions that can break whenever the shell updates.

So, to get around that, I'm building a Python based GUI app that will expose the settings and provide
the user with a simple interface for editing. 

### Status

Currently, the master branch only has a title bar and a "Hello, World!" message. This is all I had time to implement today (06/12/2024). I will be adding a left navigation bar next. The first settings I plan to expose and provide for changes will include all audio devices on the system. I will also implement administrator authentication for it.