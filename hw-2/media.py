import os
from overrides import overrides


class EmptyDataSetException(Exception):
    pass


class File:
    def __init__(self, path: str, owner: str, creation_date: str):
        self._path = path
        self._owner = owner
        self._creation_date = creation_date

        file = None  # file = open(path, 'rb')
        self._data = []

        if file:
            byte = file.read(1)
            while byte:
                self._data.append(byte)
                byte = file.read(1)
            file.close()

    def save(self, path: str):
        file = open(self._path, 'wb')
        if not self._data:
            raise EmptyDataSetException()
        for byte in self._data:
            file.write(byte)
        file.close()

    @property
    def size(self):
        try:
            return os.path.getsize(self._path)
        except FileNotFoundError:
            return 0

    @property
    def path(self):
        return self._path

    @property
    def owner(self):
        return self._owner


class Video(File):
    def __init__(self, path: str,
                 owner: str,
                 creation_date: str,
                 fps: int):
        super().__init__(path, owner, creation_date)
        self._fps = fps

    def play(self):
        # playing video file
        pass

    def stop(self):
        # stops video
        pass

    @overrides
    def save(self, path: str):
        # append some additional data to _data
        super().save(path)

    @property
    def fps(self):
        return self._fps


class RemoveVideo(Video):
    def __init__(self,
                 url: str,
                 path_to_save: str,
                 owner: str,
                 creation_date: str,
                 fps: int):
        # create file (path_to_save) and download data via url
        # ...
        super().__init__(path_to_save, owner, creation_date, fps)
        self._fps = fps


class Audio(File):
    def play(self):
        # playing video file
        pass

    def stop(self):
        # stops video
        pass


class Image(File):
    def invert_colors(self):
        # inverts colors
        pass

    def get_region(self, x: int, y: int, width: int, height: int):
        # uses passed params to get rect from image
        pass


if __name__ == "__main__":
    v = Video("incorrect_path", "name_surname", "15.03.2024", 60)
    print(v.path)
    print(v.owner)
    print(v.fps)
    print(v.size)
    v.play()
    v.stop()

    try:
        v.save(v.path)
    except EmptyDataSetException:
        print("There is no data to save")

    print("------------------")

    rv = RemoveVideo("youtube",
                     "incorrect_path",
                     "name_surname",
                     "15.03.2024",
                     120)
    print(rv.path)
    print(rv.owner)
    print(rv.fps)
    print(rv.size)
    rv.play()
    rv.stop()