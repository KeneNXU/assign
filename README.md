## Data Analysis

## Introduction

This project collects data and performs data analysis on the data collected

1. **Install the dependencies:**

```
pip install -r requirements.txt
```

2. **Database Setup:**
   Make sure mongodb is running and create a mydatabase database with a users collection

3. **Run the development server:**

```
py app.py
```

3. **Verify on the Browser**<br>
   Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000)

4. **Data Analysis**<br>
   Run the following command in the main directory to create a csv file from the mongo database

```
python models.py
```
