import openai

API_KEY ="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"

openai.api_key = API_KEY

def chatgptresponse(conversation):
    try:
        reponse = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=conversation
        )
    except openai.error.APIConnectionError:
        return None
    
    conversation.append({'role':response.choices[0].message.role, 'content':response.choices[0].message.content})
    return conversation
    
def initializationConversation():
    global conversation
    conversation=[]
    conversation.append({'role':'system','content':'How may I help you?'})
    conversatinon = chatGPTResponse(conversation)

#Function that returns the response
def getResponse(prompt):
    global conversation
    conversation.append({'role':'user','content':prompt})
    conversation = chatGPTResponse(conversation)

    return conversation[-1]['content'].strip()
    #strip use to turncate white spaces