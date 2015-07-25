import requests
import re
import os

def download_pic(url, des_dir):
    pic_name = url.split('/')[-1]
    pic = requests.get(url)
    if pic.status_code == 200:
        if not os.path.exists("%s/%s" % (des_dir, pic_name)): 
	    with open("%s/%s" % (des_dir, pic_name), 'wb') as f:
                f.write(pic.content)
		f.close()
		print pic_name + ' download completed'
	else:
	    print pic_name + ' already exists'
    else:
        print 'url not exists'


def get_img_url(home_url):
    a = requests.get(home_url)
    to_get = re.compile(r'(?<=src=["])http://ww\d\.sinaimg\.cn/[^t]\w+/\w+\.(?:gif|jpg)(?=["])')
    return to_get.findall(a.content)

#get_img_url('http://jandan.net/ooxx')


def get_page_url(home_url):
    b = requests.get(home_url)
    to_get = re.compile(r'(?<=current-comment-page">\[)\d+(?=\])')
    return to_get.search(b.content).group()

#print get_page_url('http://jandan.net/ooxx')

home_page = 'http://jandan.net/ooxx'
des_dir = 'D:/test'
root_page = get_page_url('http://jandan.net/ooxx')
for i in range(int(root_page)-10,int(root_page)+1):
    url_list = get_img_url(home_page + '/page-' + str(i) + '#comments')
    for j in url_list:
        download_pic(j, des_dir)
