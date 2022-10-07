import sys
import webbrowser
import itertools
import threading
from time import sleep
from arguments import arguments
from searchpie.searchpie import SearchPie

Done = False


def animation():
    global Done
    Done = False
    for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if Done:
            break
        sys.stdout.write('\r' + c + " Searching...")
        sys.stdout.flush()
        sleep(0.1)


def main():
    global Done
    try:
        args = arguments()
        pie = SearchPie(args)
        if args is None:
            return
        elif args.default is True:
            print("Valid Default Params: " + ", ".join(["wiki", "movie", "tv", "anime", "manga"]))
            default = input("Enter Param: ")
            pie.default = default
            return
        elif args.key is not None and args.key != '':
            pie.api_key = args.key
            return
        elif args.show_def is True:
            print(pie.default)
            return
        t = threading.Thread(target=animation)
        t.start()
        data = pie.parser()
        Done = True
        print('\x1b[1K\r')

        if args.browser is True:
            webbrowser.open(data[0].url, new=2)
            return

        data = data[:int(args.pages)]
        for i in data:
            if args.all is True and i.identifier_type == "wiki":
                i.identifier_type = "all_wiki"
            print(i)
            if len(data) > 1:
                print("\n")
    except Exception as e:
        Done = True
        print('\x1b[1K\r')
        print(str(e))


if __name__ == '__main__':
    main()
