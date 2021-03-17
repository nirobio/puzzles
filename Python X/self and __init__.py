{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# class is a set having some attribute in common\n",
    "# object is one instance of the class which can perform its f(x)\n",
    "# self represents the instance of the class\n",
    "\n",
    "# __init__ is a constructor which is used when we create an object\n",
    "# of a given class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# here we are creating the class car with atrributes\n",
    "\n",
    "class Car(object):\n",
    "    #blueprint for car\n",
    "    \n",
    "    def __init__(self, model, colour, company, top_speed):\n",
    "        self.model = model\n",
    "        self.colour = colour\n",
    "        self.company = company\n",
    "        self.top_speed = top_speed\n",
    "        \n",
    "    def start(self):\n",
    "        print(\"started\")\n",
    "        \n",
    "    def stop(self):\n",
    "        print(\"stopped\")\n",
    "        \n",
    "    def accelerate(self):\n",
    "        print(\"accelerating...\")\n",
    "        #insert accelerator f(x) here\n",
    "        \n",
    "    def change_gear(self, gear_type):\n",
    "        print(\"gear changed\")\n",
    "        #insert gear-related f(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "audi = Car(\"A6\", \"red\", \"audi\", 80)\n",
    "porsche = Car(\"911\", \"yellow\", \"porsche\", 120)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# self represents an instance of the class and binds the attribute\n",
    "# with the given arguments. Using self in a class to access methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "80"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "audi.top_speed"
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
