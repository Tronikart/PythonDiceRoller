import random

def roll(dice):
	endResult = {}
	result = 0
	#################
	# It is a string
	#################
	if type(dice) == str:
		numberDice = int(dice.split('d')[0])
		modifier = 0 if len(dice.split('+')) < 2 else int(dice.split('+')[1])
		##############
		# Its xDy form
		###############
		if len(dice.split('d')) == 2:
			dieNumber = int(dice.split('d')[1]) if modifier == 0 else int(dice.split('+')[0].split('d')[1])
			###################
			# Only one die roll
			###################
			if numberDice == 1:
				endResult['multipleResult'] = False
				result = random.randrange(numberDice, dieNumber + 1)
				endResult['dice'] = str(result)
			###################
			# Several Die Roll
			###################
			else:
				endResult['multipleResult'] = True
				endResult['dice'] = ""
				# Avoiding negative numbers
				i = numberDice if numberDice > 0 else -numberDice
				i += 1
				result = 0
				# Going through all the dice rolls, at the end, delete the extra ' + ' and break
				while(True):
					if i > 0:
						aux = random.randrange(1, dieNumber + 1)
						result += aux
						if i == numberDice:
							pass
						else:
							endResult['dice'] += str(aux) + " + "
						i -= 1
					else:
						endResult['dice'] = endResult['dice'][:len(endResult['dice'])-3]
						break
		##################
		# Its xDyDyDy form
		##################
		else:
			endResult['multipleResult'] = True
			dieNumber = int(dice.split('d')[1]) if modifier == 0 else int(dice.split('+')[0].split('d')[1])
			###################
			# Only one die roll
			###################
			if numberDice == 1:
				#endResult['multipleResult'] = True
				auxResult = random.randrange(numberDice, dieNumber + 1)
				#endResult['dice'] = str(auxResult)
			###################
			# Several Die Roll
			###################
			else:
				endResult['multipleResult'] = True
				endResult['dice'] = ""
				i = numberDice if numberDice > 0 else -numberDice
				i += 1
				auxResult = 0
				while(True):
					if i > 0:
						i -= 1
						aux = random.randrange(1, dieNumber + 1)
						auxResult += aux
					else:
						break
			# Recursively handling more than one dice roll
			recur = roll(str(auxResult) + dice[3:].split('+')[0])
			endResult['dice'] = ""
			if recur['error'] == False:
				result += recur['total']
				endResult['dice'] += recur['dice']
			else:
				endResult['error'] = True
		# Useful flags for printing info
		# Crit, fail, the dice that were added, if there was any error
		endResult['crit'] = True if result == dieNumber else False
		endResult['fail'] = True if result == 1 else False
		endResult['total'] = result + modifier
		endResult['dice'] = endResult['dice'] + " + (" + str(modifier) + ")" if modifier > 0 else endResult['dice']
		endResult['error'] = False
	elif type(dice) == int:
		modifier = 0
		endResult['total'] = random.randrange(1, dice+1)
		endResult['error'] = False
		endResult['multipleResult'] = False
	else:
		endResult['error'] = True
	if endResult['error']:
		pass
	else:
		endResult['multipleResult'] = True if modifier > 0 else endResult['multipleResult']
	return endResult

