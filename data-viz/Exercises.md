-   Create an additional function scatter_plot that takes a data frame df and plot relationship between the following two attributes:

displacement over x-axis
acceleration over y-axis

<!-- Exercise 1 -->

-   Create an additional function bar_plot that takes a data frame df and compares the cylinders of all the cars from 1975 model_year and ford company.

To check whether a car is owned by ford company, you can use the following line:

df.car_name.str.contains('ford')

<!-- Exercise 2 -->

-   This statement will only be true for the cars of the ford company, that’s how you can filter the cars.

To check whether a car belongs to model-year of 1975, you can use the following line:

df["model_year"].isin([75])

This statement will only be true for the cars of the 1975 model_year.

Try to implement the function below. Good Luck!

-   Create an additional function line_plot that takes a data frame df and then plots the change in weight throughout the years for the cars of ford company.

<!-- Exercise 3 -->
