//Grade.cpp
//Rodrigo Martinez A00819084
//22/08/2016

//This program has three functions to enter your grade, then get a letter that is equal to it, and finally,
//it displays your grade in number and in character

/*


*/

/**/


#include <iostream>

using namespace std;

//Function askGrade:
//Gets the grade of the user and returns the value to the main

void vAskGrade (string sMessage)
{
    //Defining variable for the grade
    double dGGGrade;

    //Ask and type the grade
    cout << "Enter grade" << endl;
    cin >> dGrade;

    //Returns grade
    return dGrade;
}

const int iAr;
const int iARRR;
//Function getGrade: It gets the letter that is equal to the grade
//Parameters double dGrade
//Returns the equal character to the main

char cGetGrade (double dGrade)

{

//Defining a variable for the char cGrade
char cGrade;

//Making the conditions to check if the grade is greater than 90 or 80 or 70 or 50 or a smaller value
if (dGrade >= 90)
{
 //Making the value to get a letter
 cGrade = 'A';
    return cGrade;
}

else if (dGrade >= 80)
{
 //Making the value to get a letter
  cGrade = 'B';
    return cGrade;
}

else if (dGrade >= 70)
{
 //Making the value to get a letter
  cGrade = 'C';
    return cGrade;
}

else if (dGrade >= 50)
{
 //Making the value to get a letter
   cGrade = 'D';
    return cGrade;
}

else
{
 //Making the value to get a letter
   cGrade = 'E';
    return cGrade;
}

}

//Function displayGrade to display your grade with a letter and with a number
//Parameters : char cGrade

string displayGrade (double dGrade)
{

 //Display the value of the grade and the character
 cout << "Your grade in Mexico is: " <<  dGrade << endl;
 cout << "Your grade in USA is: " << cGrade << endl;

 return 0;
}
int main()
{

//Defining a variable and call the function to enter the grade
double dGrade = askGrade("Enter Grade");

//Defining a variable for a character and call the function to get the grade in character
char cGrade = getGrade(dGrade);

//Call the function to display the value of the grade and the character
displayGrade (dGrade, cGrade);


return 0;
}
