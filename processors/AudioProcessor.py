import logging
import time
import traceback
from langchain.llms.ollama import Ollama
from utils import threaded, Singleton
from langchain.agents import AgentExecutor, create_react_agent, Tool
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory, ConversationSummaryMemory

from sensors import AudioSensor
from motors import AudioMotor

template = """
    You are a Personal Assistant. Your name is Leo. You will talk with human like a friend.
    Sometimes, you may hear your own voice, but you should ignore it.
    Incase you need to wait for the next human input, you can use the tool `wait_and_get_next_human_input`.
    Incase you need to talk with human, you can use the tool `convert_assistant_response_to_voice_and_talk_with_human`.

    TOOLS:
    ------

    You has access to the following tools:

    {tools}

    To use a tool, please use the following format:

    ```
    Thought: Do I need to use a tool? Yes
    Action: the action to take, should be one of [{tool_names}].
    Action Input: the input to the action
    Observation: the result of the action
    ```

    When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

    ```
    Thought: Do I need to use a tool? No
    Final Answer: Your response
    ```

    Begin!

    Previous conversation history:
    {chat_history}

    New input: {input}
    {agent_scratchpad}
"""



class AudioProcessor(Singleton):
    _llm = None
    _prompt = None
    _agent = None
    _executor: AgentExecutor = None
    _tools = None
    _memory = None

    @staticmethod
    @threaded
    def start():
        instance = AudioProcessor()
        instance.config()
        instance.__process()
        return instance

    def config(self):
        if not self._llm:
            self._llm = Ollama(model="llama2")

        if not self._prompt:
            self._prompt = PromptTemplate.from_template(template)

        if not self._tools:
            def wait_and_get_next_human_input(input):
                time.sleep(3)
                return AudioSensor.get()

            def talk_with_human(input):
                AudioMotor.speak(input)

                response = wait_and_get_next_human_input("")

                observation = "Assistant is talking now." if response == "" else response

                return f"Observation: {observation}"


            self._tools = [
                Tool("wait_and_get_next_human_input", func=wait_and_get_next_human_input, description="Wait for the next human input or finish the talk"),
                Tool("convert_assistant_response_to_voice_and_talk_with_human", func=talk_with_human, description="Convert Assistant's response to voice and talk with the human", )
            ]
        if not self._memory:
            self._memory = ConversationBufferWindowMemory(memory_key="chat_history", k=10, input_key="input")

        if not self._agent:
            self._agent = create_react_agent(llm=self._llm, prompt=self._prompt, tools=self._tools)

        if not self._executor:
            self._executor = AgentExecutor(
                agent=self._agent, 
                tools=self._tools, 
                verbose=True, 
                memory=self._memory,
                handle_parsing_errors=True,
                max_iterations=10,
            )


    def __process(self):
        logging.info("Starting...")
        AudioSensor.start()

        while True:
            try:
                time.sleep(1)
                text = AudioSensor.get()

                if not text or text == "":
                    continue

                response = self._executor.invoke(input={"input": text})
                message = response.get("output", None)

                if message:
                    AudioMotor.speak(message)
                
    
            except Exception as e:
                logging.error(e)
                traceback.print_exc()
        
