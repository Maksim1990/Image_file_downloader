from urllib import request

apple_url = 'https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportCompleteSample.csv?view=kc'

def download_file(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    dest_url=r'goog.scv'
    fx=open(dest_url, "w")
    for line in lines:
        fx.write(line+'\n')
    fx.close()

download_file(apple_url)