from textwrap import dedent
from crewai import Task

class Highlights_Tasks():
	def Game_task(self, game):
		return Task(
			description=dedent(f"""\
							Analyze and find all the new {game} releases
							Using this releases you will make a youtube video that show all the new highlights of the game release"""),


		)

	def Highlights_task(self, game):
		return Task(

			description=dedent(f"""\
						now you will summurize the highlights about the new {game} release.
						write the highlights to a flie that i can use when i make my youtube video."""),

		)
