This script simulates all possible reward-amounts (within a range)
at which you could choose to re-invest the rewards for compound
interest.

It comes with a built-in text UI to input the main values (capital,
interest rates, and flat fees). Other values are assumed, and can be
changed within the code (i.e. it assumes a 0.1% re-compound fee in
addition of the flat fee, since usually any recompound will involve
a change of currency).

The script chooses the timeframe it will use in the calculation by
aiming for an ideal amount of times recompounded, namely 4.
This is to avoid calculations with too many compounds. Since the
ideal amount at which to recompound varies with capital, and capital
increases after every compound, simulating too many compounds would
output an averaged result, less ideal for the immediate present than
a calculation with a shorter time-frame.

This was built purely to help out those people yield-farming who are
confused about how to figure out when should they be recompounding.
The community is welcome to improve on the existing model.