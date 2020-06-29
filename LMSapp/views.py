from django.shortcuts import render,redirect
import requests
# from .models import Cart
from bs4 import BeautifulSoup
from .models import Links

# Create your views here.

b_keywords = ['Beginner', 'install', 'download', 'setup', 'set up', 'run', 'compile', 'import', 'step by step', 'learn',
              'basic', 'intro', 'fundamentals', 'quick guide', 'crash course', 'Introduction']
c_keywords = ['vs', 'comparison']
d_keywords = ['how to', 'demo', 'demonstration']
p_keywords = ['project', 'build', 'create']
a_keywords = ['complete course', 'advance', 'complete guide', 'high level', 'full course']
a_videos = {}
b_videos = {}
c_videos = {}
d_videos = {}
o_videos = {}
pdf = {}
books = {}
text = {}
articles = {}
study_materials = {}
solve_codes = {}
tutorials = {}
slides = {}
blogs = {}
quiz = {}
checkouts = {}
checkout_videos = {}
checkout_slide = {}
def vdopage(request):
    return render(request, 'LMSapp/VideoSearch.html')
def vdocart(request):
    key = request.GET.get('q')
    yt_links(key)
    return render(request, 'LMSapp/OnlyVideosCart.html', {'a_videos': a_videos, 'o_videos': o_videos,
                                                          'b_videos': b_videos, 'c_videos': c_videos,
                                                          'd_videos': d_videos})

def filepage(request):
    return render(request, 'LMSapp/FileSearch.html')
def filecart(request):
    key = request.GET.get('q')
    goal_kicker(key)
    slide_share(key)
    beginners_book(key)
    computer_pdf(key)
    tuto_computer(key)
    programmer_books(key)
    ws_vincent(key)
    return render(request, 'LMSapp/OnlyFilesCart.html', {'pdf': pdf, 'books': books, 'slide': slides})
def addcart(request):
    # if request.method == "POST":
    #     name = request.POST['NAME']
    #     # if request.POST['checks']:
    #     #     checks.append(request.POST['checks'])
    #     # if request.POST['checks']:
    #     #     checks.append(request.POST['checks'])
    #     # check2 = request.POST['NAW']
    #     checks = request.POST.getlist('checks')
    #     # cart = Cart.link(checks[0])
    #     # car = Cart.objects.link
    #     # car.save()
    #     print('Added to cart')
    return render(request, "LMSapp/cart.html", {'a_videos': a_videos, 'o_videos': o_videos,
                                                'b_videos': b_videos, 'c_videos': c_videos,
                                                'd_videos': d_videos, 'text': text, 'pdf': pdf, 'books': books,
                                                'study_materials': study_materials, 'codes': solve_codes,
                                                'articles': articles, 'tutorials': tutorials, 'blogs': blogs,
                                                'quiz': quiz, 'slide': slides})

def checkout(request):
    if request.method == "POST":
        checks_articles = request.POST.getlist('articles')
        checks_materials = request.POST.getlist('materials')
        checks_books = request.POST.getlist('books')
        checks_tutorials = request.POST.getlist('tutorials')
        checks_pdfs = request.POST.getlist('pdfs')
        checks_blogs = request.POST.getlist('blogs')
        checks_videos = request.POST.getlist('videos')
        checks_codes = request.POST.getlist('codes')
        checks_quizs = request.POST.getlist('quizs')
        checks_slides = request.POST.getlist('slides')
        # print(checks)
        for ch in checks_articles:
            checkouts[ch] = articles[ch]
        for chm in checks_materials:
            checkouts[chm] = study_materials[chm]
        # print(checks_videos)
        print(checks_pdfs)
        for vd in checks_videos:
            if vd in b_videos.keys():
                checkout_videos[vd] = b_videos.get(vd)
            elif vd in a_videos.keys():
                checkout_videos[vd] = a_videos.get(vd)
            elif vd in c_videos.keys():
                checkout_videos[vd] = c_videos.get(vd)
            elif vd in d_videos.keys():
                checkout_videos[vd] = d_videos.get(vd)
            if vd in o_videos.keys():
                checkout_videos[vd] = o_videos.get(vd)
        for sl in checks_slides:
            checkout_slide[sl] = slides[sl]
        for pd in checks_pdfs:
            if pd != '':
                checkouts[pd] = pdf[pd]
        for bo in checks_books:
            checkouts[bo] = books[bo]
        for qu in checks_quizs:
            checkouts[qu] = quiz[qu]
        for co in checks_codes:
            checkouts[co] = solve_codes[co]
        for blo in checks_blogs:
            checkouts[blo] = blogs[blo]
        for tu in checks_tutorials:
            checkouts[tu] = tutorials[tu]
        print(checkout_slide)
    for title_text in checkout_videos.keys():
       	Links.objects.create(title=title_text, link_url=checkout_videos[title_text])
    return render(request, "LMSapp/checkout.html", {'checkout': checkouts, 'checkout_videos': checkout_videos, 'checkout_slide': checkout_slide})
