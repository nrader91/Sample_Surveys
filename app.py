{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d7426de5",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-086181c1e886>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mQuestion\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mQuestion\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m question_prompts = [ \n\u001b[0;32m      4\u001b[0m     \u001b[1;34m\"what color are apples?\\n(a) Red/Green\\n(b) Purple\\n(c) Orange\\n\\n\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;34m\"what color are bananas?\\n(a) Teal\\n(b) Magenta\\n(c) Yellow\\n\\n\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Sample_Surveys\\Question.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"3f3930af\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "from Question import Question\n",
    "\n",
    "question_prompts = [ \n",
    "    \"what color are apples?\\n(a) Red/Green\\n(b) Purple\\n(c) Orange\\n\\n\",\n",
    "    \"what color are bananas?\\n(a) Teal\\n(b) Magenta\\n(c) Yellow\\n\\n\",\n",
    "    \"what color are strawberries?\\n(a) Yellow\\n(b) Red\\n(c) Blue\\n\\n\"\n",
    "]\n",
    "\n",
    "\n",
    "questions = [\n",
    "    Question(question_prompts[0], \"a\"),\n",
    "    Question(question_prompts[1], \"c\"),\n",
    "    Question(question_prompts[2], \"b\"),\n",
    "]\n",
    "\n",
    "\n",
    "\n",
    "def run_test(questions):\n",
    "    score = 0\n",
    "    for question in questions:\n",
    "        answer = input(question.prompt)\n",
    "        if answer == question.answer:\n",
    "            score += 1\n",
    "    print(\"You got \" + str(score) + \"/\" + str(len(questions)) + \"correct\")\n",
    "    \n",
    "run_test(questions)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "934eabf0",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
