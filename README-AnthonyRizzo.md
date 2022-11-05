Anthony Rizzo 

Task:
I was tasked to webscrape Anthony Rizzo MLB statistics from Baseball Reference.

Issues:
Without advanced HTML or CSS skills , it is difficult to sscrape the 2nd-5th table on the website . 
Due to these tables being dynamic in nature meaning the table loads as the user strolls down the page . 

Actions:
#Scrape
I use BeautifulSoup to scrape baseballreference.com
#Clean the data 
by replacing ("")

Used a for loop to scrape the html script from the baseballreference.com 

Used beautfulSoup's findall syntax to extract the tables 
  Use a for loop to go in to each table and extract the data 
  
Finally now i can switch between multiple tables dependning on location in the script 

I retrieved the WAR , year and team Anthony Rizzo played and then exported it into its own CSV. 
  







