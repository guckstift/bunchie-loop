
from PIL import Image

bunchie = Image.open ("bunchie_color.gif")

i = 0
while True:
	bunchie.save("outfile"+str(i)+".gif")
	#converted = bunchie.convert ("RGB")
	try:
		bunchie.seek(bunchie.tell()+1)
	except EOFError:
		break
	i+=1