def search(request):
    key = request.GET.get('q')
    yt_links(key)                                           #1
    medium(key)                                             #2
    dream_host(key)                                         #3
    programmer_books(key)                                   #4
    edu_cba(key)                                            #5
    slide_share(key)                                        #6
    goal_kicker(key)                                        #7
    codes_cracker(key)                                      #8
    coding_bat(key)                                         #9
    beginners_book(key)                                     #10
    tut_gate(key)                                           #11
    tut_plus(key)                                           #12
    tech_gig(key)                                           #13
    java_point(key)                                         #14
    guru(key)                                               #15
    data_incubator(key)                                     #16
    git_connected(key)                                      #17
    geek = geeks(key)                                       #18
    ws_vincent(key)                                         #19
    computer_pdf(key)                                       #20
    code_condo(key)                                         #21
    learn_java(key)                                         #22
    hackr(key)                                              #23
    tuto_computer(key)                                    #24
    geeks_for_geeks(key)                                    #25
    frontend_masters(key)                                   #26
    coder_pedia(key)                                        #27
    tutorials_in_hand(key)                                  #28
    dev_mozilla(key)                                        #29
    coding_game(key)                                        #30
    eda_bit(key)                                            #31
    # print(data)
    # print('\nplist\n', plist)
    return render(request, 'LMSapp/searchpage.html', {'a_videos': a_videos, 'o_videos': o_videos,
                                                      'b_videos': b_videos, 'c_videos': c_videos,
                                                      'd_videos': d_videos, 'text': text, 'pdf': pdf,
                                                      'geeks': geek, 'slide': slides, 'books': books,
                                                      'study_materials': study_materials, 'codes': solve_codes,
                                                      'articles': articles, 'tutorials': tutorials, 'blogs': blogs,
                                                      'quiz': quiz})
def home(request):
    return render(request, 'LMSapp/Mainpage.html')

def empty(request):
    return render(request, 'LMSapp/empty.html', {'text': text})

def goal_kicker(key):
    books_arr = []
    titile_arr = []
    # keys = key.split(' ')
    res = requests.get(f'https://books.goalkicker.com/').text
    soup = BeautifulSoup(res, 'lxml')
    container = soup.select('a')
    for content in container:
        link = sep_key(content['href'])
        if key.casefold() in link.casefold():
            books_arr.append('https://books.goalkicker.com/'+link)
            titile_arr.append(link[:-1])
    for i in range(len(titile_arr)):
        books[titile_arr[i]] = books_arr[i]
def slide_share(key):
    thumb_dict = {}
    thumbs = []
    hrefs = []
    title = []
    keys = key.split(' ')
    if len(keys) > 1:
        KeyWord = ''
        for ke in keys:
            KeyWord = KeyWord + '+' + ke
    else:
        KeyWord = key
    url = f'https://www.slideshare.net/search/slideshow?searchfrom=header&q={KeyWord}'
    sl_link = 'https://www.slideshare.net'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    slidess = soup.find_all('a', class_='title title-link antialiased j-slideshow-title')
    thumb_content = soup.find_all('img')
    for thumb in thumb_content:
        img = thumb['src']
        if 'thumbnail' in img:
            thumbs.append(img)
    for slide in slidess:
        hrefs.append(sl_link+slide['href'])
        title.append(slide['title'])
    for i in range(len(thumbs)):
        slides[sep_key(title[i])] = hrefs[i], thumbs[i]
    # return thumb_dict

