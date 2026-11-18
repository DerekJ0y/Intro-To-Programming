from PIL import Image  # needs pillow to work
from PIL import ImageDraw
from PIL import ImageFont

character_sheet= Image.open("C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/Nimble charater sheet.jpg")
font1 = ImageFont.truetype("times new roman",12)
draw= ImageDraw.Draw(character_sheet)
draw.text((168,256),"it worked",font=font1,fill=(0,0,0))
character_sheet.show()
character_sheet.save("C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/Nimble charater sheetnew.jpg")