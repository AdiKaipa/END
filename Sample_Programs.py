{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Sample Programs.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP8ro6iE8vpv9wXAeizn0C6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AdiKaipa/END/blob/main/Sample_Programs.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IOWU5cMHEr-q"
      },
      "source": [
        "# write a python program to find sum of multiples of 3 or 5 below user provided number\r\n",
        "def Sum_of_Multiples(n, a = 3, b = 5):\r\n",
        "  return sum([i for i in range(1, n) if (i % 3) * (i % 5) == 0])\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Rk_CWDTuHMKV"
      },
      "source": [
        "# write a python program to find power digit sum for user provided numbers\r\n",
        "def Power_digit_Sum(a, n):\r\n",
        "  return sum([int(ch) for ch in str(a ** n)])\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HCZv_0AzJKoP"
      },
      "source": [
        "# write a python program to find sum square difference for user provided number\r\n",
        "def Sum_Square_Diff(n):\r\n",
        "  return sum([(n * (n + 1) / 2) ** 2]) - sum([i * i for i in range(1, n + 1)])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yh95QrfeKngR"
      },
      "source": [
        "# write a python program to find the difference between larget and smallest integers in the list\r\n",
        "def Max_Min_Diff(list_num):\r\n",
        "  return max(list_num) - min(list_num)\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AxLkYl7IOZQp",
        "outputId": "cb1a44d6-9364-4794-833d-c0aa78aef28d"
      },
      "source": [
        "# write a python program to find the frequency of characters in the given string\r\n",
        "string = \"hello how are you\"\r\n",
        "char_dict = {}\r\n",
        "for ch in string:\r\n",
        "  if ch in char_dict.keys():\r\n",
        "    char_dict[ch] += 1\r\n",
        "  else:\r\n",
        "    char_dict[ch] = 1\r\n",
        "for k, v in char_dict.items():\r\n",
        "  print(k, ':', v)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "h : 2\n",
            "e : 2\n",
            "l : 2\n",
            "o : 3\n",
            "  : 3\n",
            "w : 1\n",
            "a : 1\n",
            "r : 1\n",
            "y : 1\n",
            "u : 1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rpWwkRAxQtWV"
      },
      "source": [
        "# write a python program to find the reverse of the string\r\n",
        "def Reverse(string):\r\n",
        "  return string[::-1]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QMDuwf4qS0SF"
      },
      "source": [
        "# write a python program to check whether the string is even?\r\n",
        "def Is_Even(String):\r\n",
        "  return len(String) % 2 == 0\r\n",
        "  "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2mKchBgKTeXP"
      },
      "source": [
        "# write a python program to convert user provided number into string of dashes\r\n",
        "def Dashes(n):\r\n",
        "  return '-' * n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UdTsQsSVUdLi",
        "outputId": "76464a47-b3ac-493c-a961-d1b882435e54"
      },
      "source": [
        "# write a python program that converts lower case to upper case and vice versa\r\n",
        "string = \"HeLlo\"\r\n",
        "con_string = \"\"\r\n",
        "for ch in string:\r\n",
        "  if ch >= 'A' and ch <= 'Z':\r\n",
        "    con_string += ch.lower()\r\n",
        "  else:\r\n",
        "    con_string += ch.upper()\r\n",
        "print(f\"Converted string: {con_string}\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Converted string: hElLO\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XamRdqQ3iLVv"
      },
      "source": [
        "# write a python program to find the number of digits in the user provided integer number\r\n",
        "def Num_of_Digits(n):\r\n",
        "  return len(str(n))\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fN2NuLlzkADK"
      },
      "source": [
        "# write a python program which takes user provided string and returns the space between the characters\r\n",
        "def Space_bt_char(string):\r\n",
        "  return ' '.join(list(string))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-qvrl8T4mWCT"
      },
      "source": [
        "# write a python program that return unique characters in the string\r\n",
        "def Unique_char(string):\r\n",
        "  return set(string)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7IiF_6THm-98"
      },
      "source": [
        "# write a python program which returns the largest digit in the user provided integer number\r\n",
        "def Largest_digit(n):\r\n",
        "  return max([int(ch) for ch in str(n)])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8nnJW_kQn-_r",
        "outputId": "2c42d582-d565-46f2-ae60-07d8c04e93cd"
      },
      "source": [
        "# write a python program to sum of factors of a number\r\n",
        "n = 28\r\n",
        "sum_factors = sum([i for i in range(1, n) if n % i == 0])\r\n",
        "print(f\"Sum of factors: {sum_factors}\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Sum of factors: 28\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UJbaQMOGpDhe"
      },
      "source": [
        "# write a python program that filters the strings from the user provided list\r\n",
        "def Filter_string(list_):\r\n",
        "  return [v for v in list_ if type(v) != str]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Rx8EjtJGq7mV"
      },
      "source": [
        "# write a python program to count the number of duplicate characters in the user provided string\r\n",
        "def Duplicate_char_count(string):\r\n",
        "  return len(string) - len(set(string))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bpS7rjBIwbyv",
        "outputId": "67d0d8f7-b405-435e-b311-3bf17ac6dc5a"
      },
      "source": [
        "# write a python program to find the absolute distance between the digits of two numbers\r\n",
        "n1 = 283\r\n",
        "n2 = 426\r\n",
        "dist = 0\r\n",
        "for x, y in zip(str(n1), str(n2)):\r\n",
        "  dist += abs(int(x) - int(y))\r\n",
        "print(f\"Absolute distance: {dist}\")\r\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Absolute distance: 11\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zL0wIS-R2Z7c"
      },
      "source": [
        "# write a python program to disply the last nth element of the list\r\n",
        "\r\n",
        "def nth_element(list1, n):\r\n",
        "  return list1[-n]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yrd_H2cj5h4k"
      },
      "source": [
        "# write a python program to sort the user provided list\r\n",
        "def Sort_list(list1):\r\n",
        "  return sorted(list1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bern8m7-4LfH"
      },
      "source": [
        "# write a python program to replace vowel by * in the user provided string\r\n",
        "def Replace_star(string):\r\n",
        "  for ch in string:\r\n",
        "    if ch in \"AEIOUaeiou\":\r\n",
        "      string = string.replace(ch, '*')\r\n",
        "  return string"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BsVV0R1u6WsD"
      },
      "source": [
        "# write a python program to replaces vowel by * and consonant by - in the user provided input\r\n",
        "def Replace_star_line(string):\r\n",
        "  for ch in string:\r\n",
        "    if ch in \"AEIOUaeiou\":\r\n",
        "      string = string.replace(ch, '*')\r\n",
        "    elif ch in \"bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ\":\r\n",
        "      string = string.replace(ch, '-')\r\n",
        "  return string"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ylvR_dEx7_1E"
      },
      "source": [
        "# write a python program to move capital letters to front in the user provided string\r\n",
        "def Move_front(string):\r\n",
        "  l = ''\r\n",
        "  u = ''\r\n",
        "  for ch in string:\r\n",
        "    if ch >='A' and ch <= 'Z':\r\n",
        "      u = u + ch \r\n",
        "    else:\r\n",
        "      l = l + ch \r\n",
        "  return u + l\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u296wgww9SPQ",
        "outputId": "cc684202-bce3-4302-c63e-9c0bebb18aeb"
      },
      "source": [
        "# write a python program find all the number which are divisible by 7 but not 7 in the given range\r\n",
        "n1 = 230\r\n",
        "n2 = 450\r\n",
        "l = []\r\n",
        "for i in range(n1, n2):\r\n",
        "  if (i % 7 == 0) and (i % 5 != 0):\r\n",
        "    l.append(i)\r\n",
        "print(f\"List: {l}\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "List: [231, 238, 252, 259, 266, 273, 287, 294, 301, 308, 322, 329, 336, 343, 357, 364, 371, 378, 392, 399, 406, 413, 427, 434, 441, 448]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "298mWuLxGRbN"
      },
      "source": [
        "# write a python program to find factorial of a user provided integer number\r\n",
        "def Factorial(n):\r\n",
        "  if n == 0:\r\n",
        "    return 1\r\n",
        "  return n * Factorial(n - 1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XSC8rdeydTX9"
      },
      "source": [
        "# write a python program to find gcd of two user provided numbers\r\n",
        "def Gcd(a, b):\r\n",
        "  if a % b == 0:\r\n",
        "    return b \r\n",
        "  return Gcd(b, a % b)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vo6DptBJdvXS"
      },
      "source": [
        "# write a python program to exchange first and last digit of the user provided number\r\n",
        "def Exchange(n):\r\n",
        "  s = list(str(n))\r\n",
        "  s[0], s[-1] = s[-1], s[0]\r\n",
        "  return int(''.join([ch for ch in s]))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QuiHWlqEgbpA"
      },
      "source": [
        "# write a python program to check whether the length of two user provided strings is same\r\n",
        "def Is_length_same(string1, string2):\r\n",
        "  return len(string1) == len(string2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dfrA_Nl0hhn5"
      },
      "source": [
        "# write a python program to concatenate user provided first and last names \r\n",
        "def Concat(first_name, last_name):\r\n",
        "  return first_name + last_name"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UrrzSlcEisbm"
      },
      "source": [
        "# write a python program to check whether the user provided string ends with character n\r\n",
        "def Is_last_char(string):\r\n",
        "  return string[-1] == 'n' or string[-1] == 'N'"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "flst2jPuj51n"
      },
      "source": [
        "# write a python program to count the frequency of the user provided character in the string\r\n",
        "def Freq(string, ch):\r\n",
        "  return string.count(ch)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bQxX3uLslgmN"
      },
      "source": [
        "# write a python program to whether to strings are identical for case insensitive comparision\r\n",
        "def Is_identical(string1, string2):\r\n",
        "  return string1.lower() == string2.lower()\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "802zdn4Ko1Ka"
      },
      "source": [
        "# write a python program which checks whether the triangle is right angle at a for the user provided numbers a, b, c\r\n",
        "def Is_rightangle(a, b, c):\r\n",
        "  return a * a == b * b + c * c"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AcAlvpKMqao4"
      },
      "source": [
        "# write a python program to display kth digit from the last for the user provided number\r\n",
        "def Kth_digit_last(n, k):\r\n",
        "  return int(list(str(n))[-k])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kuMjQPcZxvFd"
      },
      "source": [
        "# write a python program to print sum of even digits of a user provided number\r\n",
        "def Sum_even_digit(n):\r\n",
        "  return sum([int(i) for i in str(n) if int(i) % 2 == 0])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-3xoLQ4Nyi1c"
      },
      "source": [
        "# write a python program to find last odd digit in the user provided number\r\n",
        "def Last_odd_digit(n):\r\n",
        "  return [int(i) for i in str(n) if int(i) % 2 != 0][-1]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s7OZSHLGzrON"
      },
      "source": [
        "# write a program to find the first even digit in the user provided input\r\n",
        "def First_even_digit(n):\r\n",
        "  return [int(i) for i in str(n) if int(i) % 2 == 0][0]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CwRAj3uH0UkG"
      },
      "source": [
        "# write a python program to find smallest digit in the user provided number\r\n",
        "def Smallest_digit(n):\r\n",
        "  return min([int(i) for i in str(n)])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-5z9PC4n0Rbu"
      },
      "source": [
        "# write a python program which displays the last of all factors of user provided number\r\n",
        "def Last_digit_factor(n):\r\n",
        "  return [i % 10 for i in range(1, n) if n % i == 0]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bWSQZprA2dHF"
      },
      "source": [
        "# write a python program that returns digits to number\r\n",
        "def digit2num(digit):\r\n",
        "  return int(''.join( [str(d) for d in digit]))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3161AVMN-Roa"
      },
      "source": [
        "# write a python program to check whether the given number is power of two\r\n",
        "def is_power_2(n):\r\n",
        "  if n == 1:\r\n",
        "    return True \r\n",
        "  if n % 2 != 0:\r\n",
        "    return False \r\n",
        "  return is_power_2(n // 2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "J6AWgyWc_X3C"
      },
      "source": [
        "# write a python program to check whether the given strings are anagrams\r\n",
        "def is_anagram(word1, word2):\r\n",
        "  return sorted(word1) == sorted(word2)\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jw3bJ2SJ_8es"
      },
      "source": [
        "# write a python program to count number vowels in the given string\r\n",
        "def Num_of_vowels(string):\r\n",
        "  ans = 0\r\n",
        "  for ch in string:\r\n",
        "    if ch in \"aeiouAEIOU\":\r\n",
        "      ans += 1\r\n",
        "  return ans\r\n",
        "\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZHwwNf_kAmSn"
      },
      "source": [
        "# write a python program to count the occurrances of each word in sentence\r\n",
        "def word_count(sent):\r\n",
        "  word_dict = {}\r\n",
        "  words = sent.split()\r\n",
        "  for w in words:\r\n",
        "    if w in word_dict.keys():\r\n",
        "      word_dict[w] += 1\r\n",
        "    else:\r\n",
        "      word_dict[w] = 1\r\n",
        "  return word_dict"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pix2ZP-nCqHk"
      },
      "source": [
        "# write a python program to find maximum odd number from user provided list\r\n",
        "def Max_odd(list1):\r\n",
        "  return max([k for k in list1 if k % 2 != 0])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xZ8WUuzgD0KH"
      },
      "source": [
        "# write a python program to find maximum number whose last digit is even for the user provided list\r\n",
        "def Max_lastdigit_even(list1):\r\n",
        "  return max([k for k in list1 if (k % 10) % 2 == 0])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QIW_4PgOE1hf"
      },
      "source": [
        "# write a python program to find sum of all number excluding maximum number from the list \r\n",
        "def sum_exclude_max(list1):\r\n",
        "  return sum(list1) - max(list1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0f9y23KyFRgN"
      },
      "source": [
        "# write a python program to check user provided two strings are circular permutations of each other\r\n",
        "def Circular_permu(a, b):\r\n",
        "  return a in b + b"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XrjYMat3V-7w"
      },
      "source": [
        "# write a python program to check whether the user provided number is perfect square\r\n",
        "def Is_square(n):\r\n",
        "  p = 1\r\n",
        "  while p * p < n:\r\n",
        "    p += 1\r\n",
        "  return p == n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NQI2tfUSY13N"
      },
      "source": [
        "# write a python program to check whether the user provided string is palindrome\r\n",
        "def Palindrome(string):\r\n",
        "  if len(string) == 0:\r\n",
        "    return True\r\n",
        "  if string[0] != string[-1]:\r\n",
        "    return False \r\n",
        "  return Palindrome(string[1: -1])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "g2BtyFyvbNj1"
      },
      "source": [
        "# write a python program to wheck whether the user given number is strong number\r\n",
        "def Fact(digit):\r\n",
        "  return [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880][digit]\r\n",
        "def Is_strong(n):\r\n",
        "  return sum([Fact(int(d)) for d in str(n)]) == n\r\n",
        "\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PWTVdWhbYXrw",
        "outputId": "6d0222e9-ad53-440f-8d2e-864d489908db"
      },
      "source": [
        "# write a python program to add two numbers \r\n",
        "num1 = 1.5\r\n",
        "num2 = 6.3\r\n",
        "sum = num1 + num2\r\n",
        "print(f'Sum: {sum}')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Sum: 7.8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9OOcSK-WYxae"
      },
      "source": [
        "# write a python function to add two user provided numbers and return the sum\r\n",
        "def add_two_numbers(num1, num2):\r\n",
        "    sum = num1 + num2\r\n",
        "    return sum"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8xpGoE8dY160",
        "outputId": "79a79f8b-57e8-4cf1-8c96-44437f568575"
      },
      "source": [
        "# write a program to find and print the largest among three numbers\r\n",
        "\r\n",
        "num1 = 10\r\n",
        "num2 = 12\r\n",
        "num3 = 14\r\n",
        "if (num1 >= num2) and (num1 >= num3):\r\n",
        "   largest = num1\r\n",
        "elif (num2 >= num1) and (num2 >= num3):\r\n",
        "   largest = num2\r\n",
        "else:\r\n",
        "   largest = num3\r\n",
        "print(f'largest:{largest}')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "largest:14\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5iDstv8RY6Hk"
      },
      "source": [
        "# write a program to find sum of square of first number and cube of second number\r\n",
        "def Sum_square_cube(n1, n2):\r\n",
        "  return n1 ** 2 + n2 ** 3"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z_vRzpLCZcw2"
      },
      "source": [
        "# write a program to find area of a triangle\r\n",
        "def Area_triangle(a, b, c):\r\n",
        "  s = (a + b + c) / 2\r\n",
        "  val = s * (s - a) * (s - b) * (s - c) \r\n",
        "  return val ** 1/2\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wiFARV6GaPJm",
        "outputId": "3c6d3891-d35e-4b19-8ec2-9db76724c7fc"
      },
      "source": [
        "# write a program which prints all even numbers which are multiplies of 3 in the rane 20 to 70\r\n",
        "even_num = []\r\n",
        "for i in range(20, 70):\r\n",
        "  if i % 2 == 0 and i % 3 == 0:\r\n",
        "    even_num.append(i)\r\n",
        "print(f\"even numbers multiplies of 3: {even_num}\")\r\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "even numbers multiplies of 3: [24, 30, 36, 42, 48, 54, 60, 66]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1wwQZGxubmVV"
      },
      "source": [
        "# write a program to find first even digit of the user given number\r\n",
        "def First_even_digit(n):\r\n",
        "  while n != 0:\r\n",
        "    if (n % 10) % 2 == 0:\r\n",
        "      even = n % 10\r\n",
        "    n = n // 10\r\n",
        "  return even"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X88IlOxxbf_U"
      },
      "source": [
        "# write a program to delete first k digits of the number\r\n",
        "def Del_first_k(n, k):\r\n",
        "  return int(''.join([ch for i, ch in enumerate(str(n)) if i >= k]))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rkt2h31wDnGR"
      },
      "source": [
        "# write a python program which repeats each character once in the given string\r\n",
        "def Repeated_string(string):\r\n",
        "  s = ''\r\n",
        "  for ch in string:\r\n",
        "    s = s + 2 *ch\r\n",
        "  return s"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "b_2_K_KjFXtt",
        "outputId": "7caefa76-ed1c-4b57-fd8f-d21be0036a45"
      },
      "source": [
        "Repeated_string(\"Hello\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'HHeelllloo'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 60
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BA-KUBh8Flze"
      },
      "source": [
        "# write a python program which list with non-negative integers and string and returns list without strings\r\n",
        "def Without_string(list1):\r\n",
        "  return [v for v in list1 if type(v) != str]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qU4V6WfqGZbv"
      },
      "source": [
        "# write a python program which returns the position of upper case characters in the given string\r\n",
        "def Index_uppercase(string):\r\n",
        "  ind = []\r\n",
        "  for i, ch in enumerate(string):\r\n",
        "    if ch >= 'A' and ch<='Z':\r\n",
        "      ind.append(i)\r\n",
        "  return ind\r\n",
        "\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ou1qhxMfHigm"
      },
      "source": [
        "# write a python program which returns the position of upper case characters in the given string\r\n",
        "def Ind_uppercase(s):\r\n",
        "  return [i for i, ch in enumerate(s) if ch >= 'A' and ch <= 'Z']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dr4R9WiBIEgQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e1f4913f-3bf5-4935-d552-0fef6404d844"
      },
      "source": [
        "# write a program to swap two numbers\r\n",
        "n1 = 5\r\n",
        "n2 = 10\r\n",
        "n1, n2 = n2, n1\r\n",
        "print(f\"After swap: {n1, n2}\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "After swap: (10, 5)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Zdv3fbBEQ_yP"
      },
      "source": [
        "# write a program to check whether the string is empty\r\n",
        "def Is_empty(string):\r\n",
        "  return len(string) == 0"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "92q36SHwSlXt"
      },
      "source": [
        "# write a program to check the whether the given string is title string\r\n",
        "def Is_title(string):\r\n",
        "  return string == string.title()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qNBAu688U2rm"
      },
      "source": [
        "# write a program to convert list elements into string\r\n",
        "def Convert_string(list1):\r\n",
        "  return [str(ch) for ch in list1]\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LO4daLryWLjR"
      },
      "source": [
        "# write a program to find second largest number from the user provided list\r\n",
        "def Sec_largest(list1):\r\n",
        "  largest = sec_largest = -99999\r\n",
        "  for v in list1:\r\n",
        "    if v > largest:\r\n",
        "      sec_largest = largest\r\n",
        "      largest = v\r\n",
        "    elif v > sec_largest:\r\n",
        "      sec_largest = v\r\n",
        "  return sec_largest"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DVYYS_C8Zwom"
      },
      "source": [
        "# write a program largest and second largest for the given list\r\n",
        "def Sec_largest(list1):\r\n",
        "  largest = sec_largest = -99999\r\n",
        "  for v in list1:\r\n",
        "    if v > largest:\r\n",
        "      sec_largest = largest\r\n",
        "      largest = v\r\n",
        "    elif v > sec_largest:\r\n",
        "      sec_largest = v\r\n",
        "  return largest, sec_largest"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G-u6Um71bEiH"
      },
      "source": [
        "# write program to check whether the given number is armstrong number\r\n",
        "def Armstrong(n):\r\n",
        "  s = [int(d) for d in str(n)]\r\n",
        "  print(s)\r\n",
        "  return sum([d ** len(s) for d in s]) == n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CE2VLX26dnZD"
      },
      "source": [
        "# write a program which repeats the last character of string n times\r\n",
        "def Repeat_last_char(s, n):\r\n",
        "  return s[:-1] + n * s[-1]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PW-ywWUxbtgs"
      },
      "source": [
        "# write a program which revrses words of the string \r\n",
        "def Word_reverse(sent):\r\n",
        "  words = sent.split()\r\n",
        "  return words[::-1]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iWxP--V0fq6D"
      },
      "source": [
        "# write a program which reverses and capitalizes the string\r\n",
        "def Reverse_capital(string):\r\n",
        "  return string[::-1].upper()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mS69W1_JgLcR"
      },
      "source": [
        "# write a program which the make the mirror image of the given number\r\n",
        "def Mirror_img(n):\r\n",
        "  return int(str(n) + str(n)[::-1])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZBaCW-Wyg0oN"
      },
      "source": [
        "# write a program which returns the single occurrance of a character\r\n",
        "def Single_occurrance(string):\r\n",
        "  d = {}\r\n",
        "  for ch in string:\r\n",
        "    if ch in d.keys():\r\n",
        "      d[ch] += 1\r\n",
        "    else:\r\n",
        "      d[ch] = 1\r\n",
        "  for k, v in d.items():\r\n",
        "    if v == 1:\r\n",
        "      return k"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CV3_GmSCh1b0"
      },
      "source": [
        "# write a program which the given list of numbers\r\n",
        "def Negate(list1):\r\n",
        "  return -1*list1"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G-RVOVSMgPnO"
      },
      "source": [
        "# write a program to find mean of the list of numbers\r\n",
        "def Mean(list1):\r\n",
        "  return mean(list1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sbUEZvO8jB16"
      },
      "source": [
        "# write a program to find sum of squares of even number for the given list\r\n",
        "def Sum_square_even(list1):\r\n",
        "  return sum([d ** 2 for d in list1 if d % 2 == 0])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k1OlES9xkWMh"
      },
      "source": [
        "# write a program to count number True's in the given list\r\n",
        "def Num_trues(list1):\r\n",
        "  return sum([int(t) for t in list1])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fL4FEGPKlpEz"
      },
      "source": [
        "# write a program to check whether the string contains identical characters\r\n",
        "def Identical_Char(s):\r\n",
        "  return len(set(s)) == 1"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Twp-hsETlPLQ"
      },
      "source": [
        "# write a program to find number of characters in the given two strings\r\n",
        "def Num_char(s1, s2):\r\n",
        "  return len(set(s1 + s2))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7oxNX5w3mvCw"
      },
      "source": [
        "# write a program to find product of odd integers\r\n",
        "def prod_of_odd(list1):\r\n",
        "  return prod([v for v in list1 if v % 2 == 1])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WbX_g9s0oByP"
      },
      "source": [
        "# write a program which returns the 4 letter strings from the given list\r\n",
        "def Four_letter_str(list1):\r\n",
        "  return [s for s in list1 if len(s) == 4]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MgrlSpoJovQ7"
      },
      "source": [
        "# write a program to find largest numbers from the list of lists\r\n",
        "def Largest(list1):\r\n",
        "  return [max(l) for l in list1]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hBuAc-D_pV1G"
      },
      "source": [
        "# write a program to check whether the given number is prime\r\n",
        "def Is_prime(n):\r\n",
        "  for i in range(2, n):\r\n",
        "    if n % i == 0:\r\n",
        "      return False\r\n",
        "  return True\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aGfVoIbFoo8W"
      },
      "source": [
        "# write a program to find length of tuple\r\n",
        "def Length(t):\r\n",
        "  return len(t)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zSE0Gseptq4L"
      },
      "source": [
        "# write the program to find all fibonacci number in the given range\r\n",
        "def fibonacci(n):\r\n",
        "  fib = [0, 1]\r\n",
        "  while fib[-1] + fib[-2] < n:\r\n",
        "    fib.append(fib[-1] + fib[-2])\r\n",
        "  return fib\r\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lynfEMJ2sabz"
      },
      "source": [
        "# write a program which display all even numbers in the given range\r\n",
        "def Even_range(r1, r2):\r\n",
        "  even = []\r\n",
        "  for n in range(r1, r2):\r\n",
        "    if n % 2 == 0:\r\n",
        "      even.append(n)\r\n",
        "  return even"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1az6Z1ZzvQ8-"
      },
      "source": [
        "# write a program which find the length of the dictionary\r\n",
        "def Length_dict(d):\r\n",
        "  return len(d)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i2jbA7xgv0cV"
      },
      "source": [
        "#write a program to display the keys in sorted order for the given dictionary\r\n",
        "def sort_key(d):\r\n",
        "  d = sorted(d.keys())\r\n",
        "  return d"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FfvjEWXEwQzU"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}