## Discount mini service
### Description
This is a tiny application for calculating customer discounts. The goal is to make discount rules easy to build & KISS principe. This application requires php, python to play with it.
Here is no strong concentration on data types and accuracy of calculations. The main purpose is to build similar structure in python equals to php structure. But the results of calculating expects approximately to be correct. Inspired from some people who write structures in php. Just trying to do the same in python.
### Usage and logic
To run from php:<br />
Just serve this from php build-in server
```
php -S localhost:7777
```
From index.php this will goes to python with one argument: order_id.
Then python will return resulting array back to elephant which will dump this array to the screen.<br />
To run without php:
```
python discount.py order_id
```
To perform unit test:
```
python -m unittest discover tests "*_test.py"
```
### Todo Questions
In context:
- if you buy five you got sixth for free, - if you buy twenty you got four for free? 
ATM this will not implemented, instead when buy five you got sixth free only.
- also if you got free item - discount should includes product price? (e.g 0 + unit price of gift)
### Used Literature and links
- http://www.u.arizona.edu/~erdmann/mse350/topics/list_comprehensions.html
- https://www.tutorialspoint.com/python/python_classes_objects.htm
- https://docs.python.org/2/library/unittest.html
- https://en.wikipedia.org/wiki/Microservices
- github
- Design Patterns in PHP and Laravel (strategy pattern) :smile:








