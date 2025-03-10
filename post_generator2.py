from llm_helper import llm

def get_length_str(length):
    if length == "Short":
        return "1 paragraph"
    if length == "Medium":
        return "2 to 3 paragraphs"
    if length == "Long":
        return "4 to 5 paragraph"


def generate_post(prompt):
    response = llm.invoke(prompt)
    #print(response.content)
    return response.content

def get_modified_response(modification_request):
    response = generate_post(modification_request)
    return response


def get_prompt(length, language, tag,scenario,sender,receiver):
    length_str = get_length_str(length)

    prompt = '''
        Generate an email in HTML format for display on a website. Follow these rules: NO PREAMBLE  
        1. **Type**: {tag}
        2. **Length**:{length_str}  
        3. **Language**:  {language}
        4. **Scenario**: {scenario}
        5. **Sender's Name** : {sender}
        6. **Receiver's Name/Designation** : {receiver}


        **Requirements**:  
        - Wrap the entire email in a `<div class='email-template'>` tag.  
        - Use `<p class="email-para">` tags for paragraphs and `<br>` for line breaks .
        - Each paragraph must be  minimum of 4-5 lines  
        - Highlight placeholders like [Name] with `<span class='placeholder'>[Name]</span>`.  
        - Include a subject line inside `<p class='subject'>`.  
        - Preserve indentation and line breaks using proper HTML (no Markdown).  
        Return **only the HTML code**, no explanations.

        ** Modified Request (If Available -> Only change Mentioned Changes , No confirmation needed—proceed immediately ) ** 


    '''.format(tag=tag, length_str=length_str, language=language, scenario=scenario,sender=sender,receiver=receiver)
    # examples = []
    # if len(examples) > 0:
    #     prompt += "4) Use the writing style as per the following examples."

    # for i, post in enumerate(examples):
    #     post_text = post['text']
    #     prompt += f'\n\n Example {i+1}: \n\n {post_text}'

    #     if i == 1: # Use max two samples
    #         break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Professional","permission from my teacher for a leave , for my brothers marriage","Vamshi","Rama Krishnan"))