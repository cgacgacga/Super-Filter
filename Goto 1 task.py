#quu..__
# $$$b  `---.__
#  "$$b        `--.                          ___.---uuudP
#   `$$b           `.__.------.__     __.---'      $$$$"              .
#     "$b          -'            `-.-'            $$$"              .'|
#       ".                                       d$"             _.'  |
#         `.   /                              ..."             .'     |
#           `./                           ..::-'            _.'       |
#            /                         .:::-'            .-'         .'
#           :                          ::''\          _.'            |
#          .' .-.             .-.           `.      .'               |
#          : /'$$|           .@"$\           `.   .'              _.-'
#         .'|$u$$|          |$$,$$|           |  <            _.-'
#         | `:$$:'          :$$$$$:           `.  `.       .-'
#         :                  `"--'             |    `-.     \
#        :##.       ==             .###.       `.      `.    `\
#        |##:                      :###:        |        >     >
#        |#'     `..'`..'          `###'        x:      /     /
#         \                                   xXX|     /    ./
#          \                                xXXX'|    /   ./
#          /`-.                                  `.  /   /
#         :    `-  ...........,                   | /  .'
#         |         ``:::::::'       .            |<    `.
#         |             ```          |           x| \ `.:``.
#         |                         .'    /'   xXX|  `:`M`M':.
#         |    |                    ;    /:' xXXX'|  -'MMMMM:'
#         `.  .'                   :    /:'       |-'MMMM.-'
#          |  |                   .'   /'        .'MMM.-'
#          `'`'                   :  ,'          |MMM<
#            |                     `'            |tbap\
#             \                                  :MM.-'
#              \                 |              .''
#               \.               `.            /
#                /     .:::::::.. :           /
#               |     .:::::::::::`.         /
#               |   .:::------------\       
#              /   .''               >::'  /
#              `',:                 :    .'
#


from PIL import Image, ImageDraw, ImageFont, ImageChops 
from random import randint 
base = Image.open('before.jpg').convert('RGBA') 
txt = Image.new('RGBA', base.size, (255,255,255,0)) 
fnt = ImageFont.truetype('Consola.ttf', 40) 
d = ImageDraw.Draw(txt) 
pepe = Image.open("pepe.jpg").convert('RGBA') 
pix = pepe.load() 
for i in range (300): 
for j in range (300): 

r,g,b,c = pix[i,j] 
pix[i,j] = (r,g,b,0) 
if r==211 and b == 240 and g == 215: 
pix[i,j] = (0,0,0,0) 

pepe.show() 

a = randint(0,base.width-299) 
b = randint(0,base.height-299) 
part1 = pepe.crop((0, 0, 299, 299)) 
part2 = base.crop((a,b, a + 299, b + 299)) 
tmp = ImageChops.blend(part1, part2, 64) 

base.paste(tmp, (a,b, a + 299, b + 299)) 

background = Image.open("pepe.png") 
foreground = Image.open("before.jpg").convert('RGBA') 

background.paste(foreground, (0, 0), base) 


d.text((base.width // 2,base.height//2), "So sad", font=fnt, fill=(255,0,0,255)) 
d.text((14,218), "So pessimistic", font=fnt, fill=(0,255,0,255)) 


out = Image.alpha_composite(base, txt) 

out.show() 
out.save("suchpict.png") 
