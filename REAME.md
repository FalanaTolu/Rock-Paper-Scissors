# Rock-Paper-Scissors

Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors.

In this version, one player is controlled by the computer and the other player is controlled the user. When the program is run, the user is asked to pick an option between "R", "P" or "S", where "R" stands for "rock", "P" for "paper", and "S" for "scissors". 

If user input is invalid (not amongst our options), an error is printed, and user input has to be entered again. The `choice` function from the inbuilt Python `random` module was used to make a choice for CPU player(computer).Players' moves are printed in the format: `Player (Rock) : CPU (Paper)`

If there is a winner, the winner is indicated, and the program ends. If it's a tie (the computer and player pick the same move) the game is restarted.