#怎样管理数据

#列表
#pop
def get_all_links(page):
    links=[]
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def get_next_target():

