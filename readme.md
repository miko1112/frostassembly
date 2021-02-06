# FAsm: Tiny power

### About

FrostAssembly, or FAsm, is a small, stack based programming language that uses reverse polish notation. I made it in my spare time.

### Backstory

At some point in time, I was looking for a text to speech program that sounded like those from the eighties. I found this website that emulated the SAM TTS engine, and I found it pretty cool, so I explored more of the creator's website. I then found that this person was working on a reverse engineered version of StarFlight, a game from 1986. I looked into the GitHub repository, and fell into the ReadMe.md file. That's when I got introduced to forth. The example they gave was the following:
```
2 3 + .
```
I was amazed by the simplicity of it, especially how what is happening internally is easy to explain. In s-macke's words, this is what happens:
 - push 2 on top of the stack
 - push 3 on top of the stack
 - pop the last two stack entries and add them together. push result back on top of the stack
 - pop the top value from the stack and print it

So, I decided that I would try to write an interpreter for Forth in Python. It was going smoothly until I tried to implement if statements. They defied the simplicity(at least in my head) and didn't use one char commands, which was one of the things I was most excited about. So I decided to take my own path and branch off into my own language. And here we are, with the first finished version of FAsm!

### Docs

Check out the documentation at https://miko1112.github.io/fasm/docs.

### Running Code

Run code by dragging your *.frost file on the fasmrun.py file.