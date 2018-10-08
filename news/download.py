import time
from settings import PATH

def save_to_txt(title, contents):
    with open(r'%s\%s.txt' % (PATH, str(int(time.time()*1000))), 'w', encoding='utf-8') as f:
        f.write(title + '\n')
        contents = (contents.encode('utf-8')).decode()
        L = contents.split(' ')
        for p in L:
            if '来源：' in p or '责任编辑：' in p or '原标题：' in p:
                continue
            if not p:
                continue
            f.write(p + '\n')
            
            


if __name__ == '__main__':
    print(PATH)
