import re
import time
#from urllib.request import urlopen
#from urllib import request
import urllib.request



# GET MARKET CAP
def TickerKeyStats():


    print("-----------------------------")
    #sourceCode = urllib.request.urlretrieve('https://www.google.com/search?q=raccoon&safe=off&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiS4aPKyqLUAhXM4IMKHVSAAqAQ_AUICigB&biw=982&bih=475').read()
    #sourceCode = str(sourceCode)

    # req = urllib.request.Request('https://www.google.com/search?q=raccoon&safe=off&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiS4aPKyqLUAhXM4IMKHVSAAqAQ_AUICigB&biw=982&bih=475')
    # with urllib.request.urlopen(req) as response:
    #     the_page = response.read()

    req = urllib.request.Request('https://pixabay.com/en/photos/raccoon/')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()


        #from urllib import request
        #request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")

        # a = re.split(r"\W", s)
        #re.match(pattern, string, flags=0)
        outFile = open("html_text.txt", 'w')
        outFile.write(str(the_page))

        regex = "http(.*)raccoon(.*)\.jpg"
        yrHi = re.findall(regex, str(the_page))
        print(len(yrHi))
        # for item in yrHi:
        #     print(item)
        # print("!!")



    # except:
    #     print("-----------------------------")
    #     print(" - Error!!")


TickerKeyStats()



