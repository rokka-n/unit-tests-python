[![wercker status](https://app.wercker.com/status/b80f6cddf82da326f7efeddeb44c9067/s/master "wercker status")](https://app.wercker.com/project/bykey/b80f6cddf82da326f7efeddeb44c9067)

# unit-tests-python

This is a collection of simple classes to help jump start with unit testing in python

# Howto use

Install python packages for unit testing
```bash
pip install -r requirements.txt
```

Check out repository, run the tests. You should see something like this.

```bash
$ nosetests -v dog_class/test_animals.py
{ ...l/unit-tests-python/dog_class }$ nosetests -v test_animals.py
test_dog_class_has_add_tricks (test_animals.animal_unittest) ... ok
test_dog_class_it_adds_tricks (test_animals.animal_unittest) ... ok
test_dog_class_name_init (test_animals.animal_unittest) ... ok
test_dog_class_prints_tricks (test_animals.animal_unittest) ... ok
test_dog_tricks_array_type (test_animals.animal_unittest) ... ok
test_zdog_class_method_print_tricks_works (test_animals.animal_unittest) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```
