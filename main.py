import glob
import sys
import os

#複数フォルダの大元のフォルダをpathに入れる。
path = sys.argv[1]

def brand_name_extraction(full_path):
    s = ''
    for moji in full_path[::-1]:
        if moji =='/':
            break
        else:
            s += moji
    return s[::-1]


for i in glob.glob(path+'/*'):

    brand_name = brand_name_extraction(i)
    print(i)

    ind = 0
    
    for image_name in glob.glob(i+'/*'):
        #print(image_name)
        
        t_path = path + '/' + brand_name + '/'
        print(image_name)
        print(t_path+brand_name+'_'+str(ind))
        os.rename(image_name, t_path+brand_name+'_'+str(ind)+'.png')
        ind += 1
    
    ind = 0
        
