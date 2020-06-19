#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The run time complexity is O(n). The function will increase in a linear fashion respective to an input of n. The completion of the while loop happens at n^3, but n is squared and added at each pass. which reduces the initial assumption of an n^3 complexity down to n complexity


b) This is o(n + log(n))if we were really specific. If I had to reduce/simplify it further then I would say that the major factor in the run time complexity is the outer for loop which has a O(n) complexity, where the inner loop has a lesser impact with the log(n) complexity. essentially each increase in n is more efficient in the inner loop due to the doubling.


c) This is O(n) complexity. The bunnyEars essentially calls itself once for each bunny in the original calling of the function, giving a linear line if graphed out.

## Exercise II

It sounds like I'm getting an input of n floors for the building, and an input of f for safe floors. Not sure if I have an exact input for number of eggs, but that would help in determining efficiency if I knew that. Also, I'm not sure at what rate I'm climbing floors, or if I need to at all.
The most ideal solution given what I have is pick the lowest floor, check that it's below floor 'f', and if so then unload all of my eggs ( else hold on to them). If I have to climb floors, then while the floor I'm on is less than 'f' floor I can drop, otherwise hold on.

The first solution has O(1) complexity as we are just going after one floor, and doing a check.
The second is o(n) floors at worst if f is the at the top of the building, but allows this to be better than that if 'f' is lower than the top.

