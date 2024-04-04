from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import Highlights_Tasks
from agents import Highlights_Agents


tasks = Highlights_Tasks()
agents = Highlights_Agents()

print("## Welcome to Highlights of game releases")
print('-------------------------------')
game = input("What is the game you would like to get highlights about the new release? \n")


# Create Agents
Game_agent = agents.Game_agent()
Write_agent = agents.Write_agent()


# Create Tasks
game_release = tasks.Game_task(Game_agent, game)
game_highlights = tasks.Highlights_task(Write_agent, game)


# Create Crew responsible for Copy
crew = Crew(
	agents=[
		Game_agent,
		Write_agent
	],
	tasks=[
		game_release,
		game_highlights
	],
	verbose=True
)

result = crew.kickoff()


# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("Your Highlights:")
file_path = "output.txt"
with open(file_path, 'w') as file:

    file.write(result)

print("Output has been written to", file_path)

print(result)