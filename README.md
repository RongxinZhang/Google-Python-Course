# Google-Python-Course
Self directed google python course

Link: https://developers.google.com/edu/python/

## Completed exercises

Started on   : 07/10/2017

Completed on : 07/17/2017

## How to run
- Make sure you are in the root director of the project.
- Then copy the commands for each exercise into your terminal without changing directories.


#### Part 1: Basic
- [x] string1.py
```sh
#Copy below commands and run in terminal
(cd ./basic && python string1.py)
```
- [x] list1.py
```sh
#Copy below commands and run in terminal
(cd ./basic && python list1.py)
```
- [x] wordcount.py
```sh
#Copy below commands and run in terminal
(cd ./basic && python wordcount.py --count alice.txt)

# OR

(cd ./basic && python wordcount.py --topcount alice.txt)
```

#### Part 2: Babynames:
- [x] babynames.py

```sh
#Copy below commands and run in terminal
# Print out baby names and rank
(cd ./babynames && python babynames.py baby1992.html)

# Create .summary file with babynames and rank
(cd ./babynames && python babynames.py --summaryfile baby2006.html && open -a textedit baby2006.html.summary)

# Create .summary file for babynames and rank in all years
(cd ./babynames && python babynames.py --summaryfile baby*.html)
```

#### Part 3: CopySpecial:
- [x] copyspecial.py

```sh
#Copy below commands and run in terminal
(cd ./copyspecial && python copyspecial.py --todir newDir)

# OR

(cd ./copyspecial && python copyspecial.py --tozip ./)
```

#### Part 4: LogPuzzle:
- [x] logpuzzle.py

```sh
#Copy below commands and run in terminal
(cd ./logpuzzle && python logpuzzle.py --todir images  animal_code.google.com && open imageDisplay.html)
```
