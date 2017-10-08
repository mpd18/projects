#include <iostream>
#define PI 3.14159

using namespace std;

class TestClass {
	protected:
		double testMember;
		
	public:
		double getTestMember(void) {
			return this->testMember;
		}
		double setTestMember(double data) {
			this->testMember = data;
		}
		
};

int main() {
	TestClass test;
	test.setTestMember(45*12*PI);
	cout << test.getTestMember() << endl;
	return 0;
}