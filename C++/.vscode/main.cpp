#include <iostream>
using namespace std;

int main()
{
    // Constants for discounts and sales tax
    const double ROOM_COST = 100.00;
    const double DISCOUNT_1 = 0.10; // 10%
    const double DISCOUNT_2 = 0.20; // 20%
    const double DISCOUNT_3 = 0.30; // 30%
    const double ADDITIONAL_DISCOUNT = 0.05; // 5%
    const double SALES_TAX_PERCENTAGE = 0.08; // 8%

    // User input
    double roomCost, salesTax;
    int numRooms, numDays;

    // Prompt user for input
    std::cout << "Enter the cost of renting one room: $";
    std::cin >> roomCost;

    std::cout << "Enter the number of rooms booked: ";
    std::cin >> numRooms;

    std::cout << "Enter the number of days the rooms are booked: ";
    std::cin >> numDays;

    std::cout << "Enter the sales tax rate (as a percentage): ";
    std::cin >> salesTax;

    // Calculate discount based on the number of rooms booked
    double discount = 0.0;
    if (numRooms >= 10 && numRooms < 20) {
        discount = DISCOUNT_1;
    } else if (numRooms >= 20 && numRooms < 30) {
        discount = DISCOUNT_2;
    } else if (numRooms >= 30) {
        discount = DISCOUNT_3;
    }

    // Additional discount for booking at least three days
    if (numDays >= 3) {
        discount += ADDITIONAL_DISCOUNT;
    }

    // Calculate total cost
    double totalCost = roomCost * numRooms * numDays * (1 - discount);

    // Calculate sales tax amount
    double salesTaxAmount = totalCost * (salesTax / 100.0);

    // Calculate total billing amount
    double totalBillingAmount = totalCost + salesTaxAmount;

    // Output results
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "\nCost of renting one room: $" << roomCost
              << "\nDiscount on each room is " << discount * 100 << "%"
              << "\nNumber of rooms booked: " << numRooms
              << "\nNumber of days the rooms are booked: " << numDays
              << "\nTotal cost of the rooms: $" << totalCost
              << "\nSales tax: $" << salesTaxAmount
              << "\nTotal billing amount: $" << totalBillingAmount << std::endl;
    
    system("pause");
    return 0;
}
