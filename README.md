# Analysis of Dark Moon dice rolling patterns

Just played this game for the first time a few days ago, and I got curious about what sorts of rolls should be expected from an Uninfected player.

Of greatest interest are probably the outputs on how often a positive contribution should be made (depending, obviously, on the number of dice being rolled), and the probability of submitting more than one positive die. The average best submission is also an interesting figure.

### Usage
run the script ```./dark_moon_dice_calc.py``` with the names (or accepted abbreviations) of dice in the roll you wish to analyze.

For instance, using the full names, you might run:
```./dark_moon_dice_calc.py black_d6 black_d6 red_d6```

...which will perform an analysis on the fairly common scenario of rolling three dice, one of which is a red (weak) die, the other two being black (strong) dice.

Abbreviations that are currently accepted are listed in the script itself, but a less-verbose equivalent for the above might be:
```./dark_moon_dice_calc.py b b r```

The blue (Commander's) die is also available, and naturally the script is easily edited to define new types of dice and make them available.