def beginners_book(key):
    books_arr = []
    title_arr = []
    # keys = key.split(' ')
    res = requests.get(f'https://beginnersbook.com/').text
    soup = BeautifulSoup(res, 'lxml')
    contents = soup.select('a')
    for content in contents:
        link = content['href']
        if key.casefold() in link.casefold():
            books_arr.append(link)
            title_arr.append(link[26:-1])
    for i in range(len(books_arr)):
        books[sep_key(title_arr[i])] = books_arr[i]

def geeks(key):
    articles = []
    thumbs = []
    geeks_list = {}
    avail1 = ['c', 'php', 'java', 'c-plus-plus', 'sql', 'python', 'php']
    avail2 = ['html', 'javascript', 'css', 'jquery']
    url = None
    if key in avail1:
        url = f'http://www.geeksforgeeks.org/{key}/'
    elif key in avail2:
        url = f'https://www.geeksforgeeks.org/{key}-tutorials/'
    try:
        if url != None:
            res = requests.get(url).text
            soup = BeautifulSoup(res, 'lxml')
            # print(soup.prettify())
            title = soup.find('h1', class_='entry-title').text
            images = soup.find_all('img')
            # print(images)
            for thumb in images:
                img = thumb['src']
                if 'uploads' in img:
                    if img not in thumbs:
                        thumbs.append(img)
            articles.append(url)
    except:
        pass
    if(len(thumbs)>=2):
        geeks_list[url] = thumbs[1], sep_key(title)
    return geeks_list

def computer_pdf(key):
    # c_pdf = {}
    # keys = key.split(' ')
    res = requests.get(f'https://www.computer-pdf.com/web-programming/{key}/').text
    soup = BeautifulSoup(res, 'lxml')
    contents = soup.select('a')
    for content in contents:
        link = content['href']
        title = sep_key(content.text)
        if key.casefold() in link.casefold():
            pdf[title] = link

def sep_key(link):
    try:
        keys = link.split(' ')
        if len(keys) > 1:
            KeyWord = keys[0]
            for i in range(1, len(keys)):
                KeyWord = KeyWord + '-' + keys[i]
        else:
            KeyWord = link
        return KeyWord
    except:
        pass
def tuto_computer(key):
    link_arr = []
    title_arr = []
    prev_arr = []
    # keys = key.split(' ')
    res = requests.get(f'https://tuto-computer.com/search.php?search_text={key}').text
    soup = BeautifulSoup(res, 'lxml')
    contents = soup.select('a')
    for content in contents:
        link = content['href']
        title = content.text
        if title!='':

            if key.casefold() in link.casefold():
                link_arr.append('https://tuto-computer.com/'+link)
                title_arr.append(title)

    for i in range(1, len(title_arr)):
        pdf[sep_key(title_arr[i])] = link_arr[i]
    # print(pdf)
    # for links in link_arr:
    #     keyword = sep_key(links)
    #     url_link = keyword
    #     req = requests.get(url_link).text
    #     bs = BeautifulSoup(req, 'lxml')
    #     pre = bs.find_all('a')
    #     for li in pre:
    #         pre_link = li['href']
    #         if 'pdf-preview' in pre_link and pre_link not in prev_arr:
    #             prev_arr.append("https://tuto-computer.com/" + li['href'])
    # for i in range(len(prev_arr)):
    #      pdf[sep_key(title_arr[i])] = prev_arr[i]
def edu_cba(key):
    KeyWord = sep_key(key)
    try:
        url = f'https://www.educba.com/category/software-development/software-development-tutorials/{KeyWord}-tutorial/'
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        par = soup.find('div', class_='decr-tut').text
        text["edu_cba"] = par #.replace(f'{key} tutorial'.casefold(), '')
        # print("For more info visit -> " + url)
    except:
        pass

