from PIL import Image  # needs pillow to work
from PIL import ImageDraw
from PIL import ImageFont # https://youtu.be/0T_dF7QwOfU?si=ksOAIwwgc1FsgLxd used to find out how to write on an image

character_sheet= Image.open("C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/Nimble charater sheet.jpg")
font1 = ImageFont.truetype("arial",50)
draw= ImageDraw.Draw(character_sheet)
# Name= input( 'what would you like the name of the charater to be: ')
draw.text((240,50),'it worked',font=font1,fill=(0,0,0),)
draw.text((1050,50),'it worked',font=font1,fill=(0,0,0),)
draw.text((150,98),'it worked',font=font1,fill=(0,0,0),)
draw.text((1050,98),'it worked',font=font1,fill=(0,0,0),)
draw.text((205,155),'it worked',font=font1,fill=(0,0,0),)
draw.text((180,270),'+1',font=font1,fill=(0,0,0),)
draw.text((295,270),'+2',font=font1,fill=(0,0,0),)
draw.text((425,270),'+3',font=font1,fill=(0,0,0),)
draw.text((550,270),'+4',font=font1,fill=(0,0,0),)
draw.text((660,270),'+5',font=font1,fill=(0,0,0),)
draw.text((1215,290),'+6',font=font1,fill=(0,0,0),)
draw.text((1328,270),'+7',font=font1,fill=(0,0,0),)
draw.text((1328,370),'+8',font=font1,fill=(0,0,0),)
draw.text((1435,265),'+9',font=font1,fill=(0,0,0),)
draw.text((1435,340),'+10',font=font1,fill=(0,0,0),)
draw.text((1575,290),'+11',font=font1,fill=(0,0,0),)
draw.text((1680,290),'+12',font=font1,fill=(0,0,0),)
character_sheet.save(f"C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/charater sheet.jpg")


character_sheet= Image.open("C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/charater sheet.jpg")
font1 = ImageFont.truetype("arial",40)
draw= ImageDraw.Draw(character_sheet)
draw.text((170,520),'+1',font=font1,fill=(0,0,0),)
draw.text((300,520),'+2',font=font1,fill=(0,0,0),)
draw.text((425,520),'+3',font=font1,fill=(0,0,0),)
draw.text((550,520),'+4',font=font1,fill=(0,0,0),)
draw.text((675,520),'+5',font=font1,fill=(0,0,0),)
draw.text((800,520),'+6',font=font1,fill=(0,0,0),)
draw.text((925,520),'+7',font=font1,fill=(0,0,0),)
draw.text((1050,520),'+8',font=font1,fill=(0,0,0),)
draw.text((1175,520),'+9',font=font1,fill=(0,0,0),)
draw.text((1300,520),'+10',font=font1,fill=(0,0,0),)
character_sheet.save(f"C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/charater sheet.jpg")

character_sheet= Image.open("C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/charater sheet.jpg")
font1 = ImageFont.truetype("arial",30)
draw= ImageDraw.Draw(character_sheet)

# if str_ == '+':
#     draw.text((181,413),'▲',font=font1,fill=(0,0,0),)
# elif str_ == '-':
#     draw.text((194,413),'▼',font=font1,fill=(0,0,0),)


# if dex_ == '+':
#     draw.text((296,413),'▲',font=font1,fill=(0,0,0),)
# elif dex_ == '-':
#     draw.text((304,413),'▼',font=font1,fill=(0,0,0),)


# if int_ == '+':
#     draw.text((440,413),'▲',font=font1,fill=(0,0,0),)
# elif int_ == '-':
#     draw.text((454,413),'▼',font=font1,fill=(0,0,0),)


# if wis_ == '+':
#     draw.text((580,413),'▲',font=font1,fill=(0,0,0),)
# elif wis_ == '-':
#     draw.text(( 594,413),'▼',font=font1,fill=(0,0,0),)
character_sheet.save(f"C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/charater sheet.jpg")
# https://youtu.be/0T_dF7QwOfU?si=ksOAIwwgc1FsgLxd other part of writing on an image

character_sheet= Image.open("C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/charater sheet.jpg")
font1 = ImageFont.truetype("arial",40)
draw= ImageDraw.Draw(character_sheet)
draw.text((870,350),'str',font=font1,fill=(0,0,0),)
draw.text((1000,350),'dex',font=font1,fill=(0,0,0),)
character_sheet.show()
character_sheet.save(f"C:/Users/derrk/Desktop/School work/Intro-To-Programming/Projects/Final Project/charater sheet.jpg")
# https://youtu.be/0T_dF7QwOfU?si=ksOAIwwgc1FsgLxd other part of writing on an image
