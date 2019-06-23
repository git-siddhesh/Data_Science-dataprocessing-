{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "pandasInClass",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
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
        "<a href=\"https://colab.research.google.com/github/git-siddhesh/Data_Science-dataprocessing-/blob/Data_processing/pandasInClass.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RNl29wCEJ6oZ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "#reading data from csv file\n",
        "df=pd.read_csv('com.csv')\n",
        "#df2=pd.read_csv('http://13.234.66.67/summer19/datasets/salary.csv')\n",
        "#df2    #to print the complete data \n",
        "df\n",
        "\n",
        "#to print the information of the data\n",
        "#df.info()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3roFU8-sNJHt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#to print particular coloumn\n",
        "df['Name']\n",
        "#to print the values of the name as array\n",
        "df['Name'].values"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F7FbUHq5LkCx",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#top 3v rows \n",
        "\n",
        "#df2.head(3)\n",
        "df.tail(3)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rG6IMBKSNsTm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#for selecting particular rows and column\n",
        "df.iloc[0:,[0,2]]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bdbxo_MxOFSO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#to know the things you can do with df['Salary']\n",
        "dir(df['Salary'])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZMq60ypLOBE4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#to print max() or min(),avg(),mean() salary \n",
        "df['Salary'].mean()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RejKrl8FPtC2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "df.values\n",
        "#data in the rows and columns are just set of lists of same size"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MwTid5BtQJzf",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}