# -*- coding: utf-8 -*-

#正向最大匹配法

text='研究生命的最初起源'#即将被分词的文本
dic=['研究','研究生','生命','命','的','最','初','起源'] #在这个字典进行匹配
ww=7 #每次取七个字符来匹配
MMresult=[]
index=0
text_length=len(text)

while text_length>index:
    for size in range(ww+index,index,-1):
        print(size,':',ww+index,index,-1)#输出遍历索引的过程
        piece=text[index:size]
        print(piece)#输出每次尝试匹配的字符串
        if piece in dic:
            index=size-1
            break
    index=index+1
    MMresult.append(piece+'--')
print(MMresult)


#逆向最大匹配法

text='研究生命的最初起源'#即将被分词的文本
dic=['研究','研究生','生命','命','的','最','初','起源'] #在这个字典进行匹配
ww=7 #每次取七个字符来匹配
RMMresult=[]
index=len(text)

while index>0:
    for size in range(index-ww,index):
        print(size,':',index-ww,index)#输出遍历索引的过程
        piece=text[size:index]
        print(piece)#输出每次尝试匹配的字符串
        if piece in dic:
            index=size+1
            break
    index=index-1
    RMMresult.append(piece+'--')
RMMresult.reverse()
print(RMMresult)


#把正向最大匹配法写成一个类
'''
class MM(object):

  #  def __init__(self):
   #     self.ww=7
    
    def cut(self,text):
        ww=7 #每次取七个字符来匹配
        result=[]
        index=0
        text_length=len(text)
        dic=['研究','研究生','生命','命','的','最','初','起源']
        while text_length>index:
            for size in range(ww+index,index,-1):
                print(size,':',ww+index,index,-1)#输出遍历索引的过程
                piece=text[index:size]
                print(piece)#输出每次尝试匹配的字符串
                if piece in dic:
                    index=size-1
                    break
            index=index+1
            result.append(piece+'--')
        print(result)
if __name__=='__main__':
    text='研究生命的最初起源'
    token=MM()
    print(token.cut(text))    
   
'''
#把逆向最大匹配法写成一个类
'''
class RMM(object):
    def __init__(self):
        self.w=7
    def cut(self,text):
        dic=['研究','研究生','生命','命','的','最','初','起源'] #在这个字典进行匹配
        result=[]
        index=len(text)

        while index>0:
            for size in range(index - self.w,index):
                print(size,':',index - self.w,index)#输出遍历索引的过程
                piece=text[size:index]
                print(piece)#输出每次尝试匹配的字符串
                if piece in dic:
                    index=size+1
                    break
            index=index-1
            result.append(piece+'--')
        result.reverse()
        print(result)

if __name__=='__main__':
    text="研究生命的最初起源"
    tokenn=RMM()
    print(tokenn.cut(text))
'''