def yt_links(key):
    req = requests.get(f"https://www.youtube.com/results?search_query={key}")
    soup = BeautifulSoup(req.text, 'lxml')
    contents = soup.find_all('a')
    for content in contents:
        link = content['href']
        title = sep_key(content.text)
        if 'list=PL' in link:
            if 'playlist' in link:
                le = link[15:]
            else:
                le = link[26:]

            if any(ck.casefold() in title.casefold() for ck in c_keywords) and le not in c_videos:
                c_videos[title] = le
            elif any(bk.casefold() in title.casefold() for bk in b_keywords) and le not in b_videos:
                b_videos[title] = le
            elif any(dk.casefold() in title.casefold() for dk in d_keywords) and le not in d_videos:
                d_videos[title] = le
            elif any(ak.casefold() in title.casefold() for ak in a_keywords) and le not in a_videos:
                a_videos[title] = le
            else:
                if le not in o_videos:
                    if '\n\n' in title:
                        continue
                    else:
                        o_videos[title] = le
        elif 'watch' in link and 'ad' not in link:
            li = link[9:]

            if any(ck.casefold() in title.casefold() for ck in c_keywords) and li not in c_videos:
                c_videos[title] = li
            elif any(bk.casefold() in title.casefold() for bk in b_keywords) and li not in b_videos:
                b_videos[title] = li
            elif any(dk.casefold() in title.casefold() for dk in d_keywords) and li not in d_videos:
                d_videos[title] = li
            elif any(ak.casefold() in title.casefold() for ak in a_keywords) and li not in a_videos:
                a_videos[title] = li
            else:
                if li not in o_videos:
                    if '\n\n' in title:
                        continue
                    else:
                        o_videos[title] = li

def tut_gate(key):
    url = f'https://www.tutorialgateway.org/{key}-tutorial/'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    links = soup.find_all('a')
    for link in links:
        href = str(link.get('href'))
        title = href[32:-1]
        if key.casefold() in href.casefold():
            study_materials[sep_key(title)] = href

def codes_cracker(key):
    keyword = key
    url = f'https://codescracker.com/{keyword}/index.htm'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    links = soup.find_all('a')
    for link in links:
        href = str(link.get('href'))
        title = href[:-4]
        title = title.replace(f'/{key}/', '')
        if key.casefold() in href.casefold() and "index" not in title:
            study_materials[sep_key(title)] = "https://codescracker.com" + href

def coding_bat(key):
    try:
        url = f'https://codingbat.com/{key}'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        links = soup.find_all('a')
        for link in links:
            href = str(link.get('href'))
            title = href.replace('/doc/', '')
            title = title.replace('.html', '')
            title = title.replace('/', ' ')
            if key.casefold() in href.casefold():
                study_materials[sep_key(title)] = "https://codingbat.com" + href
    except:
        pass

def guru(key):
    try:
        url = f'http://www.guru99.com/{key}-tutorials.html'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        links = soup.find_all('a')
        for link in links:
            title = link['href'][1:-5]
            if key in title:
                study_materials[sep_key(title)] = 'http://www.guru99.com' + link['href']
    except:
        pass

def tut_plus(key):
    try:
        url = f'https://tutsplus.com/tutorials/search/{key}'

        res = requests.get(url)
        source = res.text
        soup = BeautifulSoup(source, 'lxml')
        title = []
        href = []
        li_arr = {}
        links = soup.find_all('a')
        for link in links:
            if key.casefold() in str(link.get('href')):
                title.append(link.get('href')[35:-11])
                href.append(link.get('href'))
        for i in range(5, len(title)-10):
            study_materials[sep_key(title[i])] = href[i]
    except:
        pass
def tech_gig(key):
    try:
        url = f'https://www.techgig.com/practice/{key}'
        res = requests.get(url)
        source = res.text
        soup = BeautifulSoup(source, 'lxml')
        link = soup.find_all('a')
        li = []
        for links in link:
            if 'practice' in links.get('href'):
                if key.casefold() in str(links.get('href')):
                    li.append(links.get('href'))
        solve_codes["solve-code"] = li[1]
    except:
        pass
