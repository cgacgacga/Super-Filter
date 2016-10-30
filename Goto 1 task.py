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

base = Image.open('before.jpg').convert('RGBA')
txt = Image.new('RGBA', base.size, (255,255,255,0))
fnt = ImageFont.truetype('Consola.ttf', 40)
d = ImageDraw.Draw(txt)
pepe  = Image.open("pepe.jpg").convert('RGBA')
pix = pepe.load()
for i in range (300):
	for j in range (300): 
		
		r,g,b,c = pix[i,j]
		pix[i,j] = (r + 50,g + 50,b + 50 ,10)

part1 = pepe.crop((0, 0, 299, 299))
part2 = base.crop((0, 0, 299, 299))
tmp = ImageChops.blend(part1, part2, 255)


base.paste(tmp, (0, 0, 299, 299))


d.text((250,250), "So sad", font=fnt, fill=(122,122,122,255))


out = Image.alpha_composite(base, txt)

out.show()
out.save("suchhist.png")
