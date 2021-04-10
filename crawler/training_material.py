# 抓取國中家教復習教材列表
# https://chineseandsociety.blogspot.com/

import urllib.request as req
from urllib.error import URLError, HTTPError

def getPageData(url):
    request = req.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    # with req.urlopen(request) as response:
    #     data = response.read().decode("utf-8")
    try:
         response = req.urlopen(request)
    except HTTPError as e:
        print("The server can\'t fulfill the request.")
        print("Error code: ", e.code)
    except URLError as e:
        print("Failed to reach a server.")
        print("Reason: ", e.reason)
    else:
        data = response.read().decode("utf-8")
    return data
    
org_url = "https://chineseandsociety.blogspot.com/"
import bs4
import pandas as pd

def crawPages():
    data = getPageData(org_url)
    root = bs4.BeautifulSoup(data, "html.parser")

    # 從網誌封存清單中找出所有月份的 post links
    PostMonths = root.select("li > ul a.post-count-link")
    all_post_list = ""
    for postLink in PostMonths:
        postsPage = getPageData(postLink["href"])
        postRoot = bs4.BeautifulSoup(postsPage, "html.parser")

        # 抓取該月份的 post list, 取 post 的文字和 href
        posts = postRoot.select("ul.posts > li a")
        for post in posts:
            all_post_list = all_post_list + "name:{0},url:{1},".format(post.string, post["href"])

        # df = pd.DataFrame({
        #     "name":"http://www.google.com",
        #     "name2":"http://www.yahoo.com"
        # }, index=[0])
        #df = pd.DataFrame(all_post_list)
        df = pd.read_csv(all_post_list)
        
    return df.iloc[0].to_string()