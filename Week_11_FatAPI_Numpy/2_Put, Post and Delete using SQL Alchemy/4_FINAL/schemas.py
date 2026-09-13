from pydantic import BaseModel, Field


class Novel(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    price: int = Field(gt=0)