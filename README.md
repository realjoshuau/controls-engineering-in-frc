# Practical Guide to State-space Control
## Graduate-level control theory for high schoolers

I originally wrote this as a final project for an undergraduate technical
writing class I took at University of California, Santa Cruz in Spring 2017
([CMPE 185](https://cmpe185-spring17-01.courses.soe.ucsc.edu/)). It is intended
as a digest of graduate-level control theory aimed at veteran FIRST Robotics
Competition (FRC) students who know algebra and a bit of physics and are
comfortable with the concept of a PID controller. As I learned the subject of
control theory, I found that it wasn't particularly difficult, but very few
resources exist outside of academia for learning it. This book is intended to
rectify that situation by providing a lower the barrier to entry to the field.

This book reads a lot like a reference manual on control theory and related
tools. It teaches the reader how to start designing and implementing control
systems for practical systems with an emphasis on pragmatism rather than theory.
While the theory is mathematically elegant at times and helps inform what is
going on, one shouldn't lose sight of how it behaves when applied to real
systems.

## Download

A PDF version is available at
https://file.tavsys.net/control/state-space-guide.pdf.

## Dependencies

To compile the book, the following are required.

* make (to run the makefile)
* texlive-core (for latexmk)
* texlive-latexextra (for bibtex and makeglossaries)
* texlive-bibtexextra (for additional BibTeX styles and bibliography databases)
* xelatex (for setting and using custom fonts)
* biber (for generating bibliography)
* Python 3.5+
  * Python Control (to generate plots and state-space results)
  * yapf (to format Python source code)
* tk (required on some Linux platforms as a backend for matplotlib)
* Inkscape (to convert SVGs to PDF)
* ghostscript (to reduce size of final PDF for publishing)

Python Control can be installed via your system's package manager or via pip.
For better root locus plots, build and install Python Control from its Git repo
at https://github.com/python-control/python-control instead of using 0.7.0 from
pypi.python.org.

```
git clone git://github.com/python-control/python-control
pip install --user ./python-control
```

The examples only require Python 3.5+ and Python Control. To run them, execute
the following in the `code` directory.

```
PYTHONPATH=. ./frccontrol/examples/elevator.py
```

## Build

After installing the dependencies, just run `make`. By default, two files will
be generated: state-space-guide.pdf, which has uncompressed images (way higher
than 300dpi); and state-space-guide-ebook.pdf, which is suitable for online
distribution.

The following make targets are supported for compiling the book with various
levels of image compression.

|Command          |File                            |Purpose                  |
|-----------------|--------------------------------|-------------------------|
|`make book-stamp`|`state-space-guide.pdf`         |Quick content development|
|`make ebook`     |`state-space-guide-ebook.pdf`   |Online distribution      |
|`make printer`   |`state-space-guide-printer.pdf` |Standard color printing  |
|`make prepress`  |`state-space-guide-prepress.pdf`|Book publishing          |

## Future Improvements

### Simplify for the target audience

The book is still very high level for the subject it covers as well as very
dense and fast-paced (it covers three classes of feedback control, two of which
are for graduate students, in one short book). I want to make the contents of
the book that are in the critical path more accessible.

What I need to do is read through this book from the perspective of explaining
it to my veteran software students, because my in-person tutor-style
explanations are generally better than what I write.

It's also not designed for skim reading (e.g., "Which equations do I need to
implement a low-fi simulator for a drivetrain?"). I already call out final
results, so filling out the index might help.

### Bridge the knowledge gap

### Add more practical examples

I'd also like to expand the introductions for each section and provide more
examples like I did for the Kalman filter design to give the reader practice
applying the skills discussed.

### Teach topics better

The classical control sections are glossed over. Also the stability portion
doesn't talk on how PID affects stability. There is mention of the root locus
but the student has no idea why it's important or how it relates to something
like a PID controller.

The probability section and math for stochastic systems needs examples.

### Finish incomplete topics

The following state-space implementation examples are planned:

* Elevator (in progress)
  * Add u_error state to model
  * Include writing unit tests in Google Test
  * Include how to implement the model in C++ with Eigen
* Flywheel (in progress)
  * See elevator items
* Drivetrain
  * See elevator items
  * 971/y2017/control_loops/python/polydrivetrain.py?
* Single-jointed arm (in progress)
  * See elevator items
* Rotating claw with independent top/bottom
  * See 971/y2014/control_loops/python/claw.py
  * Use as example of coordinate transformations for states?

Complete sections on integral control for plant augmentation and delta U
control?

### Add content for building understanding and intuition

### More thorough examples

The "Implementation Steps" section needs subsections to explain how to do each
or at least provide examples.

### Supplementary background

Any other results that are good for background but are unnecessary should be
included in an appendix.

Add a section on polytopes for convex optimization? So far, I've seen it used
for handling saturated control inputs to prioritize tracking some states over
others using the limited control input.

## Licensing

This project, except for the software, is released under the Creative Commons
Attribution-ShareAlike 4.0 International license. The software is released under
the 3-clause BSD license.
