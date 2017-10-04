#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
	string line;
	istringstream iss;
	int first,next,customers,i,hours;
	ifstream myFile;
	myFile.open("../2017/energy.in");
	
	
	getline(myFile,line);
	iss.str(line);
	string splitElement;
	vector<int> split;
	for(i=0;i<2;i++) {
		iss >> splitElement;
		split.push_back(stoi(splitElement));
	}
	
	first = split[0];
	next = split[1];
	
	getline(myFile,line);
	iss.str(line);
	iss >> splitElement;
	customers = stoi(splitElement);
	
	int money;
	
	for(i=0;i<customers;i++){
		getline(myFile,line);
		hours = stoi(line);
		cout << hours << ' '; 
		if(hours <= 1000) {
			cout << hours * first << endl;
		} else {
			money += 1000 * first;
			money += (hours-1000) * next;
			cout << money << endl;
		}
		money = 0;
	}
	
}