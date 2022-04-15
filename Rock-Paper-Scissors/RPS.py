# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# Got my idea from -> https://forum.freecodecamp.org/t/rock-paper-scissors-project-proper-completion/473440
import math
import numpy as np
def player(prev_play, opponent_history=[]):
	guess = "R"	
	answer = { 'R': 'P', 'P': 'S', 'S': 'R' }
	if prev_play:
		opponent_history.append(prev_play)
	else:
		opponent_history.clear()
	if len(opponent_history) >= 4:			
		playlist = []
		for i in range(len(opponent_history)):
			if (len(opponent_history[i:i+4]) == 4):
				playlist.append("".join(opponent_history[i:i+4]))

		potential_play = ["".join(opponent_history[-3:]) +"S" , 
										 	"".join(opponent_history[-3:]) +"P",
										 	"".join(opponent_history[-3:]) +"R"]
		
		counter = { k: playlist.count(k) for k in potential_play }
		prediction = max(counter, key=counter.get)[-1]
		ans1= answer[prediction]
		playlist = np.array(playlist)
		playlist = playlist[(playlist ==potential_play[0])  |  (playlist ==potential_play[1])  | (playlist ==potential_play[2])]
		if playlist.size != 0:
			play = np.unique(playlist, return_counts=True)[1].argmax()
			guess = answer[np.unique(playlist, return_counts=True)[0][play][-1]]
		else:
			guess = "P"
	return guess

