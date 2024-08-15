import os
import sys
import shutil
from PIL import Image

#
#
#
#   here's the terminal line
#
#  >python divmaker.py wildlife
#
#
#

# print ('argument list', sys.argv)
rootpath = 'C:/Web_Design/maithonisphotography/'
imagepath = rootpath + 'images/'
folder = ""  +(sys.argv[1])
startline = 0
endline = 0
size_thumbnail = (580,1200)

##clear thumbs folder and create it
if os.path.exists(imagepath +folder+'/thumbs'):
     shutil.rmtree(imagepath +folder+'/thumbs')
os.mkdir(imagepath +folder+'/thumbs')

##creates divs.txt based on images in folder
f = open(rootpath+'divs.txt', 'w')
for filename in reversed(os.listdir(imagepath +folder)):

     if (filename != 'thumbs'):
                  
          # strips exif        
          i = Image.open(imagepath+folder+'/'+filename)
          data = list(i.getdata())
          image_without_exif = Image.new(i.mode, i.size)
          image_without_exif.putdata(data)
          image_without_exif.save(imagepath+folder+'/'+filename)

          ##makes resized thumbnails
          i = Image.open(imagepath+folder+'/'+filename)
          i.thumbnail(size_thumbnail)
          (name, ext) = os.path.splitext(filename)
          i.save(imagepath+folder+'/thumbs/'+name+'.webp','WEBP')

          ##writes div classes
          f.write('\t\t\t\t\t\t<div class="item">\r')
          f.write('\t\t\t\t\t\t\t<div class="animate-box">\r')
          f.write('\t\t\t\t\t\t\t\t<a href="images/' + folder + "/" + filename + '" class="image-popup fh5co-board-img"><img src="images/' + folder + '/thumbs/'+name+'.webp'+'" alt=""></a>\r')
          f.write('\t\t\t\t\t\t\t</div>\r')
          f.write('\t\t\t\t\t\t</div>\r')
f.close()

##grabs divs.txt data into memory and deletes the file
with open(rootpath+'divs.txt', "r") as f:
     divcontent = f.readlines()
f.close()
if os.path.exists(rootpath+'divs.txt'):
     os.remove(rootpath+'divs.txt')

##finds start position
with open(rootpath+folder+".html", "r") as f:
    lines = f.readlines()
    for row in lines:
          # check if string present on a current line
          word = '<!-- begin pictures -->'
          #print(row.find(word))
          # find() method returns -1 if the value is not found,
          # if found it returns index of the first occurrence of the substring
          if row.find(word) != -1:
               print('start line number:', lines.index(row)+1)
               startline = lines.index(row)+1
f.close()

##finds end position
with open(rootpath+folder+".html", "r") as f:
    lines = f.readlines()
    for row in lines:
          # check if string present on a current line
          word = '<!-- end pictures -->'
          #print(row.find(word))
          # find() method returns -1 if the value is not found,
          # if found it returns index of the first occurrence of the substring
          if row.find(word) != -1:
               print('end line number:', lines.index(row))
               endline = lines.index(row)  
f.close()

if startline == 0 or endline == 0:
     print('start or end line is missing')
     exit()

##cuts away front and back of file ignoring content in middle
with open(rootpath+folder+".html") as f:
     content = f.readlines()
     contentstart = content[:startline]
     contentend = content[endline:]
f.close()

##creates new file with beginning divs and end
with open(rootpath+folder+".html", "w") as f:
     f.writelines(contentstart)
     f.writelines(divcontent)
     f.writelines(contentend)
f.close()