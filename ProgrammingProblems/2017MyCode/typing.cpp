#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

char areSimliar(int*,int*,string,string,string*);
int findRow(char);

int main() {
	string letters[5] = {"         ",
						"abcdefghi",
						"jklmnopqr",
						"stuvwxyz ",
						"         "};
	int dx[] = {0,0,1,1,0,-1,-1,1,-1};
	int dy[] = {0,1,0,1,-1,0,-1,-1,1};
	string currentLine;
	int number;
	
	istringstream iss;
	ifstream inputFile;
	inputFile.open("../2017/typing.in");
	getline(inputFile,currentLine);
	iss.str(currentLine);
	iss >> currentLine;
	number = stoi(currentLine);
	
	string string1,string2;
	
	int i=0;
	for(i=0;i<number;i++)
	{
		getline(inputFile,currentLine);
		iss.str(currentLine);
		//get the strings I am comparing
		iss >> string1;
		iss >> string2;
		if(string1.compare(string2) == 0) {
			cout << '1' << endl;
		} else if(string1.length() != string2.length()) {
			cout << '3' << endl;
		} else {
			cout << areSimliar(dx,dy,string1,string2,letters) << endl;
		}
	
	}
}

char areSimliar(int dx[], int dy[], string string1, string string2, string letters[]) {
	int counter=0;
	int i=0,j=0;
	int letter =0;
	for(i=0;i<string1.length();i++)
	{
		if(string1[i] == string2[i])
		{
			counter++;
			continue;
		} else {
			for(j=0;j<9;j++) {
				if(string2[i] == letters[findRow(string2[i]) + dx[j]][dy[j]]) {
					counter++;
				}
			}
		}
	}
	if(counter==string1.length()) {
		return '2';
	} else {
		return '3';
	}
}

int findRow(char currentChar) {
	if(currentChar >= 97 && currentChar <=105) {
		return 1;
	} else if(currentChar >=106 && currentChar <=114) {
		return 2;
	} else {
		return 3;
	}
}