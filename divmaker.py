import os
import sys
import shutil
from PIL import Image
print ('argument list', sys.argv)
folder = ""  +(sys.argv[1])
startline = 0
endline = 0
size_thumbnail = (580,1200)

##clear thumbs folder and create it
shutil.rmtree('C:/Web_Design/maithonisphotography/images/' +folder+'/thumbs')
os.mkdir('C:/Web_Design/maithonisphotography/images/' +folder+'/thumbs')

##creates divs.txt based on images in folder
f = open('C:/Web_Design/maithonisphotography/divs.txt', 'w')
for filename in reversed(os.listdir('C:/Web_Design/maithonisphotography/images/' +folder)):
     if (filename != 'thumbs'):
          ##resizes images
          i = Image.open('C:/Web_Design/maithonisphotography/images/'+folder+'/'+filename)
          i.thumbnail(size_thumbnail)
          (name, ext) = os.path.splitext(filename)
          i.save('C:/Web_Design/maithonisphotography/images/'+folder+'/thumbs/'+name+'.webp','WEBP')

          ##writes div classes
          f.write('\t\t\t\t\t\t<div class="item">\r')
          f.write('\t\t\t\t\t\t\t<div class="animate-box">\r')
          f.write('\t\t\t\t\t\t\t\t<a href="images/' + folder + "/" + filename + '" class="image-popup fh5co-board-img"><img src="images/' + folder + '/thumbs/'+name+'.webp'+'" alt=""></a>\r')
          f.write('\t\t\t\t\t\t\t</div>\r')
          f.write('\t\t\t\t\t\t</div>\r')
f.close()

##grabs divs.txt data into memory and deletes the file
with open("C:/Web_Design/maithonisphotography/divs.txt", "r") as f:
     divcontent = f.readlines()
f.close()
if os.path.exists("C:/Web_Design/maithonisphotography/divs.txt"):
     os.remove("C:/Web_Design/maithonisphotography/divs.txt")

##finds start position
with open("C:/Web_Design/maithonisphotography/"+folder+".html", "r") as f:
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
with open("C:/Web_Design/maithonisphotography/"+folder+".html", "r") as f:
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
with open("C:/Web_Design/maithonisphotography/"+folder+".html") as f:
     content = f.readlines()
     contentstart = content[:startline]
     contentend = content[endline:]
f.close()

##creates new file with beginning divs and end
with open("C:/Web_Design/maithonisphotography/"+folder+".html", "w") as f:
     f.writelines(contentstart)
     f.writelines(divcontent)
     f.writelines(contentend)
f.close()

    

     
