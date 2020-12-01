# Kwai_download
This crawler download Kwai short-videos by **search a certain topic keyword**.

## User guidance

Use Firefox or Chrome browser to open [快手 (kuaishou.com)](https://video.kuaishou.com/). 

![1](img/1.png)

Search a topic keyword.

![2](img/2.png)

Scroll down until you got enough videos.

**Note: All the videos in this page will be downloaded from top to bottom and left to right. In other words, only these videos shown in this page will be downloaded.**

![3](img/3.png)

Click F12 and find elements, choose ‘body’, copy and paste it into file 'element.txt', save. 

**Note: make 'element.txt' empty before you paste.**

![4](img/4.png)

![5](img/5.png)

python download.py -r \<root\>

If not specified, root is default as './\<keyword\>'. 