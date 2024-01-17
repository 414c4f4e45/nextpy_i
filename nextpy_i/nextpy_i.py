# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

import nextpy as xt
from lorem_text import lorem
import pyperclip
# Construct the filename to display 
from xtconfig import config
filename = f"{config.app_name}/{config.app_name}.py"

class State(xt.State):
	paragraphs : int
	result : str
	raze : str
	def generate(self):
		if self.paragraphs==0 or self.paragraphs==None:
			self.raze="Please Enter Value > 0"
		elif type(self.paragraphs)=='str':
			self.raze="Please Enter an Integer Value!"
		else:
			self.raze = ""
			self.result=lorem.paragraphs(self.paragraphs)
	def clear(self):
		self.paragraphs = None
		self.result = ""
		self.raze = ""
	def copy(self):
		if self.result=="":
			self.raze="Nothing to Copy"
		else:
			pyperclip.copy(self.result)
			self.raze="Copied to Clipboard"			
# define index page. Frontend Pages are just functions that return a frontend components
def index() -> xt.Component:
    return xt.fragment(
        xt.vstack(
            xt.input(placeholder="Enter No. of Paragraphs",on_change=State.set_paragraphs),
            xt.text(f"{State.raze}"),
            xt.hstack(
            	xt.button("Generate",on_click=State.generate),
            	xt.button("Clear",on_click=State.clear),
            	xt.button("Copy",on_click=State.copy),
            ),
            xt.text(f"TEXT: {State.result}")
        )
    )

# Global styles defined as a Python dictionary
style = {
    "text_align": "center",  
}


app = xt.App(style=style)
app.add_page(index)
