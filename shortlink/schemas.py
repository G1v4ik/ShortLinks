from pydantic import BaseModel

class URLBase(BaseModel):
    targrt_url: str


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    admin_url: str