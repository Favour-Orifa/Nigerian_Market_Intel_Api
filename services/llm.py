import time
import anthropic
import openai
from config import *
from models import MarketResponse

def get_market_intelligence(question: str, provider: str) -> MarketResponse:
    begin_time = time.time()
    
    prompt = """you are a Nigerian Market intelligent assistant, and you job is to give factual,
                structured answers about nigerian market, finance and market conditions"""
    
    # 3. call the right LLM based on provider
    if provider =="anthropic":
       client = anthropic.Anthropic(api_key = ANTHROPIC_API_KEY)
       response = client.messages.create(
           model= ANTHROPIC_MODEL,
           max_tokens = MAX_TOKEN_VALUE,
           system = prompt,
           messages = [{"role": "user", "content": question}]
    )
     

    elif provider == "openai":
        client = openai.OpenAI(api_key = OPENAI_API_KEY)
        response = client.chat.completions.create(
            model = OPENAI_MODEL,
            max_tokens= MAX_TOKEN_VALUE,
            messages = [{"role": "system", "content": prompt},
                        {"role":"user","content": question} ]
        )

    else:
        client = openai.OpenAI(api_key= OPENROUTER_API_KEY, base_url= "https://openrouter.ai/api/v1")
        response = client.chat.completions.create(
            model = OPENROUTER_MODEL,
            max_tokens = MAX_TOKEN_VALUE,
            messages = [{"role": "system", "content": prompt},
                        {"role":"user", "content": question}]
        )   

        
        
    
    # 4. extract the answer from the response
    if provider == "anthropic":
        answer  = response.content[0].text
    else:
        answer = response.choices[0].message.content    

    # 5. calculate response time
    response_time = (time.time() - begin_time) * 1000

    
    # 6. calculate cost
    if provider == "anthropic":
       input_tokens = response.usage.input_tokens
       output_tokens = response.usage.output_tokens
       token_used = input_tokens + output_tokens
       cost = (input_tokens * 0.000003) + (output_tokens *0.000013 )
    else:
        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
        token_used = input_tokens + output_tokens
        cost = (input_tokens * 0.000003) + (output_tokens * 0.000015)         

    

    
    return MarketResponse(answer=answer, response_time_ms=response_time, tokens_used=token_used,prompt= question, cost_usd=cost, source=provider)
