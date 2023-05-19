Author: Flynn Costello
SID: 530488477
Unikey: fcos0917



**Test Cases**
Table 1. Summary of test cases for `buy_cheese` function in `shop.py`. 
 ----------------------------------------------------------------------------------------------------------
| Test ID |         Description          |     Inputs     |           Expected Output             | Status |
| ------- | ---------------------------- | -------------- | ------------------------------------- | ------ |
| 01      | Positive Test Case -         | 125            |                                       | PASSED |
|         | User correctly               | "cheddar, 1"   | You have 125 gold to spend.           |        |
|         | purchases 1 cheddar          | "swiss, 1"     | State [cheese quantity]: #            |        |
|         | and 1 swiss                  | "back"         | Successfully purchase 1 cheddar.      |        |
|         |                              |                | You have 115 gold to spend.           |        |
|         |                              |                | State [cheese quantity]: #            |        |
|         |                              |                | Successfully purchase 1 swiss.        |        |
|         |                              |                | You have 15 gold to spend.            |        |
|         |                              |                | State [cheese quantity]: #            |        |
|         |                              |                |                                       |        |
|         |                              |                | (110, (1, 0, 1))                      |        |
|         |                              |                |                                       |        |
------------------------------------------------------------------------------------------------------------
| 02      | Positive Test Case -         | 125            | You have 125 gold to spend.           | PASSED |
|         | User Enters "back" to        | "back"         | State [cheese quantity]: #            |        |
|         | leave the purchase           |                |                                       |        |
|         | cheese section               |                | (0, (0, 0, 0))                        |        |
|         |                              |                |                                       |        |
------------------------------------------------------------------------------------------------------------
| 03      | Negative Test Case -         | 140            | You have 140 gold to spend.           | PASSED |
|         | User  only inputs the        | "swiss"        | State [cheese quantity]: #            |        |
|         | cheese type they want        | "back"         | Missing quantity.                     |        |
|         | (cheddar) and not the        |                | You have 140 gold to spend.           |        |
|         | quantity they want.          |                | State [cheese quantity]: #            |        |
|         |                              |                |                                       |        |
|         |                              |                | (0, (0, 0, 0))                        |        |
|         |                              |                |                                       |        |
------------------------------------------------------------------------------------------------------------
| 04      | Negative Test Case -         | 155            | You have 155 gold to spend.           | PASSED |
|         | Quantity less than           | "swiss -1"     | State [cheese quantity]: #            |        |
|         | zero given (invalid          | "back"         | Must purchase positive amount of      |        |
|         | quantity amount)             |                | cheese.                               |        |
|         |                              |                | You have 155 gold to spend.           |        |
|         |                              |                | State [cheese quantity]: #            |        |
|         |                              |                |                                       |        |
|         |                              |                | (0, (0, 0, 0))                        |        |
|         |                              |                |                                       |        |
------------------------------------------------------------------------------------------------------------
| 05      | Edge Test Case - Empty       | 165            | You have 165 gold to spend.           | PASSED |
|         | string is given when         | ""             | State [cheese quantity]: #            |        |
|         | asked for cheese type        | "back"         | We don't sell !                       |        |
|         | and quantity                 |                | You have 165 gold to spend.           |        |
|         |                              |                | State [cheese quantity]: #            |        |
|         |                              |                |                                       |        |
|         |                              |                | (0, (0, 0, 0))                        |        |
|         |                              |                |                                       |        |
------------------------------------------------------------------------------------------------------------
| 06      | Edge Test Case - Input is    | 175            | You have 175 gold to spend.           | PASSED |
|         | entered with extra spacing   | "  swiss   1 " | State [cheese quantity]: #            |        |
|         |                              | "back"         | Successfully purchase 1 swiss.        |        |
|         |                              |                | You have 75 gold to spend.            |        |
|         |                              |                | State [cheese quantity]: #            |        |
|         |                              |                |                                       |        |
|         |                              |                | (100, (0, 0, 1))                      |        |
|         |                              |                |                                       |        |
------------------------------------------------------------------------------------------------------------
| 07      | Edge Test Case - Input is    | 185            | You have 185 gold to spend.           | PASSED |
|         | provided as a list           | "[swiss 1]"    | State [cheese quantity]: #            |        |
|         |                              | "back"         | We don't sell [swiss,!                |        |
|         |                              |                | You have 185 gold to spend.           |        |
|         |                              |                | State [cheese quantity]: #            |        |
|         |                              |                |                                       |        |
|         |                              |                | (0, (0, 0, 0))                        |        |
|         |                              |                |                                       |        |
------------------------------------------------------------------------------------------------------------
| 08      | Edge Test Case - Inputting   | 195            | You have 195 gold to spend.           | PASSED |
|         | an extremely large quantity  | "swiss 9999999 | State [cheese quantity]: #            |        |
|         |                              | 9999999999999" | Insufficient gold.                    |        |
|         |                              | "back"         | You have 195 gold to spend.           |        |
|         |                              |                | State [cheese quantity]: #            |        |
|         |                              |                |                                       |        |
|         |                              |                | (0, (0, 0, 0))                        |        |
|         |                              |                |                                       |        |
 ----------------------------------------------------------------------------------------------------------

 

Table 2. Summary of test cases for `change_cheese` function in `game.py`.
 -------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Test ID | Description            | Inputs                                                 |                        Expected Output                       | Status |
