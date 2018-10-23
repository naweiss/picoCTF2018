#include <iostream>

unsigned int fib(unsigned int n) {
	unsigned int term1 = 0, term2 = 1, value = 0;
	for (unsigned int i = 1; i < n; ++i)
    {
        value = term1 + term2;
        term1 = term2;
        term2 = value;
    }
	return value;
}

int main()
{
    std::cout << fib(1015) << " "; // prints 3611214637
    return 0;
}