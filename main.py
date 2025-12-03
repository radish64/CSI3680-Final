import requests
from bs4 import BeautifulSoup
import pandas as pd

aurl = "https://www.amazon.com/s?k=ddr5+ram+32gb"
burl = "https://www.bestbuy.com/site/searchpage.jsp?st=ddr5%20ram%2032gb"

a2url = "https://www.amazon.com/s?k=nvidia+rtx+5090"
b2url = "https://www.bestbuy.com/site/searchpage.jsp?st=nvidia%20rtx%205090"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
aheaders = {
"Host": "www.amazon.com",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br, zstd",
"DNT": "1",
"Sec-GPC": "1",
"Alt-Used": "www.amazon.com",
"Connection": "keep-alive",
"Cookie": "session-id=140-8659005-4293526; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; csm-hit=tb:8YT9SCEK9J0628F03XJM+s-JSH87MF03BXG0YXJ2NY8|1764701835266&t:1764701835266&adb:adblk_yes; ubid-main=132-0085306-8682460; session-token=NDhnwNB22IRgfluQ32U2NGV8Ypv2ZaiKvaryfXBZIHlZLsq0fr+KL9EubFKojZbD2+YT6SHiZOvQporNnPn+YkhB+BM+iiUFpkDtbb4b6PLjtaCnXrt9a7jW9AxEhMLZz/4vIQhCJQKpTLQB7Obj1tnaPn4H/8LCDoTLHECkNuFzOLmtbANqBQQZuLgD3PxRNYQKFxC8D93+Z2My+xRFw6DZI2c1fQQXwtDt6bt9/UuzCt9XhuJNpR+cmrmGJaq9Dk1ytCaOq2U3kKNAYUiSK7Y74+ikiqV77c4SQ6pYJJIfk68hsWMxRBnIKWWwWPdgUHdZ9m5LcNxfvCJVBh9WD1vkyt09E9kp; skin=noskin; rxc=AAAA",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"Priority": "u=0, i"
}

