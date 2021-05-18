# CRYPTO MINER
Implemented Blockchain Technology Using Python. Used SHA256 Algorithm From **hashlib** Python Library. It Mines Cryptocurrency By Using The Maximum Computational Power As A Limit And Verifying The New Hash Value.

## STEP BY STEP WORKING OF THE CODE :-
1. All The Required Parameters Involving **block_number, transactions, previous_hash, prefix_zeroes** Are Provided In The **mine ( )** Function. 
2. Then The **mine ( )** Function Is Called, A Text Is Passed Through The **SHA256 ( )** Function To Convert The Text To SHA256 Type. 
3. The **mine ( )** Function Then Checks If The **" difficulty "** Variable's Value Is Equal To Number Of Zeroes At Start Of The **" new_hash "** Value. 
4. If Equal, It Returns The New Hash As Well As The Current Nonce Value. 
5. Otherwise Raises An **BaseException**.
6. Finally After Mining, It Prints The Following :- <br>
&emsp; a. Nonce Value (At Which The New Hash Got Verified). <br>
&emsp; b. Total Time (Total Time Taken To Mine A Single Block). <br>
&emsp; c. New Hash Value (Verified New Hash Value).

## KEY POINTS :-
1. By Changing The " difficulty " Variable's Value, Anyone Can Change **The Mining Difficulty** According To Their Requirements. <br>
2. By Changing The " MAX_NONCE " Variable's Value, Anyone Can Change **The Maximum Computational Power** According To Their System Specifications.

## NOTE :-
1. Zeroes Before The Hash Value To Be Verified Determines The Mining Difficulty.
2. **" MAX_NONCE "** Variable Here Determines The Maximum Computation Power.
