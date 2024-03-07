import os
import sys
print ('argument list', sys.argv)
folder = ""  +(sys.argv[1])
f = open('C:/Web_Design/maithonisphotography/divs.txt', 'w')
for filename in reversed(os.listdir('C:/Web_Design/maithonisphotography/images/' +folder)):
     if (filename != 'thumbs'):
          f.write('<div class="item">\r')
          f.write('\t<div class="animate-box">\r')
          f.write('\t\t<a href="images/' + folder + "/" + filename + '" class="image-popup fh5co-board-img"><img src="images/' + folder + '/thumbs/'+filename+'" alt=""></a>\r')
          f.write('\t</div>\r')
          f.write('</div>\r')
f.close()
     
