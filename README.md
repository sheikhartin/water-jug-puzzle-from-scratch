## Water Jug Puzzle From Scratch

Water jug is a classic and also interesting puzzle to solve. You are given some number of jugs with a capacity and a initial state of water in each jug. Now you should do some operations to make the water in one jug to be equal to the goal amount.

![You can not drink under a hockey mask...](https://media.giphy.com/media/3oKIPaVO4VEyVnjsuk/giphy.gif)

### Rules

There is no any formal strategy and you have to make one for yourself... Just kidding, you can use some standard answers for specific situations!

Let's solve a few examples to understand it better, but before that we have to respect some limitations. The operations you can perform are:

- Empty a jug
- <s>Fully fill a jug</s>
- Pour water from one jug to another until one of the jugs is ethier full or empty

The reason for removing the filling operation is that it is not possible when you and a mad stranger are fighting over a jug in the desert! It may sound silly, but please accept.

### Examples

Do all situations have answers? No, it's not. Use the below formula to test the possibility quickly:

$$
\begin{array}{l}
\begin{array}{ l }
(capacity\ A-amount\ A)\ \pm \ (capacity\ B-amount\ B)\ =\ \begin{cases}
x\\
y
\end{cases}
\end{array}\\
we\ probably\ have\ a\ solution\ if\ x\ or\ y\ is\ equal\ to\ the\ goal\ amount\\
but\ don't\ trust,\ the\ game\ is\ not\ always\ so\ simple
\end{array}
$$

<span style="color:orange"><i>Read the states like this: (amount of jug A/capacity of jug A, amount of jug B/capacity of jug B) [-> goal amount]</i></span>

$$
\begin{array}{l}
situation\ no.\ 1:\ ( 4/5,\ 3/5) \ \rightarrow \ 3\\
\\
(5-4)\ \pm \ (5-3)\ =\ \begin{cases}
+3\\
-1
\end{cases}\\
the\ x\ value\ touched\ our\ goal\\
\\
solution:\ (4/5,\ 3/5)\ \rightarrow \ (0/5,\ 3/5)\ \rightarrow \ done\\
\\
\\
situation\ no.\ 2:\ ( 5/7,\ 2/8) \ \rightarrow \ 0\\
\\
( 7-5) \ \pm \ ( 8-2) \ =\ \begin{cases}
+8\\
-4
\end{cases}\\
this\ time\ none\ of\ the\ x\ and\ y\ values\ ​​reached\ our\ desired\ level,\ but\ we\ know\ that\\
the\ containers\ must\ be\ empty\ now\ and\ the\ above\ formula\ includes\ exceptions\\
\\
solution:\ ( 5/7,\ 2/8) \ \rightarrow \ ( 0/7,\ 2/8) \ \rightarrow \ ( 0/7,\ 0/8) \ \rightarrow \ done\\
\\
\\
situation\ no.\ 3:\ ( 3/7,\ 1/4) \ \rightarrow \ 7\\
\\
(7-3)\ \pm \ (4-1)\ =\ \begin{cases}
+7\\
+1
\end{cases}\\
the\ formula\ tells\ us\ it\ is\ possible,\ but\ the\ amounts\ and\ rules\ ​​do\ not\ think\ so\\
\\
\\
situation\ no.\ 4:\ ( 11/14,\ 4/6) \ \rightarrow \ 5\\
\\
(14-11)\ \pm \ (6-4)\ =\ \begin{cases}
+5\\
+1
\end{cases}\\
what\ does\ the\ formula\ tell\ us?\ yeah,\ it's\ possible\ again\\
\\
do\ you\ solve\ this?
\end{array}
$$

### Screenshots

![Solved puzzle with default values.](screenshots/solved-puzzle.png)
![Another solved puzzle with huge jugs.](screenshots/solved-puzzle-with-huge-jugs.png)
![Manually solved puzzle.](screenshots/manually-solved-puzzle.png)
![And a unsolved puzzle...](screenshots/unsolved-puzzle.png)

### Usage

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the core logic directly from the command line:

```bash
python core.py
```

Or even better, use the graphical interface:

```bash
python app.py
```

### License

This project is licensed under the MIT license found in the [LICENSE](LICENSE) file in the root directory of this repository.
