Philidelphia Phillies Assessment 

I was tasked with developing a method to predcit players full season On Base Percentage(OBP) with only March and Aprils 26 statistics .

Issues:
Limited data points
Only 1 years worth of data 
early in the MLB season(good players play limited games)

Methodology :
Create a linear regression in python to predict full season OBP
elimate any variables with p-value greater than .05
keep R-Squared above .60
elimate an ceoeffiects that are teh oppiste of the statistic 
  Example : if the coefficient for Homeruns(HR) = -5 but in general the more HR the better the player is . 
  

*Clean Dataset:
Drop team name , playerID, name .
Change strings to float 

*Regression Analysis :(started with 26 variables)
Elimated 12 variables 
Leaving only 15 variables:
('MarApr_PA', 'MarApr_AB','MarApr_H','MarApr_K%','MarApr_ISO','MarApr_BABIP','MarApr_AVG','MarApr_SLG', 'MarApr_HR/FB','MarApr_O-Swing%','MarApr_Z-Swing%','MarApr_Swing%','MarApr_O-Contact%','MarApr_Z-Contact%','MarApr_Contact%')

Elimated another 6 variables
Leaving 9 variables : 
which had a slightly lower r-squared than the 15 variable model but had a better F-signifigance 

<img width="486" alt="image" src="https://user-images.githubusercontent.com/101025003/200127519-2dbed977-2b15-41ac-a3ce-611d78f776c4.png">


*Proceeding with the 9 variable model :

I created a CSV with these data points
Then displayed my findings in tableau 


Findings: 
<img width="1123" alt="Screen Shot 2022-11-05 at 11 32 26 AM" src="https://user-images.githubusercontent.com/101025003/200127625-6964f4ca-90a9-4c54-96c3-659d98c74ec8.png">

left visual : model for all players 
Right visual: all players predicted with -1% - 1% error 


Problems:
model is optimistic toward lower skilled players and pesstimistic to All Star players 

<img width="1123" alt="Screen Shot 2022-11-05 at 11 36 14 AM" src="https://user-images.githubusercontent.com/101025003/200127808-94ed19d3-a6a5-46b8-9146-bfd9000d58a3.png">






