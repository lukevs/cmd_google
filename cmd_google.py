from urllib import quote_plus
import sys, webbrowser

def main(argv):

    query = "+".join(map(quote_plus, argv[1:]))
    url = "https://www.google.com/#q=%s" % (query,)
    webbrowser.open(url,new=2)

if __name__ == "__main__":
    main(sys.argv)