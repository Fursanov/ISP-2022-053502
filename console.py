import sys

from json_files import json_serializer


if __name__ == "__main__":
    if len(sys.argv) > 1:
        json_serializer.dump(json_serializer.loads(sys.argv[1]),
                             sys.argv[2], int(sys.argv[3]))
        print('объект сериализован в файл ' + sys.argv[2])
