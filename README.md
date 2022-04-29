## Water Jug Puzzle From Scratch

Water jug is a classic and also interesting puzzle to solve. You are given some number of jugs with a capacity and a initial state of water in each jug. Now you should do some operations to make the water in one jug to be equal to the goal amount.

This puzzle in computer science is usually solved in two ways; the simplest way is to act step by step and the other is to use trees to show all possible situations ahead. Here I will try to implement the simplest way.

![You can not drink under a hockey mask...](https://media.giphy.com/media/3oKIPaVO4VEyVnjsuk/giphy.gif)

### Rules

There is no any formal strategy and you have to make one for yourself... Just kidding, you can use some standard answers for specific situations!

Let's solve a few examples to understand it better, but before that we have to respect some limitations. The operations you can perform are:

- Empty a jug
- Fill a jug
- Pour water from one jug to another until one of the jugs is ethier full or empty

### Examples

<i>Read the states like this: (amount of jug A/capacity of jug A, amount of jug B/capacity of jug B) [-> goal amount]</i>

![Situation no. 1:](screenshots/situation-no1.png)\
\
![Situation no. 2:](screenshots/situation-no2.png)\
\
![Situation no. 3:](screenshots/situation-no3.png)\
\
![Situation no. 4:](screenshots/situation-no4.png)

### Screenshots

![Solved puzzle with default values.](screenshots/solved-puzzle.png)
![Another solved puzzle with huge jugs.](screenshots/solved-puzzle-with-huge-jugs.png)
![Manually solved puzzle.](screenshots/manually-solved-puzzle.png)
![Manually unsolved puzzle.](screenshots/manually-unsolved-puzzle.png)
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
