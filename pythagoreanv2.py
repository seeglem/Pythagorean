#I'mgonnabetheverybestlikenooneeverwastocatchthemwasmyrealtesttotrainthemismycauseiwilltravelacrossthelandsearchingfarandwideteachpokemonthepowerthat'sinsidePokemongottacatch'emallItsyouandmeIknowit'smydestinyPokemonohyou'remybestfriendInaworldwemustdefendPokemongottacatch'emallaheartsotrueourcouragewillpullusthroughyouteachmeandI'llteachyouPokemon,gottacatch'emallgottacatch'emallyeaheverychallengealongthewaywithcourageIwillfaceIwillbattleeverydaytoclaimmyrightfulplacecomewithmethetimeisrightthere'snobetterteamarminarmwe'llwinthefightit'salwaysbeenourdreamPokemon,gottacatch'emallitsyouandmeIknowit'smydestinyPokemonohyou'remybestfriendinaworldwemustdefendPokemongottacatch'emallaheartsotrueourcouragewillpullusthroughyouteachmeandI'llteachyouPokemongottacatch'emallgottacatch'emallgottacatch'emallgottacatch'emallyeah

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Pythagoreanv2.py by Hunter Cole Seglem
Purpoise:
	This program will solve any problem you have relating to 
	not knowing the hypotenuse, height, or base of any given right triangle.
Input:
	Please input the desired side that you are having difficulty finding
	and then follow the prompts by inputing the known side lengths, and,
	like magic, this program will pump out the missing side, so that you
	can have a nice, whole triangle.
Notes:
	This is the version 2 of my code, where version 1 only solved the
	hypotenuse, this code will allow you to solve the height, and the base
	as well.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#I imported all of math, to help with math related problems we may otherwise have
import math







"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
			hypTheorem, baseTheorem, heightTheorem

					hypTheorem(iBase, iHeight)
					baseTheorem(iHeight,iHypotenuse)
					heightTheorem(iBase,iHypotenuse)
Purpoise:
	These functions are the only math in this program. They
	are made to execute the pythagorean theorem a**2+b**2=c**2
Parameters:
	I szBaseCzech
	I szHeightCzech
	I szHypotenuseCzech
Returns:
	iHypotenuse
	iBase
	iHeight

Notes:
	Version 2 now offers 3x the amount of returns! Wow!


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#I defined all of my functions right below this comment. This is the part of the code where the math lives, all warm and cozy between it's parentheses.


def hypTheorem(iBase, iHeight):
	iHypotenuse=math.sqrt((iBase**2)+(iHeight**2))
	return iHypotenuse

def baseTheorem(iHeight, iHypotenuse):
	iBase=math.sqrt((iHypotenuse**2)-(iHeight**2))
	return iBase

def heightTheorem(iBase, iHypotenuse):
	iHeight=math.sqrt((iHypotenuse**2)-(iBase**2))
	return iHeight

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
This part of the code was the trickiest. It is a bunch of if/elif statements
which executes different functions depending on what the user inputs.
There are double the amount of statements than necessary, because I don't
know how to differentiate upper and lower case letters yet, so this is the only
way I know of to improve functionality. There is also a while loop in there, which
let's you retry input in case you mess up the first time.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

iCount=0

while(iCount==0):
	#This part of the code is where I am asking the question outlined in the header about your unknown variables, from which
	#I will then solve the rest of the problem, with the function outlined above, shown by hypTheorem, baseTheorem, and heightTheorem: 
	szFirstPrompt=input("Would you like to find the Base, Height, or Hypotenuse? ")
	iCount=1
	if szFirstPrompt==("Hypotenuse"):
		szBaseCzech=input("Enter your base here: ")
		szHeightCzech=input("Enter your height here: ")
		iBaseCzech=int(szBaseCzech)
		iHeightCzech=int(szHeightCzech)
		iHypAnswer=hypTheorem(iBaseCzech,iHeightCzech)
		print (iHypAnswer)

	elif szFirstPrompt==("Base"):
		szHypotenuseCzech=input("Enter your hypotenuse here: ")
		szHeightCzech=input ("Enter your Height here: ")
		iHypotenuseCzech=int(szHypotenuseCzech)
		iHeightCzech=int(szHeightCzech)
		iBaseAnswer=baseTheorem(iHeightCzech,iHypotenuseCzech)
		print (iBaseAnswer)

	elif szFirstPrompt==("Height"):
		szHypotenuseCzech=input("Enter your hypotenuse here: ")
		szBaseCzech=input ("Enter your base here: ")
		iHypotenuseCzech=int(szHypotenuseCzech)
		iBaseCzech=int(szBaseCzech)
		iHeightAnswer=heightTheorem(iBaseCzech,iHypotenuseCzech)
		print (iHeightAnswer)

	elif szFirstPrompt==("hypotenuse"):
		szBaseCzech=input("Enter your base here: ")
		szHeightCzech=input("Enter your height here: ")
		iBaseCzech=int(szBaseCzech)
		iHeightCzech=int(szHeightCzech)
		iHypAnswer=hypTheorem(iBaseCzech,iHeightCzech)
		print (iHypAnswer)

	elif szFirstPrompt==("base"):
		szHypotenuseCzech=input("Enter your hypotenuse here: ")
		szHeightCzech=input ("Enter your Height here: ")
		iHypotenuseCzech=int(szHypotenuseCzech)
		iHeightCzech=int(szHeightCzech)
		iBaseAnswer=baseTheorem(iHeightCzech,iHypotenuseCzech)
		print (iBaseAnswer)

	elif szFirstPrompt==("height"):
		szHypotenuseCzech=input("Enter your hypotenuse here: ")
		szBaseCzech=input ("Enter your base here: ")
		iHypotenuseCzech=int(szHypotenuseCzech)
		iBaseCzech=int(szBaseCzech)
		iHeightAnswer=heightTheorem(iBaseCzech,iHypotenuseCzech)
		print (iHeightAnswer)
	else:
		print('Incorrect Entry. Please specify either "Hypotenuse," "Base," or "Height."')
		iCount=0

"""""""""""""""""
That's all folks
"""""""""""""""""

