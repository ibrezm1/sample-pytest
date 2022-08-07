# Sample Setup for pytest

Important items  
* src should have __init__.py to be identified as a package
* pytest.ini created to collectly set the path of the test .. this way we can just say pytest to test 
* coverage run --source=src --module pytest &&  coverage report -m
* python -m src.tdriver
* git add . --dry-run
* Start-Service ssh-agent # for windows 

References
* [Vedio Tutorials](https://www.youtube.com/watch?v=dw2eNCzwBkk)
