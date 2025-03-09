from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "7 to 8 lines"
    if length == "Medium":
        return "8 to 12 lines"
    if length == "Long":
        return "12 to 18 lines"


def generate_post(length, language, tag,scenario):
    prompt = get_prompt(length, language, tag,scenario)
    response = llm.invoke(prompt)
    print(response.content)
    return response.content


def get_prompt(length, language, tag,scenario):
    length_str = get_length_str(length)

    
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    #examples = few_shot.get_filtered_posts(length, language, tag)
    prompt = '''
    generate an email by taking in consideration of the following : NO PREAMBLE
    Type : {tag}
    Length : {length_str}
    Language :  {language}
    Scenario : {scenario}
    ###
    give the response with escape sequences like \n , \t


    ######
    Example response for type Professional , 18 lines , and english: 
Dear Manager,\n
\tI am writing to inform you that, unfortunately, I will be unable to come to work for the next few days.\n
\tI am currently not feeling well and my health is not in the best condition.\n
\tI have been diagnosed with an illness that requires me to take some time off to recover.\n
\tI apologize for any inconvenience this may cause and will make sure to catch up on any missed work as soon as possible.\n
\tI will keep you updated on my status and provide a doctor's note if needed.\n
\tThe expected dates of my leave are from [start date] to [end date].\n
\tI will be available by email if anything urgent comes up while I am away.\n
\tPlease let me know if there are any pressing matters that need my attention before my leave.\n
\tI appreciate your understanding and support during this time.\n
\tIf there is anything I can do to mitigate the impact of my absence, please let me know.\n
\tI am committed to my responsibilities and will ensure a smooth transition of tasks.\n
\tI will respond to all emails and messages as soon as I am feeling better.\n
\tThank you for your consideration and I look forward to returning to work as soon as possible.\n
\tPlease do not hesitate to contact me if you have any questions or concerns.\n
\tSincerely,\n
\t[Your Name]\n
Best regards, \n
[Your Name]


    '''
    examples = []
    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Professional","permission from my teacher for a leave , for my brothers marriage"))