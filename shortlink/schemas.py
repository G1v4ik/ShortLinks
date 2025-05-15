from pydantic import BaseModel, ConfigDict

class URLBase(BaseModel):
    target_url: str


class URL(URLBase):
    model_config = ConfigDict(from_attributes=True)
    
    key: str
