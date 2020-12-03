# This crawler download Kwai short-videos by search a certain topic keyword.
# It simply reads html elements string from 'element.txt',
# which is collected by manually copy the elements of the certain search result page,
# and then parses short-video links to download.
# To get more details, please refer to 'README.md'.

import requests
import os
import argparse
def downloadVideo(url,root,id):
    # url = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f9f0000brm8f726tgqapf007a00&ratio=720p&line=0'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    path = root +'/'+ str (id) +'.mp4'
    print(path)

    try:
        if not os.path.exists(root):  #判断当前根目录是否存在
            os.mkdir(root)
        if not os.path.exists(path):
            #判断当前文件是否存在
            r = requests.get(url, headers=headers)
            print(r.status_code)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")
    print()

def geturl(html_string):
    try:
        pos = html_string.find("photoUrl")
        i = 11
        st = pos + 11
        ed = html_string.find("\"",st)
        return html_string[st:ed]
    except:
        return ""

def download(root=None):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    prefix = "https://video.kuaishou.com/"
    f = open('element.txt','r',encoding='utf-8')

    s = ''.join(f.readlines())

    f.close()

    if root == None:
        pp = s.find('searchKey=')
        ed = s.find('&',pp+10)
        root = s[pp+10:ed]

    p = 0

    while(1):
        st = s.find('short-video',p)
        print(f'parse cursor position: {st}')
        if st==-1:
            return
        sla = s.find('/',st)
        ed = s.find('?',st)
        url = prefix+s[st:ed]
        id = s[sla+1:ed]

        r = requests.get(url, headers=headers)
        url = geturl(r.content.decode("unicode_escape"))
        downloadVideo(url, root, id)

        p = st+1

    return

parser = argparse.ArgumentParser(description="Kwai_download_args")
parser.add_argument('--root','-r',default=None)

if __name__ == '__main__':
    args=parser.parse_args()
    download(args.root)