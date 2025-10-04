from typing import Annotated
from sqlalchemy import String
from sqlalchemy.orm import mapped_column


unique_str_an = Annotated[str, mapped_column(String, unique=True)]
str_an = Annotated[str, mapped_column(String, nullable=False)]