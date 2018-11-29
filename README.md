# DiscreteMath-Fall2018-Prime-NUmbers
This is the PRIME NUMBER PROJECT
By Chris Calloway and Jennifer Lee
 For the Graders:
 The relevant code is broken up into the followin files:
Menu.py( which is like bascially the main class)
Sieve.py
gen_image.py
Primality.py
GCD.py
 prime_distribution.py
 prime_factorization.py
 Non Code:
 primes1.txt (downloaded from online)
Report.pdf
This contains some of the answers to the questions posed for the report.
 Note:
The menu is a class that has only been tested for Windows devices. If the GUI does not appear please just run code from their respective files (hence why it was built with this multi-file depedency to safegaurd in the case the menu module was Unix Based system incompatible.
 Work Division:
Chris did the problems 1,2,3,6,7 and set up this Github repo.
Jennifer did questions 4 and 5. In terms of the diffuculty of the questions, this
was decided mutally to be as balanced as we could predict before starting. However,
the work was tranpsort and mutally edited by the nature of this public repo.
Chris: 1,2,3,6,7
Jennifer: 4,5
 ===================================================================================
 Notes on Q4, Q5:
 For Q4 and Q5, the results are done when program is run and shown in tables as text output in the python program. As a result, the values used in those examples are minimized (e.g. prime factorization past 8 digits takes a significantly longer time) so the user does not have to wait too long. When more values are run it becomes clearer for Q4.5 that the graph of π(x) appears to increase in a logarithmic form and for Q5.5 it appeared that the time it takes to calculate the factorization would increase exponentially.
 ===================================================================================
For Developers:
 Setup: For the visualization code:
 $pip install Pillow
 $pip install Matplotlib
 $pip install PrettyTable
 You might have to uninstall PIL (because Anaconda was moronic in how they installed this)
