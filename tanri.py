{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNGkpHHgFx66Svz/wmYtq04",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/ikedamasami/test2022/blob/main/tanri.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MoFDPZWoINBB",
        "outputId": "bcbdb4b2-c5ca-4970-bf7f-896ccc971fb2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "元金を入力してください510000\n",
            "年利率を入力してください1.55\n",
            "日数を入力してください120\n",
            "2598\n"
          ]
        }
      ],
      "source": [
        "gankin = int(input(\"元金を入力してください\"))\n",
        "riritu = float(input(\"年利率を入力してください\"))\n",
        "nisu = int(input(\"日数を入力してください\"))\n",
        "risoku = int(gankin * riritu / 100 * nisu / 365)\n",
        "print(risoku)"
      ]
    }
  ]
}
