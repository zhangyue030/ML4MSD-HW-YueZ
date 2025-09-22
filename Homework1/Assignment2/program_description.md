### Program Description:

This is a bill-splitting automation tool designed to simplify the monthly calculation of rent, 
utilities (water, gas, electricity), and other shared expenses. In real life, my roommate and I
need to manually calculate how much each of us should pay every month. Since we are responsible
for paying different parts (for example, I pay the rent, electricity, gas, and parking fee,
while my roommate pays the internet fee), the manual calculation process is tedious and prone
to mistakes.

With this program, the calculation becomes automated. It reads three text files 
(water_fee.txt, gas_fee.txt, electricity_fee.txt), where each line stores the fee of one month.

The program will:
1. Read monthly water, gas, and electricity fees from the text files.
2. Calculate how much my roommate should transfer to me each month, based on fixed rules 
   (rent proportion, internet fee split, parking fee fully paid by me).
3. Support multiple months of data (one line per month) and output the result for each month.
4. Save the final results into a JSON file for easy viewing and record keeping.

In this way, there is no need to repeat manual calculations with a calculator every month.
Running the program once automatically generates the complete results, achieving automation
for a repetitive real-life task and reducing the possibility of errors.