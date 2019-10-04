import string
def DeKod(kod):
	if kod[0] == '0':
		if kod[1] == '1':
			a='S'

		elif kod[1] == '2':
			a='s'

		elif kod[1] == '3':
			a='P'

		elif kod[1] == '4':
			a='p'

		elif kod[1] == '5':
			a='С'

		elif kod[1] == '6':
			a='с'

		elif kod[1] == '7':
			a='П'

		elif kod[1] == '8':
			a='п'
		elif kod[1] == '9':
			a='С'#рус
	if kod[0] == '1':
		if kod[1] == '0':
			a='с'#рус
			print(kod)
		if kod[2] == '0':
			if kod[3] == '1':
				a=a+'e'

			elif kod[3] == '2':
				a=a+'е'#рус

			elif kod[3] == '3':
				a=a+'o'

			elif kod[3] == '4':
				a=a+'и'#рус

			elif kod[3] == '5':
				a=a+'о'#рус

		if kod[4] == '0':
			if kod[5] == '1':
				a=a+'к'#рус

			elif kod[5] == '2':
				a=a+'x'

			elif kod[5] == '3':
				a=a+'з'#рус

			elif kod[5] == '4':
				a=a+'р'#рус

			elif kod[5] == '5':
				a=a+'r'#рус

		if kod[6] == '0':
			if kod[7] == '1':
				a=a+''

			elif kod[7] == '2':
				a=a+'с'#рус

			elif kod[7] == '3':
				a=a+'д'#рус

			elif kod[7] == '4':
				a=a+'n'

			elif kod[7] == '5':
				a=a+'н'

		if kod[8] == '0':
			if kod[9] == '1':
				a=a+''

			elif kod[9] == '2':
				a=a+'а'#рус

			elif kod[9] == '3':
				a=a+'о'#рус

			elif kod[9] == '4':
				a=a+'o'
		kod=a
	return(kod)
