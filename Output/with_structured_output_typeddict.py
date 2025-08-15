from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()


model = ChatGroq(model="deepseek-r1-distill-llama-70b")

# Define TypedDict in PascalCase
class Review(TypedDict):
    key_themes: Annotated[list[str], "Key themes or topics discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal['pos', 'nag', 'nutral'], "The overall sentiment of the review, e.g., 'positive', 'negative', 'neutral'"]
    pros: Annotated[Optional[list[str]], "List of positive aspects mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of negative aspects mentioned in the review"]

# Use structured output
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
Hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove.
Also, the UI looks outdated compared to other brands.
Hoping for a software update to fix this.
""")

print(result)
