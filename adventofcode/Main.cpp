#include <iostream>

// Edit these to launch the proper program
#include "../2018/day04/Day04_1.h"
#define DayType Day04_1
#define DayStr "../2018/Day04/Day04_input.txt"



// Execution
int main()
{
	// Load and run the program
	DayType day;
	if (day.SetUp(DayStr))
	{
		day.Run();
		day.CleanUp();
	}
	else
	{
		std::cout << "ERROR: Could not setup the program" << std::endl;
	}

	// Hold the console at the end of execution
	std::cout << "\n\n\nEND OF PROGRAM" << std::endl;
	int stop = 0;
	std::cin >> stop;

	// Return success result
	return 0;
}
