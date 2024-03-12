from datetime import time
from typing import AnyStr

from bs4 import BeautifulSoup
from googlesearch import search
from gentopia.tools.basetool import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PyPDF2 import *

class pdf_readerArgs(BaseModel):
    path: str = Field(..., description="a search query")


class pdf_reader(BaseTool):
    """Tool that adds the capability to query the Google search API."""

    name = "pdf_reader"
    description = ("A search engine retrieving top search results as snippets from DuckDuckGo."
                   "Input should be a search query.")

    args_schema: Optional[Type[BaseModel]] = pdf_readerArgs

    def _run(self, path: str) -> str:
        webFile = requests.get(path)
        with open("s.pdf","wb") as f:
            for i in webFile.iter_content(1024):
                    # print(i)
                    f.write(i)
        text = ""
        pdfFile = PdfReader("s.pdf")
        for i in pdfFile.pages:
                text+= i.extract_text()
        
        return text
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = pdf_reader._run("")
    print(ans)
