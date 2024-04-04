from textwrap import dedent
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

search_tool = SerperDevTool()


class Highlights_Agents():
    def Game_agent(self):
        return Agent(
            role='New Releases of the game',
            goal='Find all the new games',
            backstory=dedent("""\
				You are a youtube creator and you want to make new video.
				You need to find all the new releases of games"""),
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        )

    def Write_agent(self):
        return Agent(
            role='Write all the highlights of the game',
            goal='After you find the new releases of the game write highlights about it',
            backstory=dedent("""\
						You need to write all the highlights about the new release of the game and about the new features"""),
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        )
