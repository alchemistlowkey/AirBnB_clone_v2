#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.engine.file_storage import FileStorage
from models.user import User


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """
        FileStorage object storage created
        """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """
    class for testing FileStorage class' methods
    """
    temp_file = ""

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_FileStorage(self):
        """
        Test that file_storage.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/file_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_FileStorage(self):
        """
        Test that test_file_storage.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_file_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    @staticmethod
    def move_file(src, dest):
        """
        Move file
        """
        with open(src, 'r', encoding='utf-8') as myFile:
            with open(dest, 'w', encoding='utf-8') as tempFile:
                tempFile.write(myFile.read())
        os.remove(src)

    def setUp(self):
        """
        Setup
        """
        self.temp_file = '/temp_store.json'
        self.temp_objs = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.temp_objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        """
        Initialized object
        """
        del self.temp_objs

    def test_type(self):
        """
        Type checks for FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """
        Tests save functionality for FileStorage
        """
        with open('file.json', 'r', encoding='utf-8') as myFile:
            dump = myFile.read()
        self.assertNotEqual(len(dump), 0)
        temp_d = eval(dump)
        key = self.temp_objs[0].__class__.__name__ + '.'
        key += str(self.temp_objs[0].id)
        self.assertNotEqual(len(temp_d[key]), 0)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(temp_d[key2], KeyError)
        except:
            pass

    def test_reload(self):
        """
        Tests reload functionality for FileStorage
        """
        storage.reload()
        obj_d = storage.all()
        key = self.temp_objs[1].__class__.__name__ + '.'
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEqual(obj_d[key].id, self.temp_objs[1].id)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass

    def test_delete_basic(self):
        """
        Tests delete basic functionality for FileStorage
        """
        obj_d = storage.all()
        key2 = self.temp_objs[2].__class__.__name__ + '.'
        key2 += str(self.temp_objs[2].id)
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass

    def test_new_basic(self):
        """
        Tests new basic functionality for FileStorage
        """
        obj = BaseModel()
        storage.new(obj)
        obj_d = storage.all()
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.assertEqual(obj_d[key] is obj, True)

    def test_new_badinput(self):
        """
        Tests new bad input functionality for FileStorage
        """
        try:
            self.assertRaises(storage.new('jwljfef'), TypeError)
            self.assertRaises(storage.new(None), TypeError)
        except:
            pass
