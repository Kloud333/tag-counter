Description
===========
Calculates a number of tags in a website page

Usage
-----

* Clone the repo
  ```
  - git clone https://github.com/Kloud333/tag-counter.git
  - cd tag-counter
  ```

* Initialize and activate a virtualenv:
  ```
  - virtualenv env
  - .\venv\Scripts\activate.bat
  ```

* Install the package:
  ```
  - pip install -e .
  ```

* Run Tests:
  ```
  - python -m unittest
  ```

* Run Console version:
  ```
  - tagcounter --get ggl
  - tagcounter --get google.com
  ```

* Run GUI version:
  ```
  - tagcounter
  ```

* Work with Aliases file:
  ```
  tagcounter --aliases      //show all aliases
  tagcounter --removealias  //remove alias
  tagcounter --addalias     //add alias
  ```
