{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is outside the function\n"
     ]
    }
   ],
   "source": [
    "# a collectiion of instructions or collection of code\n",
    "#here, the function1 has been defined as a collection of the two print functions\n",
    "\n",
    "def function1():\n",
    "    print(\"ahhhh\")\n",
    "    print(\"ahhhhh 2\")\n",
    "print(\"this is outside the function\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ahhhh\n",
      "ahhhhh 2\n"
     ]
    }
   ],
   "source": [
    "function1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ahhhh\n",
      "ahhhhh 2\n"
     ]
    }
   ],
   "source": [
    "function1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def name():\n",
    "    print(\"Niro\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Niro\n"
     ]
    }
   ],
   "source": [
    "name()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ahhhh\n",
      "ahhhhh 2\n",
      "Niro\n"
     ]
    }
   ],
   "source": [
    "function1()\n",
    "name()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# mapping; input or an argument, x is taken and the output is 2*x\n",
    "\n",
    "def function2(x):\n",
    "    return 2*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'function' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-8-e1b6a0a537bf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mfunction\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'function' is not defined"
     ]
    }
   ],
   "source": [
    "function(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-9-6da5e47935b8>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-9-6da5e47935b8>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    function(2):\u001b[0m\n\u001b[0m                ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "function(2):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-10-5e26ee222be6>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-10-5e26ee222be6>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    a = function(2):\u001b[0m\n\u001b[0m                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "a = function(2):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "function2(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = function2(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = function2(18)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36\n"
     ]
    }
   ],
   "source": [
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.3333333333333333\n"
     ]
    }
   ],
   "source": [
    "print(a/b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = function2(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def function3(x, y):\n",
    "    return x + y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "e = function3(1, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "def function4(x):\n",
    "    print(x)\n",
    "    print(\"still in this function\")\n",
    "    return 3*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "still in this function\n"
     ]
    }
   ],
   "source": [
    "f = function4(8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "print(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def function5(some_argument):\n",
    "    print(some_argument)\n",
    "    print(\"wee\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "wee\n"
     ]
    }
   ],
   "source": [
    "function5(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-26-401fec062c4a>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-26-401fec062c4a>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    BMI calculator\u001b[0m\n\u001b[0m                 ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "BMI calculator\n",
    "\n",
    "name1 = \"NY\"\n",
    "height_m1 = 1.78\n",
    "weight_kg1 = 75\n",
    "\n",
    "name2 = \"ZZ\"\n",
    "height_m2 = 1.55\n",
    "weight_kg2 = 54\n",
    "\n",
    "name3 = \"NB\"\n",
    "height_m3 = 1.61\n",
    "weight_kg3 = 46\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#BMI calculator\n",
    "\n",
    "name1 = \"NY\"\n",
    "height_m1 = 1.78\n",
    "weight_kg1 = 75\n",
    "\n",
    "name2 = \"ZZ\"\n",
    "height_m2 = 1.55\n",
    "weight_kg2 = 54\n",
    "\n",
    "name3 = \"NB\"\n",
    "height_m3 = 1.61\n",
    "weight_kg3 = 46"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bmi_calculator(name, height_m, weight_kg):\n",
    "    bmi = weight_kg / (height_m ** 2)\n",
    "    print(\"bmi: \")\n",
    "    print(bmi)\n",
    "    if bmi < 25:\n",
    "        return name + \" is not overweight\"\n",
    "    else: \n",
    "        return name + \" is overweight\"\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bmi: \n",
      "23.671253629592222\n",
      "bmi: \n",
      "22.476586888657646\n",
      "bmi: \n",
      "17.746228926353147\n"
     ]
    }
   ],
   "source": [
    "result1 = bmi_calculator(name1, height_m1, weight_kg1)\n",
    "result2 = bmi_calculator(name2, height_m2, weight_kg2)\n",
    "result3 = bmi_calculator(name3, height_m3, weight_kg3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NY is not overweight\n",
      "ZZ is not overweight\n",
      "NB is not overweight\n"
     ]
    }
   ],
   "source": [
    "print(result1)\n",
    "print(result2)\n",
    "print(result3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# km = 1.6 * miles\n",
    "# the following function converts km to miles\n",
    "\n",
    "def convert_m2km(miles):\n",
    "    return 1.6 * miles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "708.8000000000001"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "convert_m2km(443)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "# the following function converts miles to km\n",
    "\n",
    "def convert_km2m(km):\n",
    "    return km / 1.6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "442.5"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "convert_km2m(708)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<function convert_km2m at 0x112b99320>\n"
     ]
    }
   ],
   "source": [
    "print(convert_km2m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45.625\n"
     ]
    }
   ],
   "source": [
    "print(convert_km2m(73))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
