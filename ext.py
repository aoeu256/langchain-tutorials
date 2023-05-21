#llm ("show me python code to register my line magic in jupyter")
from IPython.core.magic import register_line_magic
@register_line_magic
def py(text):
    output = llm('Python code for:'+text)
    append_code_cell(output)

@register_line_magic
def o(text):
    print(llm(text))



