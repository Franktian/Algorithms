AAD Consensus Algorithms
==========
This repo contains a practice implementation of the first algorithm presented in the publication:
"Optimal Resilience Asynchronous Approximate Agreement" by Ittai Abraham, Yonatan Amit, and Danny Dolev
Implemented by Tamaki Sakura and stored at Frank Tian's Repository.

This Algorithm is a Approxiamte Agreement Algorithm on a Message Passing Model with FIFO input queue operated on real value.
It is designed to deal against Byzantine Failure, which is a more generalized and malicious failure compare to the more common crash failure. 
It is 4t + 1 resiliant i.e. If you have n agents trying to reach an approximate agreement, this algorithm allow at most (n - 1) / 4 of them can have Byzantien Failure while still providing you the correct result. 
More details can be found in their original publications.

Feel Free to contact me if you have any doubt about it and/or find any problem with my implementation.
