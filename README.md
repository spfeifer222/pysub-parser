## pysub-parser

[![Version](/home/pfeifer/dev/pysub-parser/release-v1.1.0-blue.svg)](https://github.com/spfeifer222/pysub-parser)

<!--
[![Build Status](1/federicocalendino/pysub-parser.svg?branch=master)](https://travis-ci.com/federicocalendino/pysub-parser)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=federicocalendino_pysub-parser&metric=alert_status)](https://sonarcloud.io/dashboard?id=federicocalendino_pysub-parser)
[![CodeCoverage](https://codecov.io/gh/federicocalendino/pysub-parser/branch/master/graph/badge.svg)](https://codecov.io/gh/federicocalendino/pysub-parser)
-->
Special Thanks goes to __Federico Calendino__ who created pysub-parser.


Utility to extract, clean, and print/save the content of a subtitle file.

Supported types:

type | functionality
:-----| --------------
`ssa`: [SubStation Alpha](https://en.wikipedia.org/wiki/SubStation_Alpha) <br> `ass`: [Advanced SubStation Alpha](https://en.wikipedia.org/wiki/SubStation_Alpha#Advanced_SubStation_Alpha) <br> `sub`: [MicroDVD](https://en.wikipedia.org/wiki/MicroDVD) <br> `txt`: [Sub Viewer](https://en.wikipedia.org/wiki/SubViewer) | extract, clean, print
`srt`: [SubRip](https://en.wikipedia.org/wiki/SubRip)  | extract, clean, write

For more information: http://write.flossmanuals.net/video-subtitling/file-formats


##### Import the modul

```python
import pysubparser as ps
```

### Quick usage instructions

The method `ps.parse` requires the following parameters:

__mandatory:__

* `path`: location of the subtitle file.

__optional/sometimes required:__

* `subtype`: one of the supported file types, by default file extension is used.
* `encoding`: encoding of the file
    *`utf-8` by default
    * If you get an `UnicodeDecodeError: 'utf-8' codec can't decode byte [byte] in position [position]: invalid continuation byte` try `enconding='latin-1'` or other encoding.
* `**kwargs`: optional parameters.
  * `fps`: framerate (only used by `sub` files), `23.976` by default.

##### Example to print Subtitles on terminal (all types, except .srt):

The `ps.parse()` function yield a generator of `Subtitle` objects from the `Subtitle` class. This generator is used to make the clean up and produce the output:

```python
subtitles = ps.parse('./files/space-jam.ssa')

for subtitle in subtitles:
    print('{} > {}'.format(subtitle.index, subtitle.text))
```

output:
```
1 > [BALL BOUNCING]
2 > Michael?
3 > What are you doing out here, son? It's after midnight.
4 > MICHAEL: Couldn't sleep, Pops.
...
```

##### Example to print Subtitles on terminal (.srt only)

Subtitles of type `srt` are organized and saved as a dictionary as part of the `Subtitles` class (note the plural naming). The dictionary is accessible by the attribute `subs`. Iterating over the dictionary generates the output:

```python
subtitles = ps.parse('./files/S01E04.srt')

for _,subtitle in subtitles.subs.items(): 
     print(subtitle.__repr__()) 
```
output:
```
00:02:08,388-00:02:12,685
It was the same woman from my dream, I'm sure of it. The same face. (4297 ms.)

00:02:12,768-00:02:16,313
You gotta stop watching all those cop shows. They will mess you up. (3545 ms.)

00:02:16,396-00:02:19,316
I feel like I know her, I just don't remember from where. (2920 ms.)
...
```

##### Example to clean up and write subtitles on disk with `ps.write()` function (.srt only)

The `Subtitles` class exihibits a `write()` function, which backup the origin file `space-jam.srt' to 'space-jam.srt.orig' in the source directory and save the cleaned subtitles to `space-jam.srt` (as ready to use). Hereby, advertising subtitles containing either of the following are removed:

- `www.*.com`
- `corrected by`
- `subtitles` <br>

```python
subtitles = ps.parse('./files/S01E04.srt')
subtitles.write()
```

Output:
```
Write subtitles to disk skipping empty subtitles...
Done.
```

<!--
 - `to_lowercase`: if `True` (default: `False`), the string wont be transformed to lowercase .
 - `to_ascii`: if `True` (default: `False`, every character will be transformed to their closest ascii representation.
 - `remove_brackes`: if `True` (default: `False`),  everything inside `[brackets]` will be removed.
 - `remove_format`: if `True` (default: `False`),  every formatting tag `<i>abc</i>` will be removed. 
 - `remove_advertising`: if `True` (default), subtitles with matches for
    - `www.*.com`
    - `corrected by`
    - `subtitles` <br>
are removed.
 -->

### `Class` descriptions
#### `Subtitles` Class 

##### Load Subtitles into `Subtitles` Class


##### Write Subtitles on disk with `ps.write()` function (.srt only):

This function 


### Subtitle Class

Each line of a dialogue is represented with a `Subtitle` object with the following properties:

* `index`: position in the file.
* `start`: timestamp of the start of the dialog.
* `end`: timestamp of the end of the dialog.
* `text`: dialog contents.

**text clean up**:

The class `Subtitle` provides a method `clean_up` to normalize its text, 
this will lower case it and remove anything that isn't letters or numbers.


* `to_lowercase`: if `False`, the string wont be transformed to lowercase.
* `to_ascii`: if `True`, every character will be transformed to their closest ascii representation.
* `remove_brackes`: if `True`,  everything inside `[brackets]` will be removed.
* `remove_format`: if `True`,  every formatting tag `<i>abc</i>` will be removed.

```python
from parser import parse

subtitles = parse('./files/space-jam.srt')

for subtitle in subtitles:
    print('{} > {}'.format(subtitle.index, subtitle.clean_up(to_ascii=True, remove_brackets=True)))
```

Output:
```
1 > 
2 > michael
3 > what are you doing out here son its after midnight
4 > michael couldnt sleep pops
5 > well neither can we with all that noise youre making
6 > come on lets go inside
7 > just one more shot

```

