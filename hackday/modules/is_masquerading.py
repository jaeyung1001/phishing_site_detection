DOMAIN_LIST = ["naver", "daum", "nate",]

def is_masquerading(url):
    mod = 'is_masquerading'
    for domain_keyword in DOMAIN_LIST:
        if domain_keyword in url.lower():
            domain = get_domain(url)
            if domain_keyword in domain:
                return "S", mod
            else:
                return "P", mod
        else:
            return "U", mod

def get_domain(url):
    temp = url.index("/")
    try:
        temp = url[temp + 2:].index("/") + temp + 2
    except:
        temp = len(url) + temp + 2

    url_parsed = url[:temp]
    domain_end = temp

    temp = url_parsed.rfind('.')
    domain_start = url_parsed[:temp].rfind('.')
    if domain_start == -1:
        domain_start = url_parsed[:temp].rfind('/')
    domain = url[domain_start + 1:domain_end]

    return domain