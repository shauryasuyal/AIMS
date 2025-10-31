
# Data Preprocessing Techniques

This project demonstrates three fundamental data preprocessing techniques used in machine learning - Ordinal Encoding, One Hot Encoding, and Imputation, implemented using only basic Python, Pandas, and NumPy, without using predefined helper functions like get_dummies() etc. 

It is designed for beginners and students who want to understand the logic behind encoding and imputation rather than relying on built-in libraries. The project helps learners grasp how categorical data can be converted into numerical form and how missing data can be handled manually before feeding it into machine learning models.













## Additional Information

1. **Ordinal Encoding:**    

Converts categorical data into numerical form based on their inherent order.

This helps machine learning models interpret ordered data correctly.
The code dynamically detects unique categories and assigns increasing numerical values instead of hardcoding them.

2. **One Hot Encoding:**

Transforms categorical variables into binary columns for each unique category.
Each original category gets its own column, and rows are marked with 1 where the category is present.
This is useful when there is no inherent order among categories.
The code automatically finds all unique categories and encodes them dynamically.

3. **Imputation:**

Handles missing data by filling them with calculated values.
The code demonstrates mean, median and mode imputation.
This ensures that missing values don’t interfere with data analysis or machine learning model training.



## Deployment

To deploy this project run

```bash
python Ordinal Encoding.py
python One Hot Encoding.py
python Imputation.py

```
Each of the above scripts can be run individually in a terminal or IDE that supports Python 
Make sure you have **Python 3, Pandas, and NumPy** installed before running the scripts.

If required, install dependencies using:

```bash
pip install pandas numpy

```


## Authors

- [@shauryasuyal](https://www.github.com/shauryasuyal)


## Feedback

If you have any feedback, please reach out to me at suyalshaurya0207@gmail.com


## License

**MIT License**

**Copyright (c) 2025 Shaurya Suyal**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

