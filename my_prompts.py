file_map = """
You will be given a single section from a text. This will be enclosed in triple backticks.
Please provide a cohesive summary of the following section excerpt, focusing on the key points and main ideas, while maintaining clarity and conciseness.

'''{text}'''

FULL SUMMARY:
"""


file_combine = """
You are a studynote bot. You read all the provided summaries from a larger document. They will be enclosed in triple backticks. 
You create detailed point-wise summary including topics and sub-topics given the transcript of the session. 
They can be the part of the transcript of the recorded session in a university. Format in HTML. Text should be divided into paragraphs. Paragraphs should be indented.
Make sure you include topic/subtopic in your study notes:

'''{text}'''


"""

youtube_map = """
You will be given a single section from a transcript of a youtube video. This will be enclosed in triple backticks.
Please provide a cohesive summary of the section of the transcript, focusing on the key points and main ideas, while maintaining clarity and conciseness.

'''{text}'''

FULL SUMMARY:
"""


youtube_combine = """
Read all the provided summaries from a youtube transcript. They will be enclosed in triple backticks.
Determine what the overall video is about and summarize it with this information in mind. 
Synthesize the info into a well-formatted easy-to-read synopsis, structured like an essay that summarizes them cohesively. 
Do not simply reword the provided text. Do not copy the structure from the provided text.
Avoid repetition. Connect all the ideas together.
Preceding the synopsis, write a short, bullet form list of key takeaways.
Format in HTML. Text should be divided into paragraphs. Paragraphs should be indented. 

'''{text}'''


"""