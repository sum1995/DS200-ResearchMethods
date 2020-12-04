
* * *
## Module 4 : Assignment
* * *

> **AIM:- To download a dataset from www.data.gov.in and do the following**
>> Make a scatterplot, barchart and boxplot and draw inferences from it.

### Part1: - Dataset
> The dataset is downloaded from www.data.gov.in.


### Files
> All the files are contained in the zip folder **module4**
1.  **NCRB_2009_Table_1.1.csv** is the file containing all the data. The file is same as downloaded from website, only the names of states are shortened.
2.  **ds200_module4_plots.py** is the file containing python code for the creating the graphs using _matplotlib_ library.
3.  Copy **plot_graphs.ipynb** in the **module4** folder if you want to use Jupyter Notebook.

### Part2: - Scatter Plot
> Below are two scatterplot.

![scatterplot](images/Figure_1.png)

1.  The plot on left has **Number of complaints registered suomoto by police** -i.e The cases registered by police based on their investigation - vs **Number of complaints registered as SLL** (SLL:- Special and Local Laws, these are laws which are not part of IPC and include law instituted by Acts like Gambling Act 1867, Forest Act 1927, etc) for 28 states (based on 2009 data) and 7 union territories of India.
2.  The plot on the right has **Number of complaints registered to police by oral,written or via helpline** vs **Number of cases registered as SLL**  for 28 states (based on 2009 data) and 7 union territories of India.
3.  Both the **x-axis** and **y-axis** are on log10 scale. Best fit line is also plotted in each scatter plot.
4.  **r** denotes the correlation coefficient between the data on **x-axis** and **y-axis**. 
#### The observations one can derive from the scatterplot are the following:-
1.  The number of complaints registered suomoto by the police for a state/UT are highly correlated with the number of complaints filed under SLL. 
2.  The correlation between number of complaints registered by others(not suomoto by police) are not correlated to the number of complaints filed under SLL to that extent.
3.  The regression line in plot (a) fits the data better than in plot (b).   
4.  A logical reason for this is that mostly complaints under Special and Local Laws are filed againsts an entity after investigation by law enforcers and are therefore not filed on recieving of first complaint (with few exceptions like cognizible crime under Dowry Actor SC/ST attrocity ACT).

* * *

### Part2: - Box Plot
> Below are two boxplots.

![Boxplot](images/Figure_2.png)

1.  The plot on the left shows the box plot of **Number of complaints received by police** in two catergories. First the complaints which are submitted to police by other entities via oral,written means or using police helpline for all 35 states and U.Ts. Second are the complaints that are registered by police suomoto for all 35 states and U.Ts. The first boxplot shows the number of complaints on log scale along with the outliers.
2. The second boxplot shows the same data as (1) but on a linear scale without outliers.
#### The observations one can derive from the boxplots are the following:-
1.  Looking at (b) we can say that on an average more complaints are registered by outside entities than suomoto by law enforceres.
2.  The spread in number of complaints filed by non law enforcers is more. This category also has less outliers than the other.
3.  The complaints registered suomoto by law enforcers are very high compared to the IQR in a few States/UTs and hence have more outliers.


* * *
### Part3: - Bar Chart
> Below is the Barchart which shows for all States and U.Ts (those that existed in 2009) how many complaints are filed by non law enforcers and suomoto by police.

![Barchart](images/Figure_3.png)


