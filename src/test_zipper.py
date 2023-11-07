import os
import pytest
import shutil

from zipfile import ZipFile
from zipper import Zipper

class TestZipper:
    DIR_TEMP = "temp"
    DIR_EXTRACTED =  os.path.join(DIR_TEMP, "extracted_files")

    DIR_TEST_ROOT = os.path.join(DIR_TEMP, "root")
    PATH_TEST_FILE_1 = os.path.join(DIR_TEST_ROOT, "file_1.txt")

    DIR_TEST_FILES = os.path.join(DIR_TEST_ROOT, "test_files")
    PATH_TEST_FILE_2 = os.path.join(DIR_TEST_FILES, "file_2.txt")
    PATH_TEST_FILE_3 = os.path.join(DIR_TEST_FILES, "file_3.txt")

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        # setup
        self._remove_temp()

        os.makedirs(self.DIR_TEST_FILES, exist_ok=True)
        os.makedirs(self.DIR_EXTRACTED, exist_ok=True)

        self._create_test_file(self.PATH_TEST_FILE_1)
        self._create_test_file(self.PATH_TEST_FILE_2)
        self._create_test_file(self.PATH_TEST_FILE_3)

        # yeild devides setup from teardown
        yield

        # teardown
        self._remove_temp()


    def test_dir_with_files(self):
        name = "Test Directory with Text Files"
        
        print("")
        print("#################################")
        print(name)
        print("#################################")

        path = self.DIR_TEST_FILES

        zipper = Zipper(name, path)
        zip_name = zipper.run()

        self._extract_zip(zip_name)

        assert not self._has_file(self.PATH_TEST_FILE_1)
        assert self._has_file(self.PATH_TEST_FILE_2)
        assert self._has_file(self.PATH_TEST_FILE_3)


    def test_single_file_in_dir(self):
        name = "Test Single File in Directory"
        
        print("")
        print("#################################")
        print(name)
        print("#################################")

        path = self.PATH_TEST_FILE_2

        zipper = Zipper(name, path)
        zip_name = zipper.run()

        self._extract_zip(zip_name)
        
        assert not self._has_file(self.PATH_TEST_FILE_1)
        assert self._has_file(self.PATH_TEST_FILE_2)
        assert not self._has_file(self.PATH_TEST_FILE_3)


    def test_single_file_at_root_dir(self):
        name = "Test single Text File at Root Directory"

        print("")
        print("#################################")
        print(name)
        print("#################################")

        path = self.PATH_TEST_FILE_1

        zipper = Zipper(name, path)
        zip_name = zipper.run()

        self._extract_zip(zip_name)

        assert self._has_file(self.PATH_TEST_FILE_1)
        assert not self._has_file(self.PATH_TEST_FILE_2)
        assert not self._has_file(self.PATH_TEST_FILE_3)


    def test_multiple_files_and_exclusion(self):
        name = "Test with Root file and dir files"

        print("")
        print("#################################")
        print(name)
        print("#################################")

        path = [
            self.PATH_TEST_FILE_1,
            self.DIR_TEST_FILES,
            f"!{self.PATH_TEST_FILE_3}",
        ]

        zipper = Zipper(name, path)
        zip_name = zipper.run()

        self._extract_zip(zip_name)

        assert self._has_file(self.PATH_TEST_FILE_1)
        assert self._has_file(self.PATH_TEST_FILE_2)
        assert not self._has_file(self.PATH_TEST_FILE_3)


    def _remove_temp(self):
        if os.path.exists(self.DIR_TEMP):
            shutil.rmtree(self.DIR_TEMP)


    def _has_file(self, file_path: str) -> bool:
        has_file = False
        for dir_path, _, files in os.walk(self.DIR_EXTRACTED):
            for file in files:
                path_current_file = os.path.join(dir_path, file)
                if file_path in path_current_file:
                    has_file = True
                
        print(f"Has {file_path} in Zip?: {has_file}")
        return has_file


    def _extract_zip(self, zip_name: str):
        with ZipFile(zip_name, "r") as zip:
            zip.extractall(self.DIR_EXTRACTED)


    def _create_test_file(self, path: str):
        two_mb = 1 * 1024 * 1024
        with open(path, "w") as f:
            f.write("*" * two_mb)

