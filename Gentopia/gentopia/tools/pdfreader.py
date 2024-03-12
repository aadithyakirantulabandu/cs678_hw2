from typing import AnyStr
import re
import numexpr
from gentopia.tools.basetool import *
import math
import PyPDF2
import requests
import io

class PdfreaderArgs(BaseModel):
    path: str = Field(..., description="a mathematical expression.")
class Pdfreader(BaseTool):
    """docstring for Calculator"""
    name = "pdfreader"
    description = "A calculator that can compute arithmetic expressions. Useful when you need to perform " \
                  "numerical calculations."
    args_schema: Optional[Type[BaseModel]] = PdfreaderArgs

    def _run(self, path: AnyStr) -> Any:
      response = requests.get(path)
      if response.status_code == 200:
        data = response.content
      with open(io.BytesIO(data), 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        all_text = ""
      # Loop through all pages and extract text
      for page_num in range(reader.getNumPages()):
        page = reader.getPage(page_num)
        all_text += page.extractText()
      return all_text
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
#if __name__ == "__main__":
#    ans = pdfreader()._run("1+1=")
 #   print(ans)