# def java_point(key):
#     try:
#         url = f'https://www.javatpoint.com/{key}-tutorial'
#         res = requests.get(url).text
#         soup = BeautifulSoup(res, 'lxml')
#         link = soup.find_all('a')
#         li = []
#         for links in link:
#             if key.casefold() in str(links.get('href')):
#                 li.append("https://www.javatpoint.com/" + str(links.get('href')))
#         for link in li[1:len(li) - 6]:
#             study_materials[link[27:]] = link
#     except:
#         pass

def java_point(key):
    try:
        url = f'https://www.javatpoint.com/{key}-tutorial'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        link = soup.find_all('a')
        li = []
        title_arr = []
        for links in link:
            if key.casefold() in str(links.get('href')) and 'https://' not in str(links.get('href')):
                li.append("https://www.javatpoint.com/" + str(links.get('href')))
                title_arr.append(sep_key(links.text))
        # for link in li[1:len(li) - 6]:
        #     study_materials[title_arr[]] = link
        for i in range(4, len(li)-6):
            study_materials[title_arr[i]] = li[i]
    except:
        pass
def learn_java(key):
    avail1 = ['java', 'ruby', 'sql']
    avail2 = ['html', 'c', 'cpp', 'js', 'php', 'perl']
    # avail3 = ['shell', 'python', 'cs', 'scala']
    if key in avail1:
        url = f'https://www.learn{key}online.org'
    elif key in avail2:
        url = f'https://www.learn-{key}.org/'
    else:
        url = None
    try:
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        link = soup.find_all('a')
        li = []
        for links in link:
            li.append(url + links.get('href'))
        # print(li[37:len(li) - 5])
        for link in li[37:len(li) - 5]:
            if key in avail1:
                title = link.replace("https://www.learnjavaonline.org/en/", '')
            else:
                title = link.replace("https://www.learn-cpp.org//en/", '')
            study_materials[sep_key(title)] = link
    except:
        pass
def code_condo(key):
    try:
        url = f'https://codecondo.com/?s={key}'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        link = soup.find_all('a')
        li = []
        for links in link:
            href = str(links.get('href'))
            if key.casefold() in href.casefold():
                title = href[22:].replace('/#comments', '').replace('/', '')
                articles[sep_key(title)] = href
                # li.append(links.get('href'))
        # print('articles', li)
    except:
        pass

def geeks_for_geeks(key):
    avail1 = ['c', 'php', 'java', 'c-plus-plus', 'sql', 'python', 'php']
    avail2 = ['html', 'javascript', 'css', 'jquery']
    url = None
    if key in avail1:
        url = f'http://www.geeksforgeeks.org/{key}/'
    elif key in avail2:
        url = f'https://www.geeksforgeeks.org/{key}-tutorials/'
    try:
        res = requests.get(url)
        source = res.text
        soup = BeautifulSoup(source, 'lxml')
        link = soup.find_all('a')
        li = []
        for links in link:
            href = str(links.get('href'))
            if key.casefold() in href.casefold():
                title = href[30:].replace('/', '')
                if title != '':
                    study_materials[sep_key(title)] = href
    except:
        pass

def programmer_books(key):
    try:
        url = f' https://www.programmer-books.com/?s={key}'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        link = soup.find_all('a')
        li = []
        for links in link:
            href = str(links.get('href'))
            if key.casefold() in href.casefold() and 'page' not in href.casefold():
                books[sep_key(href[33:].replace('/', ''))] = href
    except:
        pass

def ws_vincent(key):
    url = f'https://wsvincent.com'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    link = soup.find_all('a')
    link_arr = []
    for links in link:
        href = url + links.get('href')
        if key.casefold() in href.casefold():
            link_arr.append(href)
    for i in range(5, len(link_arr) - 1):
        books[sep_key(link_arr[i][22:].replace('/', ''))] = link_arr[i]

