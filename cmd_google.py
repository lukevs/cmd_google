from urllib import quote_plus
import sys
import webbrowser

def main(argv):

    source = sys.stdin.readlines() if len(argv) == 1 else argv[1:]
    query = "+".join(map(quote_plus, source))

    url = "https://www.google.com/#q=%s" % (query,)
    webbrowser.open(url,new=2)

if __name__ == "__main__":
    main(sys.argv)