| ------- | ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| 01      | Positive Test Case -   | "Flynn"                                                | Hunter Flynn, you currently have:                            | PASSED |
|         | Player has 1 cheddar   | [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]          | Cheddar - 1                                                  |        |
|         | and successfully sets  | "Cardboard and Hook Trap"                              | Marble - 0                                                   |        |
|         | trap with cheddar      | False                                                  | Swiss - 0                                                    |        |
|         |                        |                                                        |                                                              |        |
|         |                        | "cheddar"                                              | Type cheese name to arm trap: #                              |        |
|         |                        | "yes"                                                  | Do you want to arm your trap with Cheddar? #                 |        |
|         |                        |                                                        | Cardboard and Hook Trap is now armed with Cheddar!           |        |
|         |                        |                                                        |                                                              |        | 
|         |                        |                                                        | (True, "Cheddar")                                            |        | 
|         |                        |                                                        |                                                              |        | 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------      
| 02      | Positive Test Case -   | "Dan"                                                  | Hunter Dan, you currently have:                              | PASSED |
|         | Player has 1 marble    | [["Cheddar", 0], ["Marble", 1], ["Swiss", 0]]          | Cheddar - 0                                                  |        |
|         | but chooses not to     | "Carboard and Hook Trap"                               | Marble - 1                                                   |        |
|         | arm the trap at first. | False                                                  | Swiss - 0                                                    |        |
|         | When asked a second    |                                                        |                                                              |        |
|         | time they choose to    | "marble"                                               | Type cheese name to arm trap: #                              |        |
|         | arm the trap           | "no"                                                   | Do you want to arm your trap with Marble? #                  |        |
|         |                        | "marble"                                               |                                                              |        |
|         |                        | "yes"                                                  | Hunter Dan, you currently have:                              |        |
|         |                        |                                                        | Cheddar - 0                                                  |        |
|         |                        |                                                        | Marble - 1                                                   |        |
|         |                        |                                                        | Swiss - 0                                                    |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | Type cheese name to arm trap: #                              |        |
|         |                        |                                                        | Do you want to arm your trap with Marble? #                  |        |
|         |                        |                                                        | Carboard and Hook Trap is now armed with Marble!             |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | (True, "Marble")                                             |        |
|         |                        |                                                        |                                                              |        |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 03      | Negative Test Case -   | "Joe"                                                  | Hunter Joe, you currently have:                              | PASSED |
|         | Invalid cheese name    | [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]          | Cheddar - 1                                                  |        |
|         | is entered, then back  | "Carboard and Hook Trap"                               | Marble - 0                                                   |        |
|         | is entered             | False                                                  | Swiss - 0                                                    |        |
|         |                        |                                                        |                                                              |        |
|         |                        | "camembert"                                            | Type cheese name to arm trap: #                              |        |
|         |                        | "back"                                                 | No such cheese!                                              |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | Hunter Joe, you currently have:                              |        |
|         |                        |                                                        | Cheddar - 1                                                  |        |
|         |                        |                                                        | Marble - 0                                                   |        |
|         |                        |                                                        | Swiss - 0                                                    |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | Type cheese name to arm trap: #                              |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | (False, None)                                                |        |
|         |                        |                                                        |                                                              |        |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 04      | Negative Test Case -   | "Zac"                                                  | Hunter Zac, you currently have:                              | PASSED |
|         | When asked if they     | [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]          | Cheddar - 1                                                  |        |
|         | want to arm the trap,  | "Carboard and Hook Trap"                               | Marble - 0                                                   |        |
|         | the user enters a      | False                                                  | Swiss - 0                                                    |        |
|         | random word ("hello")  |                                                        |                                                              |        |
|         |                        | "hello"                                                | Type cheese name to arm trap: #                              |        |
|         |                        | "back"                                                 | No such cheese!                                              |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | Hunter Zac, you currently have:                              |        |
|         |                        |                                                        | Cheddar - 1                                                  |        |
|         |                        |                                                        | Marble - 0                                                   |        |
|         |                        |                                                        | Swiss - 0                                                    |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | Type cheese name to arm trap: #                              |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | (False, None)                                                |        |
|         |                        |                                                        |                                                              |        |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 05      | Edge Test Case -       | "Daniel"                                               | Hunter Daniel, you currently have:                           | PASSED |
|         | Empty string entered   | [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]          | Cheddar - 1                                                  |        |
|         | when user is asked     | "Carboard and Hook Trap"                               | Marble - 0                                                   |        |
|         | what cheese they want  | False                                                  | Swiss - 0                                                    |        |
|         | to put on the trap     |                                                        |                                                              |        |
|         |                        | ""                                                     | Type cheese name to arm trap: #                              |        |
|         |                        | "back"                                                 | No such cheese!                                              |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | Hunter Daniel, you currently have:                           |        |
|         |                        |                                                        | Cheddar - 1                                                  |        |
|         |                        |                                                        | Marble - 0                                                   |        |
|         |                        |                                                        | Swiss - 0                                                    |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | Type cheese name to arm trap: #                              |        |
|         |                        |                                                        |                                                              |        |
|         |                        |                                                        | (False, None)                                                |        |
|         |                        |                                                        |                                                              |        |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 06      | Edge Test Case -       | "Sophie"                                               | Hunter Sophie, you currently have:                           | PASSED |
|         | Extra spacing when     | [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]          | Cheddar - 1                                                  |        |
|         | choosing cheddar and   | "Carboard and Hook Trap"                               | Marble - 0                                                   |        |
|         | saying yes             | False                                                  | Swiss - 0                                                    |        |
|         |                        |                                                        |                                                              |        |
|         |                        | "     cheddar     "                                    | Type cheese name to arm trap: #                              |        |
|         |                        | "  yes  "                                              | Do you want to arm your trap with Cheddar? #                 |        |
|         |                        |                                                        | Carboard and Hook Trap is now armed with Cheddar!            |        |
|         |                        |                                                        |                                                              |        |                                                                      |        |
|         |                        |                                                        | (True, "Cheddar")                                            |        |
|         |                        |                                                        |                                                              |        |
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------