bheaders = {
"Host": "www.bestbuy.com",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Referer": "https://www.bestbuy.com/home",
"DNT": "1",
"Sec-GPC": "1",
"Connection": "keep-alive",
"Cookie": "SID=35d56986-ddbe-45d8-a72c-611ae4095396; CTT=16eedcba271c9d2ba5c29a4c013bfb0e; bby_rdp=l; bm_ss=ab8e18ef4e; _abck=20FF7AE91FBDB3C146CE1DD1234BCA8A~-1~YAAQTCM+F6EGu9WaAQAAjIh64A5tivxHJ/MnhjY35a5PU1taMff3uCmI43z3yTTct9da4rsxtB0MPhaXMJcVS06cVhhXvLUoFvBw2k9ZIejwnxC7N5463yAdL+g32Fa3uFF7vFaynrGC1Fg/FEuh4WhQJMS1stthdZ3nCvqdBOIRXgUvjZ+5CNW/QuiLXzuzLA06daLHTDLRl0aI85Uxx39+955nYHpZEqf4j9FtNIMBWnALrhU5U6809CkF17+GmG2WjNBgY7z2vsfSPVOvTj9HaFm17lBO8TkVxtq6hGNRGue9tisvDwDNHKbJrMqX8wbT86bod+MspWlG7X/Q6HK2ZbTIKX1vc6fEbEoFospPpZh+4KeoSPIgaMHHFnkifNDQ65EpYBLj0ctVBnXDLH6Idi8Bd2UT4jLDG5w7nDlMsrCy2yM30DJVzJExIPJKeATKaIpyujWIZygOdsQbGS+pvltXbX+YFpzHg5frxE4P4Jm3pwSRRChI9QRVUVO/QG/i6syc8nRDdaE/cAFQz94+HPSFiEQvTlTejRXiW6ojLWD4dg8HZnMnrOXFNo/3DJvIAQToP8zyM981isox8xrPpxhyipuTaVL41lgIRZLF2+ECZrSQP8TCCVhoZN2neqbfyCGzl4cMochehG39SlYm9eJJIk/d1v39S+q5KoZM2NXc~-1~-1~1764704478~AAQAAAAE%2f%2f%2f%2f%2f2BQ%2fy3zn33riOYJQEmNjuApUo2ejI5aI%2fXl3RI1zLJZae9GLwWNOTOHlUNn7tlH7WdDuePZWjQYB6Utg3RP9vtJc8Hvdfaey9O4~-1; bm_s=YAAQTCM+F6IGu9WaAQAAjIh64AQE4/3yTu7J8Y7+bnLvmMV0v5sQ78KDtlWpyelk3i6NPra/IgyAIEs4rkGMLYl2HILkz0DxDjb5IPwGKqmOjDo1P5mQM81CoInWZsNmupoH3qqMrUvduY2CiJ/KeVsyVkp5CKNg68VJHSfR694MNjdU/vPoyR7hYFVE3ZaJ3qKIng4qTy4hyO2zcZxp6yy9yIRkSEaBpy4AL0xD02xaPmaDbHvWJdyEidLYWA/2RDUqbn93KHdv9aZRzhm4ZaWNcPZiuSmG4MK3xm9FWJ0pigHqgGUMt2Jl5ihIaZNIfMZO4A+/mPUBOHq1LaWnVNDQ/Gme8Rep6egDpN5VWcqFaMi8Yejbu++sE7PQ7WDwuhALnqVn43qSFsLqdLmVUej07phVU0z3EOChtSIuPXG5A3CnxM0QMoY4R0HRbIfihE8ADJEhKd6JmXHm14MMb+ndFmpD+j7sfunhttxHze430hTtU/hTgQYyMx5GfxzbPj6DqFqdd/gXoN7fdP9j51kFkzui6AGm72bWGnZ1Onh7yWZ0TNsl6OJl9sXw8dPgzg==; bm_so=8CA0570D50D6EE631A4AC68BEE7D07F50D2E0F812F02FFC39766A4BBFBD6F957~YAAQViM+F4NjIqyaAQAA01t64AU5UAcykx2kAWLkfiDraW0SGgRPFaJ9WMCbriqSD/LP9xND3gBcOQLD0I4zEV+YHbMitNe+bGYCNuUpnWGLwShFMfB/V33TMZUsbfIqZayXMFjMzB+OdXtDMBG3Irhcw7Qctfv8bEEcCvJQszv1hBejmmbOP9dPSDXnHh5sFfp76vdb1nzJ4xzowQWZ5jghC5IclRa8jCg0qTEvSDHi+ueJEgqe066UMEmUF0Jp/fFgXMBtN9JhJEM1fYB0B1xgwkM89l2HE+1zJElJVkJ4Z/TanXVZ+T6g6sn40cA6cyJzQWCdquslSPLtMszRl1D+0QBSZ3rptKt1MXEMU1srCQmL9Kz0Tq6wbEcnhtG/y7b/34sA00YZ9jZhzJ/W6bybAa2U94fI7qOtVqta49YB5hqqEiHDcylXkFMdz+1KJfN0/Kf9RXiQGvlQY2w=; bm_sz=A95C055012A756649BD05CB4816EE214~YAAQViM+F4RjIqyaAQAA01t64B1i1MHbw5JOY5SSpIJOuGYheJXY5MURpH5tQqiwnFLdJf6PZshrAfxGQGSQJhuvtA0g3IelMdR8eWrWsBBtYcs8f8R6Sudo/LGokty9IUHMcsfFtXZN6jF60EuBigN7CRiDi9nNyNw4HFShk6B8YW0lneYzoBLTmAnruxcI+55fWIvdbPosZaG3+nD6aTTHb0IZfnYIrpb7zPIfpFvW7NPV2KWqRPbrBUolzKwtz79v5LULgVVh76GSizpkW6LJ1k0GZLxmbm/qlcyVjEHNZnnzDaGLQRfo4ip/Uc87cOsw0kKBx6xTP8sSqoP0aQgwX5VF5kvIVYS32ySheyaSy40/UXt9kBSsFwSKZz13UQ4LsMoFF6T3zshyDQDja8IlwNOv/oBqjoFmzAai4zK1YNp0sFGqHVbudSFV3BrewVZIig48PyX5+8H9~3621186~3224628; vt=7c2a955e-cfae-11f0-b2f0-0eca03eb2237; dtCookie=v_4_srv_7_sn_OIVVR2BBJU9FH8174UJOATMFMBI2N4RO_app-3Ace21993b1022d2c8_1_app-3A230be8cef7973e6b_1_ol_0_perc_100000_mul_1; rxVisitor=1764700878787CK12DCBG97R7UB78RCRCGJHKCR0GLN5G; dtPC=7$102710066_922h-vHRSHTQLBHNTPBKOQCNUCUDFSMCAUKSRP-0e0; rxvt=1764704514540|1764700878788; dtSa=-; bm_lso=8CA0570D50D6EE631A4AC68BEE7D07F50D2E0F812F02FFC39766A4BBFBD6F957~YAAQViM+F4NjIqyaAQAA01t64AU5UAcykx2kAWLkfiDraW0SGgRPFaJ9WMCbriqSD/LP9xND3gBcOQLD0I4zEV+YHbMitNe+bGYCNuUpnWGLwShFMfB/V33TMZUsbfIqZayXMFjMzB+OdXtDMBG3Irhcw7Qctfv8bEEcCvJQszv1hBejmmbOP9dPSDXnHh5sFfp76vdb1nzJ4xzowQWZ5jghC5IclRa8jCg0qTEvSDHi+ueJEgqe066UMEmUF0Jp/fFgXMBtN9JhJEM1fYB0B1xgwkM89l2HE+1zJElJVkJ4Z/TanXVZ+T6g6sn40cA6cyJzQWCdquslSPLtMszRl1D+0QBSZ3rptKt1MXEMU1srCQmL9Kz0Tq6wbEcnhtG/y7b/34sA00YZ9jZhzJ/W6bybAa2U94fI7qOtVqta49YB5hqqEiHDcylXkFMdz+1KJfN0/Kf9RXiQGvlQY2w=^1764702712419; lux_uid=176470087912794828; ak_bmsc=C7B936AABB631F7F51C80D4AA9CE1CC7~000000000000000000000000000000~YAAQViM+F11jIqyaAQAA5Fl64B1uz7EXDonYUG9z+pQSH3oIlMJGgVqWnxR9ne9eQmX09xbkc7uLYpTjRUkSDgtjoWOYgAc2b9ywfC+LCS6cckbKw8RdbR2+AYSVMbhmxiEuTED7T20So7EYz+2y8ZKVrkQLiol162pNTrSwaDdHI+1ULYl6e0Iv9vvsPJPl6841yNe9xtVmXxCP3NgnCOJjrJ5hGqUwbyYKIGTg5v3a8PRjy/+QvWrjiAacljMes4tASlUK4Hb1xkjk7IzXUWxC3DU3XXIQcDPziyDxr8C/Wla1SJm6jEQRxr+vl6lrfYeColuMC1mUZ6QW2vUWNlge8NqHIRol4nzhQC3f5HD/fIdiwH4R99RCVl++qheqD5NDKrpBWUnNqyEU4bzwsUN9kA1zZJkQ0xvP5wE7iUWYb6Qforn1hKvuifGCZilroNAM/l/KWrkeyFhcHA==; pst2=411|N; physical_dma=513; customerZipCode=48706|N; isGridViewEnabled=true; bm_mi=BFFDD4683715999A00E22E034F802AF3~YAAQLiM+F2wf/a+aAQAAP/pf4B0emqzvbdtsRUwgRR/+LUJKvbHgXUXUoQDTEE8lvnnTLYnHHuQyegPCxCaB3y5fKrGSXAHfASOVNmf2cQIM1ogZCgjffKDFv46tmPBWOMYra97B7mrlmyEk/LyNROVSM9w6JODYWsOWZ9ix5bur2GOv65x1LRXId6PxtuLUuj/doTF7OFbRl+OhejIrnzemJi+UY73q4PtprqKOFRY1iRwyNBOVl6QImcreg+fAn3C8H5/MIbN8kTo2mvSTBGCJ0txjpX11JxEAMUf0NZYKsVzTMOG0WRASmJMGZm/HVcTX0s50h8eyUs5s3Fw2tCq/~1; AWSELB=55439F380340EEA77B0C6759DBBB7545739BF62F61BD925B4D57691B479DAB2A110E3C846E781894F62AA0CF3289A90E99167A3B695D6AF84DE71733BC69CFA606542A94; AWSELBCORS=55439F380340EEA77B0C6759DBBB7545739BF62F61BD925B4D57691B479DAB2A110E3C846E781894F62AA0CF3289A90E99167A3B695D6AF84DE71733BC69CFA606542A94; bby_cbc_lb=p-browse-e",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1",
"Priority": "u=0, i",
"TE": "trailers"
}

ares = requests.get(a2url, headers=aheaders)
#bres = requests.get(b2url, headers=bheaders)

print(ares)
#print(bres)

asoup = BeautifulSoup(ares.content, 'html.parser')
#bsoup = BeautifulSoup(bres.content, 'html.parser')

products = asoup.find_all('div', {'class': 's-main-slot s-result-list s-search-results sg-row'})
product_names = []
prices = []
for product in products:
    name = product.find('a', {'class': 'a-text-normal'})
    price = product.find('span', {'class': 'a-price-whole'})
    #name = product.find('a', {'class': 'a-text-normal'})
    #price = product.find('span', {'class': 'a-offscreen'})
    if name and price:
        product_names.append(name.text)
        prices.append(price.text)
        print(product_names, prices)
        # Save to CSV
        data = {'Product Name': product_names, 'Price': prices}
        df = pd.DataFrame(data)
        df.to_csv('amazon_products.csv', index=False)

#res.raise_for_status()
