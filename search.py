from search_factory import SearchFactory
import argparse

if __name__=='__main__':
    arg_parser = argparse.ArgumentParser(description='Search Algo')
    arg_parser.add_argument('--range', type=int)
    arg_parser.add_argument('--target', type=int)
    arg_parser.add_argument('--search', type=str)

    args = arg_parser.parse_args()

    A = list(range(args.range))
    target = args.target
    search_engine = SearchFactory.get_handler(args.search)
    position = search_engine.search(A,target)

    print(f'position = {position}')