from pydantic import BaseModel, Field
from typing_extensions import Optional, Literal


class MarketQuery(BaseModel):
    question : str
    provider : Literal["anthropic", "openai", "openrouter"] 


class MarketResponse(BaseModel):
    answer :  str 
    response_time_ms :  float 
    tokens_used :  int
    prompt  :   str 
    cost_usd : float
    source : str 


