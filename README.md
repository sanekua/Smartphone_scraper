This is Amazon scrapping project.

After scraping amazon website we get information about smartphones:
-name of the smartphone
-corporation
-current smartphone price
-smartphone image

The extracted data looks like this sample

{'product_corp': ['Apple'],
 'product_image': ['https://images-na.ssl-images-amazon.com/images/I/51N9JNplyoL._AC_US218_.jpg'],
 'product_name': ['Apple iPhone 6s Plus a1687 32GB, Rose Gold - LTE CDMA/GSM ''Unlocked (Renewed)'],
 'product_price': ['228']
 }

We store our results in MySQL Database, extracted data looks like this

'Apple iPhone 6s Plus a1687 32GB, Rose Gold - LTE CDMA/GSM Unlocked (Renewed)', 
'Apple',
'228',
'https://images-na.ssl-images-amazon.com/images/I/51N9JNplyoL._AC_US218_.jpg'
 store our results in MYSQL