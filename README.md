# asking-cli

A tiny `input()`-driven quiz — the demonstration of cleanroom's stdin lane.

Four questions, one verdict. In [cleanroom](https://amanvicky.github.io/cleanroom/),
paste this repo's URL: the runner sees the `input()` calls, arms the stdin
lane, and the terminal box becomes the app's keyboard — type each answer on
its own line, then run `quiz.py`. The VM feeds those lines to `input()` like
a real stdin; if the queue runs dry, you get an honest `EOFError` telling you
what to do, not a hang.

On a real PC it is a plain script:

```
python quiz.py
```
