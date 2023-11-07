import os

from zipfile import ZipFile, ZIP_DEFLATED

class Zipper:
    """
    A class used to create a zip file from a given name and path
    """

    def __init__(self, name: str, path: str) -> None:
        print("Input Parameters")
        print(f"- Name = {name}")
        print(f"- Path = {path}")

        self.name = name
        self.included_paths = self._get_included_paths(path)
        self.excluded_paths = self._get_excluded_paths(path)

        print(f"- Included Paths = {self.included_paths}")
        print(f"- Excluded Paths = {self.excluded_paths}")
        print("")


    def run(self) -> str:
        """
        Runs the logic to evaluate the name and path properties and creates a zip file from them

        Returns:
            str: The name of the zip file created
        """
        zip_name = f"{self.name}.zip"
        print("")
        print(f"Creating '{zip_name}'...")
        with ZipFile(zip_name, "w", ZIP_DEFLATED) as zip_writer:
            for path in self.included_paths:
                if os.path.isfile(path) and path not in self.excluded_paths:
                    print(f"- Adding file: {path}")
                    zip_writer.write(path)

                elif os.path.isdir(path):
                    for dir_path, _, filenames in os.walk(path):
                        for filename in filenames:
                            file_path = os.path.join(dir_path, filename)
                            if file_path not in self.excluded_paths:
                                print(f"- Adding file: {path}")
                                zip_writer.write(file_path)

        print(f"Done creating '{zip_name}'!")
        print("")
        return zip_name
    

    def _get_included_paths(self, path: str) -> list:
        paths = []
        if isinstance(path, list):
           for item in path:
               if not item.startswith("!"):
                   paths.append(item)
        else:
           paths.append(path)
       
        return paths


    def _get_excluded_paths(self, path: str) -> list:
        paths = []
        if isinstance(path, list):
            for item in path:
                if item.startswith("!"):
                    paths.append(item[1:])

        return paths



if __name__ == "__main__":
    name = os.getenv("NAME")
    path = os.getenv("PATH")
    zipper = Zipper(name=name, path=path)
    zipper.run()
