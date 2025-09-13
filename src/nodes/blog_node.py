from os import system
from src.states.blogstate import BlogState


class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self,state:BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the "{topic}". \n\n 
                   Title should be short and write only one sentence. 
                   

                   """
            
            sytem_message=prompt.format(topic=state["topic"])
            print(sytem_message)
            response=self.llm.invoke(sytem_message)
            print(response)
            return {"blog":{"title":response.content}}

    def title_creation11(self, state: BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            
            prompt = """
            You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the "{topic}". 
            This title should be creative and SEO friendly
            
            """

            system_message = prompt.format(topic=state["topic"])
            respone = self.llm.invoke(system_message)
            print('TITLECONTENT')
            print(respone.content)
            return {"blog": {"title": respone.content}}
        
    def content_generation(self, state: BlogState):
        '''
        Generate the content for the blog based on topic and title
        '''
        
        if "topic" in state and state["topic"]:
            
            system_prompt = """
            You are expert blog writer. Use markdown formatting.
            Generate a detailed blog content with the detailed breakdown for the topic {topic}
            """
            
            system_message = system_prompt.format(topic = state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']["title"], "content": response.content}}
