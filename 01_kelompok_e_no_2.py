# -*- coding: utf-8 -*-
"""01_Kelompok E_No 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RgAEWj2kNUaiH4IKMGHxiF4WBSnYKblO

Paper Money: <br>
1. Rp 100,000    
2. Rp 50,000   
3. Rp 20,000   
4. Rp 10,000   
5. Rp 5,000   
6. Rp 2,000
<br>
<br>
Coins: <br>
1. Rp 1,000  
2. Rp 500  
3. Rp 200
4. Rp 100  
*To make it easier, we assume that all Rp. 1000 denominations are coins.

There are circumstances where the bank must liquidate all customer savings in the form of money, if the customer requests it.
And imagine this is happening right now in front of you, help the bank to calculate how many denominations of money are needed.

Here is the rule:

1. Bank must prioritize the largest denominations first to be issued.
2. If there is a balance that cannot be cashed, the bank must inform it.
3. Bank must calculate how many number of Paper Money needed and Coins needed.
4. Banks can only disburse a maximum amount of 1 billion Rupiah



Make a python code that receives an integer number of customer savings from 0 - 1 Billions.
"""

try:
    num = int(input("Input\n>> "))
    print("You entered:", num)

except ValueError:
    print("Please input a valid number")

#Create the code here
def cash_out(num):
  #Daftar denominasi dalam urutan menurun
  denominations = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

  #Dictionary untuk menyimpan jumlah setiap denominasi
  denomination_count = {denom: 0 for denom in denominations}

  #Inisialisasi total untuk uang kertas dan koin
  total_paper_money = 0
  total_coins = 0

  #Iterasi setiap denominasi dan hitung jml uang kertas/koin
  for denom in denominations:
      if num >= denom:
        count = num // denom
        denomination_count[denom] = count
        num %= denom

  #Hitung total uang kertas dan koin
  for denom in denominations:
      if denom >= 1000:
        total_paper_money += denomination_count[denom]
      else:
        total_coins += denomination_count[denom]

  #Output
  for denom in denominations:
      print(f">> Amount of currency Rp {denom:,}: {denomination_count[denom]}")

  print(f"\n>> Total Paper Money: {total_paper_money}")
  print(f">> Total Coins: {total_coins}")
  print(f">> Cannot be cashed out: {num}")

try:
  batas_maksimal = 1000000000
  if num < 0:
      print("Output")
      print(">> Please input the correct number")

  elif num > batas_maksimal:
      print("Output")
      print(f">> Maximum Saving is {batas_maksimal}")

  else :
      print("Output")
      cash_out(num)

except NameError:
    print("Please input a valid number")
