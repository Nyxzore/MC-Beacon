#include <iostream>
#include <iomanip>
#include <vector>

class Odometer {
private:
    std::vector<int> digits;
    int base; 

public:
    Odometer(int numDigits, int base = 10) : digits(numDigits, 0), base(base) {}

    // Increment the odometer
    bool increment() {
        for (int i = digits.size() - 1; i >= 0; --i) {
            digits[i]++;
            if (digits[i] < base) {
                return true; // no carry needed
            } else {
                digits[i] = 0; // carry to next digit
            }
        }
        return false;
    }

    std::vector<int> get_digits() const{
        return digits; 
    }

    void print() const {
        for (int d : digits) {
            std::cout << d;
        }
        std::cout << std::endl;
    }
};
