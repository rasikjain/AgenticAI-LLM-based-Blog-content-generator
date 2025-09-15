from os import system
from src.states.blogstate import Blog, BlogState
from langchain_core.messages import HumanMessage, SystemMessage


class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt = """
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the "{topic}". \n\n 
                   Title should be short and write only one sentence. 
                   

                   """

            sytem_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(sytem_message)
            return {"blog": {"title": response.content}}

    def content_generation(self, state: BlogState):
        """
        Generate the content for the blog based on topic and title
        """

        if "topic" in state and state["topic"]:

            system_prompt = """
            You are expert blog writer. Use markdown formatting.
            Generate a detailed blog content with the detailed breakdown for the topic {topic}
            """

            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {
                "blog": {"title": state["blog"]["title"], "content": response.content}
            }

    def translation(self,state:BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt="""
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL TITLE:
        {blog_title}
        
        ORIGINAL CONTENT:
        {blog_content}

        """
        blog_content=state["blog"]["content"]
        blog_title=state["blog"]["title"]
        
        messages=[
            HumanMessage(translation_prompt.format(current_language=state["current_language"], blog_content=blog_content, blog_title=blog_title))

        ]
        transaltion_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog": transaltion_content}


    def route(self, state: BlogState):
        return {"current_language": state["current_language"]}

    def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french": 
            return "french"
        else:
            return state['current_language']