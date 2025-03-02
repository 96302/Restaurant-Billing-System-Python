{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "276fa8d9-de63-40b7-b8ff-0d8d38e10107",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to My Restaurant!\n",
      "Here is our menu:\n",
      "Pasta: RS40\n",
      "Maggi: RS50\n",
      "Sandwich: RS50\n",
      "Coffee: RS60\n",
      "Salad: RS100\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter the name of the item you want to order (or type 'done' to finish):  Pasta\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pasta has been added to your order.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter the name of the item you want to order (or type 'done' to finish):  Done\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Your Order Summary ---\n",
      "Pasta: RS40\n",
      "Total Amount to Pay: RS40\n",
      "Thank you for ordering! Enjoy your meal. 😊\n"
     ]
    }
   ],
   "source": [
    "#Project to display the order number of items added by the customer and the total bill amount.\n",
    "# Menu Dictionary\n",
    "menu = {\n",
    "    \"Pasta\": 40,\n",
    "    \"Maggi\": 50,\n",
    "    \"Sandwich\": 50,\n",
    "    \"Coffee\": 60,\n",
    "    \"Salad\": 100,\n",
    "}\n",
    "\n",
    "# Welcome Message & Display Menu\n",
    "print(\"Welcome to My Restaurant!\")\n",
    "print(\"Here is our menu:\")\n",
    "for item, price in menu.items():\n",
    "    print(f\"{item}: RS{price}\")\n",
    "\n",
    "# Initialize order list and total\n",
    "order_list = []\n",
    "order_total = 0\n",
    "\n",
    "while True:\n",
    "    item = input(\"\\nEnter the name of the item you want to order (or type 'done' to finish): \").strip().title()\n",
    "    \n",
    "    if item.lower() == \"done\":\n",
    "        break\n",
    "    elif item in menu:\n",
    "        order_list.append((item, menu[item]))\n",
    "        order_total += menu[item]\n",
    "        print(f\"{item} has been added to your order.\")\n",
    "    else:\n",
    "        print(f\"Sorry, {item} is not available in the menu!\")\n",
    "\n",
    "# Display Final Order Summary\n",
    "if order_list:\n",
    "    print(\"\\n--- Your Order Summary ---\")\n",
    "    for item, price in order_list:\n",
    "        print(f\"{item}: RS{price}\")\n",
    "    print(f\"Total Amount to Pay: RS{order_total}\")\n",
    "    print(\"Thank you for ordering! Enjoy your meal. 😊\")\n",
    "else:\n",
    "    print(\"You did not order anything. Have a great day!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b0a617e-27d9-454a-a1ee-af2b3588fb98",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
