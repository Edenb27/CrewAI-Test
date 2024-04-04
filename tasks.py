from textwrap import dedent
from crewai import Task

class Highlights_Tasks():
	def Game_task(self, agent, game):
		return Task(
					description=dedent(f"""\
									Analyze and find all the new {game} releases and Using this releases you will make 
									a youtube video that show all the new highlights of the game release"""),
					expected_output='A new releases of the game',

					agent=agent
		)

	def Highlights_task(self, agent, game):
		return Task(

					description=dedent(f"""\
								now you will summarize the highlights about the new {game} release. write the 
								highlights to a flier that i can use when i make my youtube video."""),
					expected_output='Highlights of the new game release',

					agent=agent
		)