def git_connected(key):
    try:
        url = f'https://gitconnected.com/learn/{key}'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        link = soup.find_all('a')
        li = []
        for links in link:
            if 'https' not in str(links.get('href')):
                li.append("https://gitconnected.com" + links.get('href'))
        for lin in li[19:]:
            tutorials[sep_key(lin[38:-7])] = lin
    except:
        pass
def data_incubator(key):
    url = f'https://blog.thedataincubator.com/?s={key}'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    link = soup.find_all('a')
    # li = []
    for links in link:
        href = str(links.get('href'))
        if '0' in href:
            title = href[42:-1]
            if title != '':
                blogs[sep_key(title)] = href

def hackr(key):
    try:
        url = f'https://hackr.io/tutorials/learn-{key}/amp'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        links = soup.find_all('a')
        for link in links:
            href = str(link.get('href'))
            if 'amp' in href and key.casefold() in href.casefold():
                tutorials[sep_key(href[26:-4])] = href
    except:
        pass

def frontend_masters(key):
    try:
        url = f'https://frontendmasters.com/courses/{key}/'
        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        link = soup.find_all('a')
        for links in link:
            href = str(links.get('href'))
            if key.casefold() in href:
                study_materials[sep_key(href[16:-1])] = "https://frontendmasters.com" + href
    except:
        pass

def coder_pedia(key):
    try:
        url = f'https://www.thecoderpedia.com/?s={key}'

        res = requests.get(url).text
        soup = BeautifulSoup(res, 'lxml')
        # li = []
        links = soup.find_all('a')
        for link in links:
            href = str(link.get('href'))
            if 'blog' in href:
                solve_codes[sep_key(href[35:-1])] = href
    except:
        pass

def tutorials_in_hand(key):
    url = f'https://tutorialsinhand.com/tutorials/{key}-tutorial/{key}-basics/{key}-introduction.aspx'
    res = requests.get(url)
    if res.status_code != 404:
        tutorials[sep_key(url[38:-5].replace('/', ' '))] = url
status_codes = [400, 401, 403, 404, 500, 502, 504]
def dev_mozilla(key):
    url = f'https://developer.mozilla.org/en-US/search?q={key}'
    res = requests.get(url)
    url_code = res.status_code
    if any(st_code == url_code for st_code in status_codes):
        pass
    else:
        articles[f'{key}-developer.mozilla'] = url
def coding_game(key):
    url = f'https://www.codingame.com/learn/tag/{key}'
    res = requests.get(url)
    url_code = res.status_code
    if any(st_code == url_code for st_code in status_codes):
        pass
    else:
        quiz[f'{key}-codingame'] = url

def eda_bit(key):
    url = f'https://edabit.com/challenges/{key}'
    res = requests.get(url)
    url_code = res.status_code
    if any(st_code == url_code for st_code in status_codes):
        pass
    else:
        quiz[f'{key}-edabit_challenges'] = url

def medium(key):
    url = f'https://www.google.com/search?q=medium+{key}&oq=medium+{key}&aqs=chrome..69i57.7460j0j7&sourceid=chrome&ie=UTF-8'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    link = soup.find_all('a')
    for links in link:
        href = str(links.get('href'))
        if 'medium.com' in href:
            ls = href.split('&')
            link_href = ls[0][7:]
            title = link_href[19:-13].replace('/', ' ')
            study_materials[sep_key(title)] = link_href

def dream_host(key):
    url = f'https://www.google.com/search?q=dreamhost+{key}&oq=dreamhost+{key}&aqs=chrome..69i57j0l7.6628j0j8&sourceid=chrome&ie=UTF-8'

    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    link = soup.find_all('a')
    for links in link:
        href = str(links.get('href'))
        if 'help.dreamhost' in str(links.get('href')):
            ls = href.split('&')
            link_href = ls[0][7:]
            articles[sep_key(link_href[55:])] = link_href

def common_op(request):
    get_links = Links.objects.all()
    return render(request, "courses/content/video.html", {'Links': get_links})